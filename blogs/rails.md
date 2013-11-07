我学rails
###

*对于一个用了多年django的人来说，学rails自然就和django对比。

##创建项目
    rails new app
    django-admin.py startproject app

##生成模块
    rails generate scaffold Product title:string description:text image_url:string price:decimal
要实现这个django就比较麻烦了:
    python manage.py createapp
然后继续写model，实现上面的功能。

## 根据model创建数据可
    rake db:migrate
    python manage.py syncdb
这里要说明的是rails内置的就是migrate的方法，相对django就需要靠south来实现了(django1.7的时候会内置 [migrate](https://docs.djangoproject.com/en/dev/topics/migrations/)的命令),其实我是不太喜欢用south，太繁琐，比如加字段的时候，先在model加字段，然后执行alert语句操作数据库，如果需要后续操作，写脚本run。其中alert语句和脚本放到版本管理里，这样多人参与项目的时候也是可以工作的。

## 运行项目

    rails server#rails s #for short
    python manage.py runserver

这个差别倒不是很大，django这么多年也没写着简化版的runserver命令，这就是差距啊。

## 导入初始数据
    rake db:seed
    python manage.py loaddata sample.json
    ##还有一个rake db:rollback 的命令，还可以在测试model里指定fixtures，支持测试的时候用
## 没有对应的
明显的命令就是这些了，下面看些不那么明显的：

    rails generate controller Store index
这个controller看起来和django中views差不多，
*生成了erb文件，
*生成了一个route，
*生成了test，helper
*生成了js.coffee，css,sass
好吧也没差很多，=。=。其实django的startapp也有生成测试文件的，不过






#关于erb的问题

我是相当的不喜欢erb这个东西，主要还是语法的问题：不好看！！也许是早些年写jsp受伤了，相对而言我还是喜欢django的{{}}式的语法，现在这种语法很流行比如[handlebars](http://handlebarsjs.com/)等等
