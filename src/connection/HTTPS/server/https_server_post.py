#---------------------------------------------
# Possible POST state:
# - /post_state_edge
# - /post_state_ground
# - /post_state_cloud
# - /post_state_network
# - /post_state_control

# Possible POST command:
# - /post_command_operator
#       - false_alarm
#       - reset
# - /post_command_ground
#       - reset
# - /post_command_lidar_1
#       - start
#       - stop
# - /post_command_lidar_2
#       - start
#       - stop
#---------------------------------------------

from src.param import param_edge
from src.connection.HTTPS.client import https_client_post
from src.connection.HTTPS.server import https_server_fct
from src.connection.HTTPS.server import https_server_forward
from src.connection.HTTPS.server import http_command
from src.utils import parser_json
from src.utils import terminal
import json


def manage_post(self):
    command = str(self.path)
    payload = https_server_fct.retrieve_post_data(self)
    if(payload == None):
        return

    # POST state
    if(command == '/post_state_ground'):
        param_edge.state_ground = json.loads(payload)
        https_client_post.post_state_ground("ground", param_edge.state_ground)
    elif(command == '/post_state_edge'):
        param_edge.state_edge = json.loads(payload)
    elif(command == '/post_state_cloud'):
        param_edge.state_cloud = json.loads(payload)
    elif(command == '/post_state_control'):
        param_edge.state_control = json.loads(payload)
    elif(command == '/post_state_network'):
        param_edge.state_network = json.loads(payload)

    # POST command
    elif(command == '/post_command_operator'):
        if(payload == "false_alarm"):
            http_command.command_false_alarm()
        elif(payload == "reset"):
            http_command.command_broker_reset()
    elif(command == '/post_command_ground'):
        if(payload == "reset"):
            https_client_post.post_command("ground", "reset")
    elif(command == '/post_command_lidar_1'):
        if(payload == "start"):
            https_client_post.post_command("lidar_1", "start")
        elif(payload == "stop"):
            https_client_post.post_command("lidar_1", "stop")
    elif(command == '/post_command_lidar_2'):
        if(payload == "start"):
            https_client_post.post_command("lidar_2", "start")
        elif(payload == "stop"):
            https_client_post.post_command("lidar_2", "stop")
    else:
        print("[error] HTTP POST not known [%s]"% command)
