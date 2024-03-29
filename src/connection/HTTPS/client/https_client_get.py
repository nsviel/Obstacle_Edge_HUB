#---------------------------------------------
# Possible GET command:
# - /http_ping
# - /capture_state
#---------------------------------------------

from src.param import param_edge
from src.connection.HTTPS.client import https_client_fct
from src.utils import parser_json

import json


def get_state(dest):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/get_state_" + dest
    data = https_client_fct.send_https_get(ip, port, connected, command)
    if(data != None and data != b''):
        try:
            if(dest == "ground"):
                param_edge.state_ground = json.loads(data)
            elif(dest == "network"):
                return json.loads(data)
                #param_edge.state_network = json.loads(data)
        except:
            print("[\033[1;31merror\033[0m] GET \033[1;32m%s\033[0m state failed"% dest)
    return None

def send_command(dest, command):
    [ip, port, connected] = https_client_fct.network_info(dest)
    data = https_client_fct.send_https_get(ip, port, connected, command)
    return data
