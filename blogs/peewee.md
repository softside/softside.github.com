阅读peewee代码
====

细致分析一个orm的源码对于我们可以正确的使用orm带来的帮助是非常的明显的，虽然之前试图分析django的orm部分，但是没有坚持下来，其实peewee也是不错的啊，代码又少，提供的功能也还够用，值得我们深入学习一下。peewee的作者还是[readthedocs.org](https://readthedocs.org)的创建人之一。
[Shortcomings in the Django ORM and a look at Peewee, a lightweight alternative](http://charlesleifer.com/blog/shortcomings-in-the-django-orm-and-a-look-at-peewee-a-lightweight-alternative/)

和django orm一样采用了“声明式”（declarative）的方式，这是一种比较先进的方式，sqlalchemy现在也提供了这种方式，ror的active record也是类似的方式。
来个简单的例子，熟悉django的筒子是不是很眼熟，，我们通篇都拿这个“人”（Person）来分析，

    from peewee import *

    db = SqliteDatabase('people.db')

    class Person(Model):
        name = CharField()
        birthday = DateField()
        is_relative = BooleanField()

        class Meta:
            database = db # this model uses the people database
我们大概看一下peewee的Model部分：这里有个`__metaclass__== BaseModel`,好神奇啊有木有，呵呵。

Question 1,如何取得用户定义的信息？
----
声明式，我们说是啥就有啥，我们说有一个名字（name）就有一个名字，说有生日（birthday）就有生日，是不是有上帝的感觉，呵呵（悲催的码农也就这点乐趣了，呵呵）。好了，框架是怎么知道我们定义了啥呀？
当我们定义了Person这个类，继承了peewee的Model，我们观察这个Model：
    
    class Model(object):
        __metaclass__ = BaseModel

        def __init__(self, *args, **kwargs):
            self._data = self._meta.get_default_dict()
            self._obj_cache = {} # cache of related objects
    
            for k, v in kwargs.items():
                setattr(self, k, v)

有个__metaclass__属性是BaseModel，首先执行的是BaseModel的 `__new__`方法，然后执行Model的`__init__`方法。有木有很眼熟，不熟的筒子们看[这里](http://docs.python.org/2.7/reference/datamodel.html#object.__new__)
在BaseModel里有：

    def __new__(cls, name, bases, attrs):

我们看一下这四个参数是啥：
    
    <class 'peewee.BaseModel'>,
    Person,
    (<class 'peewee.Model'>,),
    {'__module__': 'person', 'birthday': <peewee.DateField object at 0x10342b3d0>, 'is_relative': <peewee.BooleanField object at 0x10342b4d0>, 'name': <peewee.CharField object at 0x10342b390>, 'Meta': <class my-test.Meta at 0x10340cb48>}

到这里是不是清楚了，在我们定义示例代码的时候，我们可以通过Person.__dict__获取需要信息。













     