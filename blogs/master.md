# saltstack源码分析

 *最近做有关saltstack(简称salt)的工作，为了更好的完成工作，需要对salt有更深入的了解*
## salt简单介绍
salt的定位是一个远程执行和配置管理的工具，用python写的。
我们定位应用salt的场景，在某些时候，我们需要临时租用大量的服务器来抗住瞬间爆发的大流量，这就需要我们在很短的时间内对一批服务器进行安装配置。
## salt架构
salt分为主服务器（master）和从服务器（minion）。我们在master机器上执行salt-master命令启动服务，在minion启动salt-minion上命令。master可以通过*salt*命令来控制minion。所以master就是大爷啊，让minion去执行各种命令.

通过简单的分析，我决定分为以下几个方面对salt的源码进行分析：

1. master的启动过程
2. minion的启动过程
3. salt命令的执行过程
4. maste和minion中间数据的传递

##salt-master的启动过程
我们在master端启动的时候执行的是salt-master命令，我们就从这个命令开始,其他的和这个类似，下次就不在详细描述了

    ➜  ~  salt-master --version
    salt-master 2014.1.4
    ➜  ~  which salt-master |xargs more
    #!/bin/bash
    PYTHONPATH="/usr/local/Cellar/saltstack/2014.1.4/libexec/lib/python2.7/site-packages:/usr/local/Cellar/saltstack/2014.1.4/lib/python2.7/site-packages" exec "/usr/local/Cellar/saltstack/2014.1.4/libexec/bin/salt-master" "$@"
    ➜  ~  more /usr/local/Cellar/saltstack/2014.1.4/libexec/bin/salt-master
    #!/usr/bin/python
    '''
    Start the salt-master
    '''
    
    from salt.scripts import salt_master
    
    
    if __name__ == '__main__':
        salt_master()
        
我们切换到salt的目录，找到这个salt_master函数，

    def salt_master():
        '''
        Start the salt-master.
        '''
        master = salt.Master()
        master.start()        
这个函数中调用了*salt.Master()*得start方法来启动服务，这个Master是类定义在*salt/__init__.py*中line52，它的父类是parsers.MasterOptionParser，这个父类还有父类(OptionParser)，还有一堆的mixin(ConfigDirMixIn, MergeConfigMixIn,LogLevelMixIn, RunUserMixin, DaemonMixIn,PidfileMixin)，然后，这个类还有meta class（WTF。。。）。好吧，其实这个不算什么，一般比较大型的项目都是这个样子的(不，不，我说的不是java，你误会了) 。
这个父类和一堆mixin都是倒腾我们在启动salt-master的时候后面指定的参数的，比如 *-l*，*-d*，*-c*，*--pid*,*-u*等等的。

其实很多项目（比如django）的utils啊parser啊等等目录的代码里，都有很多不错的代码，有兴趣的同学可以去看看，这部分的代码一般和项目的关系不是很大，相对而言更具有普遍意义。这个parser部分，我们先略过，以后单独分析，有需要提到的我会注明。

这个Master类自身的部分不是很多，不到100行的代码定义了三个方法，*prepare*,*start*,*shutdown*.	好吧，我们直奔start方法，

    110    def start(self):
    120        self.prepare()
    121        if check_user(self.config['user']):
    122            try:
    123                self.master.start()
    124            except MasterExit:
    125                self.shutdown()
    126            finally:
    127                sys.exit()
为了节省突出代码我删掉了110-120的注释，额，我们还是去看prepare这个方法吧。
    
    64        self.parse_args()
这个`parse_args()`方法定义在该类父类`MasterOptionParser`的父类`OptionParser`里,这个方法是读取启动salt-master的时候制定的参数，比如我们常用的*salt-master - l debug*,这个-l就是logging，debug是指定logging的级别，其他还有warning，info，error之类的。这个类继承了`optparser`（额，这个optparser已经deprecated了，用了一个新的叫argparser的包来代替，原因好像是经典类和新式类的问题，估计以后向python3迁移的时候会有麻烦，额，想多了，且等着呢，）的`OptionParser`
                

下面的代码来自OptionParser的parse_args方法，

	 184        process_option_funcs = []
	 185        for option_key in options.__dict__.keys():
	 186            process_option_func = getattr(
	 187                self, 'process_{0}'.format(option_key), None
	 188            )
	 189            if process_option_func is not None:
	 190                process_option_funcs.append(process_option_func)
	 191
	 192        for process_option_func in _sorted(process_option_funcs):
	 193            try:
	 194                process_option_func()
	 195            except Exception as err:
	 196                logging.getLogger(__name__).exception(err)
	 197                self.error(
	 198                    'Error while processing {0}: {1}'.format(
	 199                        process_option_func, traceback.format_exc(err)
	 200                    )
	 201                )        
        
line194真正执行各个mixin中定义的process_****(比如process_config_dir)，        

	 334    def process_config_dir(self):
	 335        if not os.path.isdir(self.options.config_dir):
	 336            # No logging is configured yet
	 337            sys.stderr.write(
	 338                'WARNING: {0!r} directory does not exist.\n'.format(
	 339                    self.options.config_dir
	 340                )
	 341            )
	 342
	 343        # Make sure we have an absolute path
	 344        self.options.config_dir = os.path.abspath(self.options.config_dir)
	 345
	 346        if hasattr(self, 'setup_config'):
	 347            try:
	 348                self.config = self.setup_config()
	 349            except (IOError, OSError) as exc:
	 350                self.error(
	 351                    'Failed to load configuration: {0}'.format(exc)
	 352                )        


