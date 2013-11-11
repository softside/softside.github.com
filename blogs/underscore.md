underscore
====

javascript是未来啊，前前后后在这个语言上已经投入了许多时间，该是出成果的时候了啊。underscore是一个神奇的框架，类似我们平时写得utils，这对javascript是很重要的啊。

记得最开始的时候我要判断数组里是否有某个值：

    a = []
    >[]
    1 in a
    >false
    a = [1]
    >[1]
    1 in a
    >false
    a = [1,2]
    >[1, 2]
    1 in a
    >true
    a = [1,2,3]
    >[1, 2, 3]
    1 in a
    >true
    2 in a
    >true
    3 in a
    >false
记得当时我就震惊了，现在想想，人家in操作符只是针对object的，用在array上是不行的，虽然不会报错，可是仅限于array.length范围内的几个number。

javascript的发展对underscore的影响
-----
JavaScript这个悲催的语言，在苦苦熬了这么多年以后，终于迎来了自己的春天，随着版本的水涨船高，不断增加新的api，努力使得语言本身更加人性化。underscore为了更高的效率，利用语言内置的新的功能，所以就出现了很多的判断某个函数是否存在的语句。
这些函数大部分都是关于arrayProto的。只有一个关于Object的keys函数，作用类似于python中dict的keys，返回包含的key。该函数是在JavaScript1.8.5中引入的，但是目前我知道的浏览器（还有node）都没有支持这个函数的，node和chrome算是一家的支持javascript1.7，firefox这个不思进取的还在1.5坚持，ie，，谁知道呢，，

#### each

    var each = _.each = _.forEach = function(obj, iterator, context) {
        if (obj == null) return;
        if (nativeForEach && obj.forEach === nativeForEach) {
            obj.forEach(iterator, context);
        } else if (obj.length === +obj.length) {
            for (var i = 0, length = obj.length; i < length; i++) {
                if (iterator.call(context, obj[i], i, obj) === breaker) return;
            }
        } else {
            var keys = _.keys(obj);
            for (var i = 0, length = keys.length; i < length; i++) {
                if (iterator.call(context, obj[keys[i]], keys[i], obj) === breaker) return;
            }
        }
    };

这是each的实现，如果js版本中支持forEach直接用forEach；不支持的话：首先处理array，这个array的判断很有意思,如果obj不是array，那么obj.length是undefined，而+obj.length是NAN。有人说是为了省5个byte，相对(typeof a.length=='number')，[http://stackoverflow.com/questions/9188998/obj-length-obj-length-in-javascript](这里)，还可以更好的压缩。然后是处理Object的部分,这个还是有必要的，对于对象的遍历，因为{}这个对象没有类似forEach的方法。Underscore提供的大部分类似的函数，我们在使用的时候都要提供一个必要的iterator函数，这个函数接受一个参数，表示当前遍历的对象的item，在这个回调函数做我们需要的处理。

#### keys
在each中，处理Object部分的时候，`var keys=_keys(obj)`,作用是返回Object中的key。

    _.keys = nativeKeys || function(obj) {
        if (obj !== Object(obj)) throw new TypeError('Invalid object');
        var keys = [];
        for (var key in obj) if (_.has(obj, key)) keys.push(key);
        return keys;
    };

这个nativeKeys就是前面提到的1.8.5中刚刚引进的method，维护这么个东西也不容易啊，还要看看各位大爷们是不是又实现了什么新的method。

#### map rudece filter
each函数刚写完，map就用了，真是一点都不耽误啊。这个map把处理的结果返回。所以map的回调函数要有明确的返回语句return，不然就是一堆undefined。reduce，就是前一个元素处理的返回值作为参数传递给一个元素的回调函数，听上去有点绕口，好像用处也不大，我就没用过。其实map，reduce，filter在python里面都有，可是ms这些不大建议用，要用强大的list comprehension.好吧，其实，我在python里也没怎么用过，囧
