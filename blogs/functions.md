####chap6 Functions and Fuctional Programming

When a function defines a parameter with a default value,that parameter and all the parameter that follow are optional.If values are not assigned to all optional parameters in function definition,a SyntaxError exception is raised.
Default parameter values are always set to the objects that were supplied as values when the function was defined.Here's an example:

    a = 10
    def foo(x=a):
        return x
    a=5   #reassign 'a'
    foo() #return 10(default value not changed)   
In addition,the use of mutable objects as default values may lead to unintended behavior:

    def foo(x,items=[]):
        items.append(x)
        return items
    foo(1)
Notice how the default argument retains modifications made from previous invocations.To prevent this ,it is better to use None and add check as follows:

    def foo(x,items=None):
        if items is None:
            items = []
        items.append(x) 
        return items

##Parameter passing and Return values

when a function is invoked,the function parameters are simply names that refers to the passed input objects .The underlying semantics of parameter passing doesn't neatly fit into any single style,such as pass by value or pass by reference, that you might know about from other programming languages.For example,if you pass an immutable value,the argument effectively looks like it was passed by value.However, if a mutable object(such as a list or dictionary) is passed to a function where it's then modified,those changes will be reflected in the original object.Here's an example:

    a = [1,2,3,4,5]
    def square(items):
        for i,x in enumerate(items):
            items[i] = x*x
    square(a) # a changed to [1,4,9,16,25]
Functions that mutate their input values or change the state of other parts of the program behind the scenes like this are said to have side effects.As a general rule,this is a programming style that is best avoided because such functions can become a source of subtle programming errors as programs grow in size and complexity(for example,it's not obvious from reading a fucntion call if a function has side effects).Such fuctions interact poorly with programs involving threads and concurrency because side effects typically need to be protected by locks.

The *return* statement returns a value from a function.If no value is specified or you omit the return statement,the None object is returned.To return multiple values,place the in a tuple:

    def factor(a):
        d =2
        while (d<=(a/2)):
            if ((a/d)*d ==a):
                return ((a/d),d)
        return (a,1)

Mutiple return values returned in a tuple can be assigned to indivdual variables:

    x,y = factor(1234)
    (x,y) = factor(1234)

##Scoping Rules
Each time a function executes ,a new local namespace is created.This namespace represents a local enviroment that contains the names of the function parameter,as well as the names of variables that are assigned inside the function body.When resolving names ,the interpreter first searchs the local namespaces .If no match exists,it searchs the global namespace.The global namespaces for a fuction is always the module in which the function was defined.If the interpreter finds no match in the global namespace,it makes a final check in the built-in space.If this fails ,a NameError exception is raised.
One peculiarity of namespaces is the manipulation of global variables within a function.

Variables in nested function are bound using lexical scoping.That is names are resolved by first checking the local scope and then all enslosing scopes of outer function definitions from the innermost scope
*嵌套函数的作用域：内部函数可以访问外部函数命名空间内的变量，但是不可以修改。该规则同样适用于函数访问模块内的变量*

##functions as Objects and Closures
When the statements that make up a function are packaged together with environment in which they execute,the resulting object is known as a closure。闭包是指：当函数离开创建环境后依然持有其上下文状态




##decorators
A decorators is a function whose primary purpose is to wrap anthoer function or class .The primary purpose of this wrapping is to transparently alter or enhance the behaviorof the object being wrapped. Syntactically,decorators are denoted using the special @ sumbol as follows:

    @trace
    def square(x):
        return x*x

The preceding code is shorthand for the following:

    def square(x):
        return x*x
    square = trace(square)

In the example, a function square() is defined.However,


## Generator and yield
If a function uses the yield keyword,it defines an object known as a generator.A generator is a function that produce a sequence of values for use in iteration.Here's an example:

    def countdown():
        print "Counting down from %d"% n
        while n>0:
            yield n
            n -= 1



## Recursion
Recursion functions are easily defined.For example:

    def factorial(n):
        if n <=1:return 1
        else :return n*factorial(n-1)

However,be aware that there is a limit on the depth of recursive function calls.The function sys.getrecursionlimit() can be userd to change the value.The default value is 1000.Although is possible to increase the value,programs are still limited by the stack size limits enforced by the host operating system.When the recursion depth is exceeded,a RuntimeError exception is raised.Python doesn't perform tail-recursion optimization that you often find in functional languages such as Scheme.
Recursion doesnot work as you might expect in generator functions and coroutines.For example,this code prints all items in a nested collection of lists:

