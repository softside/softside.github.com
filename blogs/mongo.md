how to
====
* 如何给现有的数据加一列数据（增加默认值） [this](http://stackoverflow.com/questions/7714216/add-new-field-to-a-collection-in-mongodb)

the code:

    > db.foo.find()
    > db.foo.insert({"test":"a"})
    > db.foo.find()
    { "_id" : ObjectId("4e93037bbf6f1dd3a0a9541a"), "test" : "a" }
    > item = db.foo.findOne()
    { "_id" : ObjectId("4e93037bbf6f1dd3a0a9541a"), "test" : "a" }
    > db.foo.update({"_id" :ObjectId("4e93037bbf6f1dd3a0a9541a") },{$set : {"new_field":1}})
    > db.foo.find()
    { "_id" : ObjectId("4e93037bbf6f1dd3a0a9541a"), "new_field" : 1, "test" : "a" }
这个问题产生于mongose没有类似merge的工具，或者有我不知道？
