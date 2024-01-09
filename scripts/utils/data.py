#!/usr/bin/env python3

import os
import yaml

def data_dir():
    return os.path.realpath(os.path.dirname(__file__) + "/../../data") + "/"

def read_yaml(file: str) -> dict:
    data = {}
    with open(data_dir() + file) as fp:
        try:
            data = yaml.safe_load(fp)
        except yaml.YAMLError as e:
            print("YAML error in {}: {}".format(file, str(e)))
        except Exception as e:
            print("File read error in {}: {}".format(file, str(e)))
    return data

def add_file_data(data, file):
    new_data = read_yaml(file)
    if 'meta' in new_data:
        if not 'meta' in data:
            data['meta'] = []
        meta = new_data['meta']
        meta['file'] = file
        data['meta'].append(meta)
        new_data.pop('meta')
    data.update(new_data)

def get_data():
    data = {}
    for file in os.listdir(data_dir()):
        if file[-4:] == ".yml":
            add_file_data(data, file)
    return data
