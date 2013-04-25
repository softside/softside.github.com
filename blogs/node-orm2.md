#####关于node-orm2的源码的阅读体会

###### 目的

* 最近阅读了两本书，《javascript patterns》和《node.js开发指南》,通过对代码的阅读，验证书中所描述的各个技术点。

* 一年以前的时候我关注nodejs，但是那个时候社区还不是很完善，现在已经有了不小的进步。作为一个后端程序员，其实我一直对orm部分比较感兴趣，所以最近研究了下nodejs的orm框架。入选的有node-orm2,jugglingdb,seqq??,通过对比分析，我选择了这个orm进行学习。

######收获：
目前分析了2个模块，ORM.js和Model.js

* 关于npm的package，require的理解，

* 一直的疑惑，总是感觉js的代码很诡异，尤其是函数的参数，总是感觉这个参数凭空就出来了，js的语法真是，，我还没有说this这个问题，


######node-orm2介绍
* orm依赖数据库的adapter， DML调用DDL，调用pg(另一个npm包)，定义driver对象。

* 