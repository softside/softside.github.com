elisp
====

setq和defvar的区别
---
defvar和setq不同，如果变量在声明之前，这个变量已经有一个值的话，用defvar声明的变量值不会改变该变量的值，就是不发挥作用，不管之前的变量是setq设置的还是defvar设置的。


另一个区别defvar可以为变量提供文档字符创，当变量是在文件中定义的话，C-h v（这个一直不能用）后能给出变量定义的位置

*to be continue*
