#### Classes and Object-oriented Programming
类是创建新对象的机制，本章包含类的各种细节，但是不是一个面向对象编程和设计的参考。我们假定读者有其他编程语言（c或者java）数据结构和面向对象编程的经验。
#class语句
类顶了一堆属性，这些属性被对象实例共享。类实际上是函数、变量和属性的集合。
有一点很重要，就是一个class语句不创建任何对象，它只设定了一些所有的要被创建实例的实例的属性。类里定义的函数就是所谓的实例方法。实例方法就是一个类的实例使用的方法，它的第一个参数是类，一般就是self。

*如何统计类有多少实例：

    class Account(object):
        num_account = 0
        def __init__(self,name,balance):
            self.name=name
            self.balance = balance
            Account.num_account += 1
        def __del__(self):
            Account.num_account -= 1
#Class Instance
“.”操作符负责属性绑定，当我们访问一个属性，返回的结果有可能来自几个地方。首先实例本身检查并且如果没有，访问实例的类。这是类如何于实例分享属性的底层机制。
## Scoping Rules
## Inheritance
继承是一个创建一个特殊化或者修改现有类的行为的机制。

## Static Methods and Class Methods
静态方法的一个一般用途就是你可以有很多不同的方法来创建新的实例。因为一个类只可以有一个__init__方法。其他创建实例的方法可以用静态函数来实现。

##类方法
类方法的第一个参数是cls
##属性（Properties）
这个可以避免使用的时候的一个不一致，就是一个解果要不要加（）的问题。
