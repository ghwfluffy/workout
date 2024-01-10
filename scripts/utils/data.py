#!/usr/bin/env python3

import os
import yaml

def data_dir():
    return os.path.realpath(os.path.dirname(__file__) + "/../../data") + "/"

def history_dir():
    return os.path.realpath(os.path.dirname(__file__) + "/../../historical") + "/"

def read_yaml(dir: str, file: str) -> dict:
    data = {}
    with open(dir + file) as fp:
        try:
            data = yaml.safe_load(fp)
        except yaml.YAMLError as e:
            print("YAML error in {}: {}".format(file, str(e)))
        except Exception as e:
            print("File read error in {}: {}".format(file, str(e)))
    return data

def add_file_data(data, file):
    new_data = read_yaml(data_dir(), file)
    if 'meta' in new_data:
        if not 'meta' in data:
            data['meta'] = []
        meta = new_data['meta']
        meta['file'] = file
        data['meta'].append(meta)
        new_data.pop('meta')
    data.update(new_data)

def add_historical_data(data, file):
    date = file.split(".")[0]
    history_data = read_yaml(history_dir(), file)
    if 'metrics' in history_data:
        for item in history_data['metrics']:
            data['metrics'][item] = history_data['metrics'][item]
    if 'workout' in history_data:
        for exercise in history_data['workout']:
            #exercise = history_data['workout'][item]
            exercise['lastComplete'] = date
            found = False
            for i in range(len(data['exercises'])):
                if data['exercises'][i]['name'] == exercise['name']:
                    found = True
                    for key in exercise:
                        data['exercises'][i][key] = exercise[key]
                    break
            if not found:
                print("Unknown exercise {}".format(exercise['name']))
                data['exercises'].append(exercise)

def get_data():
    data = {}
    for file in os.listdir(data_dir()):
        if file[-4:] == ".yml":
            add_file_data(data, file)

    history_files = os.listdir(history_dir())
    history_files.sort()
    for file in history_files:
        if file[-4:] == ".yml":
            add_historical_data(data, file)
    return data
