# coding:utf-8
import json
import os

path = '/Users/vinson/tmp/doc_tree'

def get_join_path(path, item):
    return os.path.join(path, item)


def is_dir(path):
    if os.path.isdir(path):
        return True
    return False

def list_dir(path):
    list = []
    for item in os.listdir(path):
        sub_path = get_join_path(path,item)
        if is_dir(sub_path):
            list.append(read_dirs(sub_path))
        # filter of csv file
        elif os.path.splitext(item)[1].lower() == '.csv':
            list.append({
            'target': 'content',
            'href': sub_path,
            'title': item,
            'type': 'file'
        })
    return list


def read_dirs(path):
    result = {'title': os.path.basename(path), 'folder': 1, 'children': list_dir(path)}
    # result = {'path': path, 'name': os.path.basename(path), 'type': 'directory', 'children': list_dir(path)}
    return result

