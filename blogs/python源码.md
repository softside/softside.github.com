阅读笔记
===

Python编译器在对Python进行编译的时候，对于代码中的一个Code Block，会创建一个PyCodeObject对象与这段代码对应，那么如何确定多少代码算式一个Code Block呢？事实上，Python有一个简单而清晰的规则：当进入一个新的名字空间，或者说作用域时，我们就算是进入了一个新的Code Block了。