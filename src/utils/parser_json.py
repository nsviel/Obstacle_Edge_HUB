#---------------------------------------------
from src.param import param_edge

import json
import os


def load_state(path):
    try:
        file = open(path, "r")
        data = json.load(file)
        return data
    except:
        dir = os.path.dirname(os.path.abspath(path))
        name = os.path.basename(path)
        generic = dir + "/generic/" + name
        file = open(generic, "r")
        data = json.load(file)
        return data

def load_state_utf8(path):
    try:
        file = open(path, "r")
        data = json.load(file)
        data_encoded = json.dumps(data).encode(encoding='utf_8')
        return data_encoded
    except:
        dir = os.path.dirname(os.path.abspath(path))
        name = os.path.basename(path)
        generic = dir + "/generic/" + name
        file = open(generic, "r")
        data = json.load(file)
        data_encoded = json.dumps(data).encode(encoding='utf_8')
        return data_encoded

def load_data_from_file(path):
    file = open(path, "r")
    data = json.load(file)
    return data

def load_data_from_file_b(path):
    f = open(path)
    data = json.dumps(json.load(f))
    return data

def upload_file(path, data):
    file = open(path, "w")
    json.dump(data, file, indent=4)

def upload_state():
    file = open(param_edge.path_state_edge, "w")
    json.dump(param_edge.state_edge, file, indent=4)

def update_state_file(path, data):
    if(len(data) != 0):
        file = open(path, 'w')
        data_loaded = json.loads(data)
        json.dump(data_loaded, file, indent=4)