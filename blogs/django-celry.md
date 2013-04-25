#### django-celery

## intro
系统中有很多地方需要用到队列，django-celery很好的完成这个部分，认真学习下还是很有必要的。


# reding the source 
setting里的设置

    import djcelery
    djcelery.setup_loader()

setup_loader()都做了什么：

    def setup_loader():
        os.environ.setdefault('CELERY_LOADER', 'djcelery.loaders.DjangoLoader')

DjangoLoader中有一个 *on_worker_init*的方法:

        def on_worker_init(self):
        """Called when the worker starts.

        Automatically discovers any ``tasks.py`` files in the applications
        listed in ``INSTALLED_APPS``.

        """
        self.import_default_modules()

        self.close_database()
        self.close_cache()

import_default_modules() 继续：

    def import_default_modules(self):
        super(DjangoLoader, self).import_default_modules()
        self.autodiscover()

self.autodiscover(),呵呵呵：

    def autodiscover(self):
        self.task_modules.update(mod.__name__ for mod in autodiscover() or ())

autodiscover(),继续呵呵:

      try:
        return filter(None, [find_related_module(app, 'tasks')
                                for app in settings.INSTALLED_APPS])

find_relate_module(),endind pose了：


    def find_related_module(app, related_name):
        """Given an application name and a module name, tries to find that
        module in the application."""

        try:
            app_path = importlib.import_module(app).__path__
        except AttributeError:
            return

        try:
            imp.find_module(related_name, app_path)
        except ImportError:
            return

        return importlib.import_module('{0}.{1}'.format(app, related_name))

## conclusion
不觉明厉啊，由此可以看出，我们只要在app里建一个tasks.py,这个loader就会自己加载。convention??
