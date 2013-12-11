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

越仔细看，觉得这个项目写的真是高深啊，，
