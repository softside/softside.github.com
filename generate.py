import os, sys
import json
from datetime import datetime
pwd = os.getcwd()
blog_path = pwd+"/blogs/"
blog_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


def insert_blog(new_blog):
    json_file = open("list.json")
    blog_list = json.load(json_file).get('data')
    json_file.close()
    print blog_list
    blog_list.insert(0,new_blog)
    print blog_list
    blog_list = {'data':blog_list}
    print blog_list
    json_file = open("list.json",'w')
    #json_file.write(json.dumps(blog_list))
    json.dump(blog_list, json_file, sort_keys=True, indent=4)
    #json.dump(json_file,blog_list)
    json_file.close()

def formate_json():
    json_file = open("list.json")
    blog_list = json.load(json_file)
    json_file.close()
    json_file = open("list.json",'w')
    json.dump(blog_list, json_file, sort_keys=True, indent=4)
    json_file.close()
    return "Y"


def generate_blog(file_name):
    blog_file = blog_path+file_name
    blog_title = open(blog_file).readline()
    new_blog = {'name':file_name,
                 'title':blog_title,
                 'disp':"",
                 'date':blog_date
                 }
    return new_blog


if __name__ == "__main__":
    ###########################################
    # json_entry = generate_blog(sys.argv[1]) #
    # insert_blog(json_entry)                 #
    ###########################################
    formate_json()
