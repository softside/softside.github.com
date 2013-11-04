import json
import os,sys

data = {"data":
        [
            {"post_list":["prelude.md","ddd.txt"],"name":"emacs"},
            {"post_list":["hello.md"],"name":"javascript"}
        ]
    }
json_file = open("tag.json",'w')
json.dump(data,json_file,sort_keys=True)
