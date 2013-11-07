import os, sys
import json
from datetime import datetime

pwd = os.getcwd()
blog_path = pwd+"/blogs/"
blog_date = datetime.now().strftime("%Y/%m/%d")


def insert_blog(new_blog):
    json_file = open("list.json")
    list_info = json.load(json_file)
    blog_list = list_info.get('data')
    tag_list = list_info.get('tags')
    json_file.close()
    blog_list.insert(0,new_blog)
    blog_list = {'data':blog_list,'tags':tag_list}
    json_file = open("list.json",'w')
    json.dump(blog_list, json_file, sort_keys=True, indent=4)
    json_file.close()

def generate_blog(file_name):
    blog_file = blog_path+file_name
    blog_title = open(blog_file).readline()
    new_blog = {'name':file_name,
                'title':blog_title,
                'date':blog_date,
                'tags':[]
                 }
    return new_blog


if __name__ == "__main__":
    json_entry = generate_blog(sys.argv[1]) #
    insert_blog(json_entry)                 #
    print "ok"
