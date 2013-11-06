#/usr/local/bin/python
import json
import os,sys

def add_tag(file_name,tag_name):
    json_file = open("list.json")
    temp_file = json.load(json_file)
    data_list = temp_file.get('data')
    tag_list = temp_file.get('tags')
    json_file.close()

    if tag_name not in tag_list:
        tag_list.append(tag_name)

    for one in data_list:
        if file_name == one.get('name'):
            if tag_name not in one.get('tags'):
                one.get("tags").append(tag_name)

    info_list = {'data':data_list,'tags':tag_list}
    json_file = open("list.json",'w')
    json.dump(info_list, json_file, sort_keys=True, indent=4)
    json_file.close()

def main():
    file_name ,tag_name = sys.argv[1:]
    add_tag(file_name,tag_name)
    print "ok"
if __name__ == "__main__":
    main()
