prelude-强大灵活简单易用的emacs配置包
====

***
强烈推荐[prelude](https://github.com/bbatsov/prelude)

这是什么
-----
这是一个emacs的配置文件，以前版本的.emacs文件放在home目录下的，emacs24的都是放在一个叫.emacs.d的目录下(prelude就是这个.emacs.d)


emacs经历
------
一开始用emacs的时候就是觉得很酷，也就一直用来着(当然也间或用sublime，主要就是这2个了)。最近照着别的的配置文件写，很烦的，毕竟个人的工作范畴不一样，目标也就不一样，还有emacs版本也不一样，总是千差万别，确实很折腾。其实我的要求并不高，没有什么特殊的需求，都是基本的功能，但是把这些基本的功能做好也是不容易的，更何况还有具体环境的差异(mac,linux,win).这个时候prelude出现了(还有一个叫start-kit)。


prelude
----
其实prelude的出现和emacs24有很大的关系，早在还在pre阶段的时候其作者就大力推荐了。但是这个项目开始的时候不是很成熟，存在这样那样的问题，好在社区的力量是强大的，在我看来这个项目已经可以用了。

怎么用
----
1.fork prelude

    git clone git@github.com:newlife/prelude.git
    ln -s prelude .emacs.d

2.add remote

    git remote add upstream https://github.com/bbatsov/prelude.git

当remote的包有更新的时候可以

    git fetch upstream
    git merge upstream/master

2.create personal

3.创建.gitsubmodule

    [submodule "personal"]
            path = personal
            url = git@github.com:newlife/emacs-prelude-personal.git

4.更新personal

    git submodule init
    git submodule update
4.
ms step3也可以用 ***git submodule add ***  来实现。



conclusion
----
上面这写是为了更好的定制化，毕竟各花入各眼，prelude只是提供了一个基本的功能组合。

note
-----
*不建议更新*

不得不说，这个作者是在是太勤劳了，保持了非常高的更新率。
由于作者一个很霸气的决定，不建议使用方向键而是使用ctrl+（nbpf）来操作，为此还特意开发了一个mode（这个mode默认是开启的，=。=）。当然作者还是很人性化啊，给提供了关闭这个mode的接口。
但是，这个勤劳的作者的接口一直变化啊，

所以，没事别更新，当然，如果你对这个很熟悉的话，也是可以的，，
