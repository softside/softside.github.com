import json
import os,sys

data = {"data":
        [
            {"post_list":["prelude.md","ddd.txt"],"name":"emacs"},
            {"post_list":["hello.md"],"name":"javascript"}
        ]
    }
json_file = open("tag.json",'w')
json.dump(data,json_file,sort_keys=True,indent=4)

def add_tag(file_name,tag_name):
    json_file = open("tag.json")
    print json_file
    tag_list = json.load(json_file)
    print tag_list
add_tag(1,2)
