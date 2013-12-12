django-rest-framework/rest_framwork/throttling.py
=====
[throttle](https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/throttling.py)

最近要写一个小的应用需要用到django-rest-framework这个框架，其中有个需求需要控制单个view的访问次数，看文档觉得有点绕，打开源码一看才200来行，我就哈哈哈了。

文件中一共实现了5个类：

1，一个基类(BaseThrottle)，这个类定义了`allow_request`和`wait` ，定义了子类需要定义的函数

2，SimpleRateThrottle,这个才是主要的类，

3，AnonRateThrottle，处理匿名用户的

4，UserRateThrottle ，处理登陆用户的

5，ScopedRateThrottle，这个是处理单个view的，可以在单个view中设置`throttle_scope`属性来定义

SimpleRateThrottle
--------
这个类是类3，4，5的基类，核心的方法是`allow_request`,需要处理两种情况，判断当前类rate是否存在和对应的key是否存在，如果不存在，返回True。核心的就是判断就是下面这些了：

        while self.history and self.history[-1] <= self.now - self.duration:
            self.history.pop()
        if len(self.history) >= self.num_requests:
            return self.throttle_failure()
        return self.throttle_success()

注意while后面的判断语句中的and，当第一次request的时候`self.history[-1]`是不会执行的，所以不会出现IndexError,这里面的pop是去除那些已经过时的请求时间，这样也是为了后面的计数做准备，这是类似滚动统计的，类似的还有比如24：00重置也是一个思路。

上面的类中实现了`throttle_failure`和`throttle_success`两个方法，因为

越仔细看，觉得这个项目写的真是高深啊，，

    WrappedAPIView = type(
        six.PY3 and 'WrappedAPIView' or b'WrappedAPIView',
             (APIView,),
             {'__doc__': func.__doc__}
        )
这里用type定义了一个新的object，名字是“WrappedAPIView,父类是APIView，`b`是这个意思，在python里无视，在python表明这是一个bytes，在2里还是'str'。
回答一个问题，就是这个检查的方法是什么时候、什么地方执行的，code在restframework/views.py中的lei的APIView的check_throttle函数中调用。

大面积的使用OOP真是噩梦啊，这不断的继承，调用真是，，

今天顺便还看了一下django的Class-based views部分的代码，我不喜欢这个，抽象，太抽象了，，


关于staticmethod,classmethod和啥都么有类方法，我们可以从他接受的参数来进行区分，
classmethod的第一个参数是class
staticmethod不接受任何参数
正常的接收的参数是self.

所以我们正常的时候使用的都是啥都不加的把，哈
