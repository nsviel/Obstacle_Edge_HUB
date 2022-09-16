#---------------------------------------------
# Possible POST command:
# - /sncf_param
# - /hu_param
# - /py_param
# - /ve_param
# - /ai_param
# - /hu_state
# - /py_state
#---------------------------------------------

from param import param_hu
from HTTP import http_client_post
from HTTP import http_server_fct
from src import parser_json

import json


def manage_post(self):
    command = str(self.path)
    if(command == '/sncf_param'):
        manage_sncf_param(self)
    elif(command == '/hu_param'):
        manage_hu_param(self)
    elif(command == '/py_param'):
        manage_py_param(self)
    elif(command == '/ve_param'):
        manage_ve_param(self)
    elif(command == '/ai_param'):
        manage_ai_param(self)
    elif(command == '/hu_state'):
        manage_hu_state(self)
    elif(command == '/py_state'):
        manage_py_state(self)

def manage_sncf_param(self):
    pass

def manage_hu_param(self):
    payload = http_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = http_server_fct.decipher_json(data)
        param_hu.state_hu[lvl1][lvl2] = lvl3
        if(lvl1 == "sncf"):
            param_hu.state_hu["sncf"]["broker_connected"] = False

def manage_py_param(self):
    payload = http_server_fct.retrieve_post_data(self)
    http_client_post.post_param_payload("py", payload)

def manage_ve_param(self):
    payload = http_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = http_server_fct.decipher_json(data)
        http_server_forward.forward_ve_post(lvl2, lvl3)

def manage_ai_param(self):
    payload = http_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        [lvl1, lvl2, lvl3] = http_server_fct.decipher_json(data)
        http_server_forward.forward_ai_post(lvl2, lvl3)

def manage_hu_state(self):
    payload = http_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        param_hu.state_hu = data
        parser_json.upload_state()
        param_hu.state_hu["sncf"]["broker_connected"] = False

def manage_py_state(self):
    payload = http_server_fct.retrieve_post_data(self)
    if(payload != None):
        data = json.loads(payload)
        http_client_post.post_state("py", data)
