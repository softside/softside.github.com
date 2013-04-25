开始使用tmux
============================
****
磨刀不误砍柴工，不要担心在工具折腾的时间，收获是大大滴啊  

tmux Productive Mouse-Free Development 

Brian P. Hogan 

ISBN-13: 978-1-934356-96-8

基础操作
----
**tmux的前缀**，因为我们是在tmux是操作consolo的，所以我们需要一个命令来告诉tmux，这是一个tmux命令，默认的前缀是ctrl+b。你可以通过配置文件自己修改，书中建议的是ctrl+a，但是我是emacs用户，这个绑定和emacs去行首的绑定冲突，所以我设置为alt+a

tmux有强大的session管理，创建session：

    tmux new-session -s basic#创建名字为basic的session
    tmux new -s basic#同上
    tmux list-sessions#查看当前所有的session
    tmux ls #同上
    tmux attach#仅有一个session是，连接该session
    tmux attach -t basic#制定session名
    tmux kill-session -t basic#关闭该session


Windows操作
----
这个window操作是很有意思的，和我们平时的tab差不多

    tmux new -s windows -n shell#我们创建了一个叫windows的session并且命名第一个window为shell
在这个window里面，我们

+ **Prefix c**#创建一个新的window
+ **Prefix ,(comma)**# 给当前window改名
+ **Prefix n**和**Prefix p**#在不同的window间切换
+ **Prefix （int)**#在window的index间切换
+ **Prefix f**#输入window名称并切换到该window
+ **Prefix w**#列出所有window，用上下键切换

Panes操作
---
这个才是我们最想要的啊，上面的window操作其实现在的console下也可以方便的进行，只要记忆下快捷键。而panes才是关键啊，虽然可以在emacs下使用ctrl+2/3来实现，但是emacs下的shell是在是有点废柴啊~

+ **Prefix %**#竖直切分当前pane
+ **Prefix "**#水平切分当前pane
+ **Prefix o**#不同pane间切换
+ **Prefix Up/Down/Left/Right**#还是切换
+ **Prefix x**#关闭pane

To be continued
---
tmux貌似还有很多更神奇的用法，以后在慢慢发掘吧~