然后再调用自己定义的setup_config，这里给master的instance增加了一个叫config的属性，这个属性很有用啊，所有在/etc/salt/master中定义的值都放到这个属性存起来等着用。

	1386    def setup_config(self):
	1387        return config.master_config(self.get_config_file_path())        

       
MasterOptionParser继承了ConfigDirMixIn，这个类是处理“－c”参数的，就是指定配置文件，这个类定义了一个get_config_file_path的方法：

	 354    def get_config_file_path(self, configfile=None):
	 355        if configfile is None:
	 356            configfile = self._config_filename_
	 357        return os.path.join(self.options.config_dir, configfile)    
取得配置文件的位置，交由config.master_config函数处理配置文件,这里读取yaml文件，放到self.config中供以后使用。

prepare()执行结束后就是self.master.start()了，这个self.master定义在salt/master.py
	106        self.master = salt.master.Master(self.config)

  
所以我们话这么大的篇幅来分析这个config从哪里来的是非常有意义的，因为这个self.config就是我们接下来要分析的salt/master.py这个文件中的opts，他们就是一个东西，opts就是我们从配置文件中读取的那个dictionary。        

下面我们转到salt/master这个文件，看看它都做了些啥，	
这里初始化了一个Master的instance，调用类的__init__方法，在这个方法里检查zeromp的版本，然后调用父类的__init__方法。调用的时候直接用父类名执行的，而没有用Super()方法:

    def __init__(self, opts):
            '''
            Create a salt master server instance
            '''
            # Warn if ZMQ < 3.2
            if not(hasattr(zmq, 'zmq_version_info')) or \
                    zmq.zmq_version_info() < (3, 2):
                # PyZMQ 2.1.9 does not have zmq_version_info
                log.warning('You have a version of ZMQ less than ZMQ 3.2!)
                .....    
            SMaster.__init__(self, opts)
这样做是有好处的。额，可能这里体现的不是很明显。

好了,前面纠结那么多，我们直接去看这个mater的start方法吧，不然估计这篇打不住了，果然是一个大项目啊；

    def start(self):
        '''
        Turn on the master server components
        '''
        self._pre_flight()
        log.info(
            'salt-master is starting as user {0!r}'.format(salt.utils.get_user())
        )

        enable_sigusr1_handler()

        self.__set_max_open_files()
        clear_old_jobs_proc = multiprocessing.Process(
            target=self._clear_old_jobs)
        clear_old_jobs_proc.start()
        reqserv = ReqServer(
                self.opts,
                self.crypticle,
                self.key,
                self.master_key)
        reqserv.start_publisher()
        reqserv.start_event_publisher()
        reqserv.start_reactor()
        reqserv.start_halite()
        #中间有省略
        try:
            reqserv.run()
        except KeyboardInterrupt:
            # Shut the master down gracefully on SIGINT
            log.warn('Stopping the Salt Master')
            raise SystemExit('\nExiting on Ctrl-c')        
        
好的，先看这么多，_pre_flight()这个方法是检查配置文件中的文件服务的，就是我们存放sls文件的设置，没有的话，服务就不起了。salt为了执行self._clear_old_jobs单独起了一个进程，reqserv.start_publisher()这个又单起了一个进程，reqserv.start_event_publisher()又是一个，所以这就3个进程了，，我们在master的配置文件里可以设置worker_threads,这个默认设置的是5个，reqserv.run()的时候，又来5个，具体实现在reqserv的_bind方法中

        #extracted from ReqServer._bind
        self.work_procs = []

        for ind in range(int(self.opts['worker_threads'])):
            self.work_procs.append(MWorker(self.opts,
                    self.master_key,
                    self.key,
                    self.crypticle))

        for ind, proc in enumerate(self.work_procs):
            log.info('Starting Salt worker process {0}'.format(ind))
            proc.start()

        self.workers.bind(self.w_uri)

所以启动salt-master以后我们执行`ps -ef |grep salt`
    

    ➜  salt git:(master) ps -ef |grep salt
      501  3918  3058   0  1:13上午 ttys002    0:00.89 /usr/bin/python /usr/local/Cellar/saltstack/2014.1.4/libexec/bin/salt-master -l debug
      501  3919  3918   0  1:13上午 ttys002    0:00.81 /usr/bin/python /usr/local/Cellar/saltstack/2014.1.4/libexec/bin/salt-master -l debug
      501  3920  3918   0  1:13上午 ttys002    0:00.01 /usr/bin/python /usr/local/Cellar/saltstack/2014.1.4/libexec/bin/salt-master -l debug
      501  3921  3918   0  1:13上午 ttys002    0:00.01 /usr/bin/python /usr/local/Cellar/saltstack/2014.1.4/libexec/bin/salt-master -l debug
      501  3922  3918   0  1:13上午 ttys002    0:01.24 /usr/bin/python /usr/local/Cellar/saltstack/2014.1.4/libexec/bin/salt-master -l debug
      501  3923  3918   0  1:13上午 ttys002    0:01.24 /usr/bin/python /usr/local/Cellar/saltstack/2014.1.4/libexec/bin/salt-master -l debug
      501  3924  3918   0  1:13上午 ttys002    0:01.26 /usr/bin/python /usr/local/Cellar/saltstack/2014.1.4/libexec/bin/salt-master -l debug
      501  3925  3918   0  1:13上午 ttys002    0:01.25 /usr/bin/python /usr/local/Cellar/saltstack/2014.1.4/libexec/bin/salt-master -l debug
      501  3926  3918   0  1:13上午 ttys002    0:01.25 /usr/bin/python /usr/local/Cellar/saltstack/2014.1.4/libexec/bin/salt-master -l debug    
        
数一下，正好9个。
        
        
        