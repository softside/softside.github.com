import os, sys
import json
from datetime import datetime
pwd = os.getcwd()
blog_path = pwd+"/blogs/"
blog_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


def insert_blog(new_blog):
    json_file = open("list.json",'wr')
    blog_list = json.load(json_file).get('data')
    blog_list.insert(0,new_blog)
    blog_list = {'data':blog_list}
    json_file.write(json.dumps(blog_list))
    json_file.close()
    print blog_list

def generate_blog(file_name):
    blog_file = blog_path+file_name
    blog_title = open(blog_file).readline()
    new_blog = {'name':file_name,
                 'title':blog_title,
                 'disp':"",
                 'date':blog_date
                 }
    return new_blog
file_name = "generate_blog.txt"
new_blog =  generate_blog(file_name)

insert_blog(new_blog)
