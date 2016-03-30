#### Become A Better Programmer - How To Read Source Code

Reading soure code has many benefits. You will discover new constructs and libraries, develop empathy for others maintaining your code, and most importantly learn how to structure your code so that it doesn't fall over from internal complexity.
阅读源码有很多好处。你可以发现新的结构和库，，更重要的学习如何组织你的代码，这样代码不会因为内部复杂性而不可控

There is one drawback though, reading source code is darned hard. When I look at a new code base, this sickening feeling washes over me. My mind just doesn't want to dive into this perceived mess.
当热也不容易，阅读源码还是很难的。当我开始阅读一个新的项目的时候，恶心的感觉扑面而来，根本就不想看这一团乱麻

This is (hopefully) a normal response. When our brains sees too much novelty, it just tends to shy away. There is nothing for our amazing biological pattern matching machine to latch onto. The abstractions are all new. It's never seen the class names before. Where does execution even start?
这个是正常的反应，当我们的大脑看到太多新的东西，他就试图避开。||。这个抽象是全新的，从来没有见过这个类名，从哪里开始执行的？

The general tips I can offer are the following: 1. Find and establish an initial base for your mind to latch onto. Usually the main entry point. 2. Start from your base and explore the major features. 3. Take notes on what you've seen.


我们可以提供一般的建议是：1，找到整个程序的入口;2，从入口开始发现主要的特性；3，记录你发现的东西

## Start At The Beginning.
The trick is to give your mind a starting point. Here is what I do. I just run the program with the -h option and invoke the help. Then I copy one of the help strings and do a search over the code base to see where this help text is located. Usually the help invocation is pretty close to where the main entry point to the program is.

技巧就是找到一个起点。我是这样做的，运行程序加 -h 参数看帮助。然后复制帮助的内容到代码里区搜索，看这个在什么地方，一般调用的地方距离程序的入口很近。我都是用which的。

## Identify The Shape Of The Program
Once I've found the main entry point, I run a few toy examples included in the documentation. Then I try to trace the main blocks of code to just get a rough sketch of how the piece fit together.
找到程序的入口后，运行一些文档中得例子，然后跟踪主要模块，看这些模块是如何组织到一起的。

Is there a manager that invokes a ton of helper functions and classes? Are there a bunch of classes that act as peers and hand control off between each other? Is there a main queue of tasks that gets consumed over time?

Getting the big picture helps you slot in the little pieces. You tend to get overwhelmed by the details if you try to forge ahead without understanding the main flow.

## Take Notes
I tend to take notes right in the source code. When writing I use a special comment character (e.g #=> instead of the typical #) so that I can distinguish between my own notes and the original author's comments.
我习惯直接在代码里做笔记，做笔记的适合我使用一些特殊的注释标记这样可以区分自己写的注释和代码原作者的注释。
Make a note on all the clever tricks, confusing flows, beautiful usgae of programming constructs, and anything else you want to remember. If you're stuck, you can also make a note about coming back to that particular section.
在一些小技巧，复杂的流程，漂亮的数据结构的用法或者任何你想记住的地方做标记。如果遇到困难了，也记一下。

By writing down your thoughts, you're really making that piece of source code your own. Over time, the constructs you pick up will start leaking into your own works.
记下你的想法，你才确实掌握那些代码。以后，你学到的这些会渗透到你的代码里。
## Becoming Your Own Person
Learning to program is a continuous process of reading code and writing code. By exposing yourself to a variety of styles, you'll eventually develop a unique perspective and voice.

编程是一个不断的看代码和写代码的过程。扩展自己到不同的领域，你会发展出自己独特的视野和看法。
