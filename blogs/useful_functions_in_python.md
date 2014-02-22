记录一些有用但是不常用的的函数
=====
常看文档有益身心健康，一下是从[http://docs.python.org/2.7/library/functions.html](http://docs.python.org/2.7/library/functions.html)中列出的一些有意思的函数，虽然平时不常用，看看还是挺有意思的。

如何判断一个序列的元素都是true？
---
先来最直观的：

    def true_sequence(seq):
        for one in seq:
            if not one:
                return False
        return True

这个看着很流畅哈，一目了然啊，built_in里已经定义了这么个东西叫all(),下次直接用all就好了。
文档也是这么写得，哈哈哈哈。

如何判断一个序列的元素至少有一个为True？
----

    def true_element(seq):
        for one in seq:
            if one:
                return True
        return False
这个函数built_in里也有了，叫any,下次用any就可以了，呵呵

enumerate
---
这个经常用们可以看一下：

    enumerate(list,start)

这个函数返回的(element_index,element)的遍历器，有没有感觉跟django里的for tag里的for_loop.counter有点像？对，django这个实现这个时候的时候确实用到了这个函数，不过并没有使用start这个参数，只提供了从0开始和从1开始两种。有没有觉得很好玩，，哈哈

filter(function, iterable)
---
这个和map，reduce放一起就是函数式(lisp,schema)在python里的体现，不过目前很多人不建议用这个东西，希望用list comprehension来代替，我的看法是用不用的看个人，*你可以不用，但是你要看得懂*。这个观点同样使用于django的CBV和FBV。因为总有些人喜欢用（鸟和林子神马的），
filter对应的list comprehension形式：

    [item for item in iterable if function(item)]# if function
    [item for item in iterable if item] # if not function

itertools里面还有一个ifilter的版本，作用是一样，返回的是遍历器（省内存，python性能不好，呵呵）

format
-----
这个东西不放这里说：单开一章，，=。=

