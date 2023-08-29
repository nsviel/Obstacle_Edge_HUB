#---------------------------------------------
from src.param import param_edge
from src.connection.HTTPS.client import https_client_fct
from src.connection.HTTPS.client import https_client_post
from src.connection import connection
from src.utils import terminal


#Test Velodium HTTP connection
def test_slam_con():
    [ip, port, connected] = https_client_fct.network_info("slam")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_slam_con.edge_has_been_deco):
        test_slam_con.edge_has_been_co = True
        test_slam_con.edge_has_been_deco = False
        terminal.addConnection("slam", "on")
        param_edge.state_edge["hub"]["interface"]["slam_http_connected"] = True
    elif(connected == False and test_slam_con.edge_has_been_co):
        test_slam_con.edge_has_been_co = False
        test_slam_con.edge_has_been_deco = True
        terminal.addConnection("slam", "off")
        param_edge.state_edge["hub"]["interface"]["slam_http_connected"] = False

test_slam_con.edge_has_been_co = False
test_slam_con.edge_has_been_deco = True

#Test AI HTTP connection
def test_ai_con():
    [ip, port, connected] = https_client_fct.network_info("ai")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_ai_con.edge_has_been_deco):
        test_ai_con.edge_has_been_co = True
        test_ai_con.edge_has_been_deco = False
        terminal.addConnection("slam", "on")
        param_edge.state_edge["hub"]["interface"]["ai_http_connected"] = True
    elif(connected == False and test_ai_con.edge_has_been_co):
        test_ai_con.edge_has_been_co = False
        test_ai_con.edge_has_been_deco = True
        terminal.addConnection("slam", "off")
        param_edge.state_edge["hub"]["interface"]["ai_http_connected"] = False

test_ai_con.edge_has_been_co = False
test_ai_con.edge_has_been_deco = True

#Test module_capture HTTP connection
def test_capture_con():
    [ip, port, connected] = https_client_fct.network_info("capture")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_capture_con.edge_has_been_deco):
        test_capture_con.edge_has_been_co = True
        test_capture_con.edge_has_been_deco = False
        terminal.addConnection("capture", "on")
        connection_capture_open()
    elif(connected == False and test_capture_con.edge_has_been_co):
        test_capture_con.edge_has_been_co = False
        test_capture_con.edge_has_been_deco = True
        terminal.addConnection("capture", "off")
        connection_capture_close()

test_capture_con.edge_has_been_co = False
test_capture_con.edge_has_been_deco = True

def connection_capture_open():
    param_edge.state_edge["hub"]["interface"]["capture_http_connected"] = True
    https_client_post.post_param_value("capture", "edge", "ip", param_edge.state_edge["hub"]["ip"])

def connection_capture_close():
    param_edge.state_edge["hub"]["interface"]["capture_http_connected"] = False
    param_edge.state_ground["capture"]["socket"]["l1_connected"] = False
    param_edge.state_ground["capture"]["socket"]["l2_connected"] = False

#Test module_capture HTTP connection
def test_ed_con():
    [ip, port, connected] = https_client_fct.network_info("edgenext")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_ed_con.edge_has_been_deco):
        test_ed_con.edge_has_been_co = True
        test_ed_con.edge_has_been_deco = False
        terminal.addConnection("slam", "on")
        connection_ed_open()
    elif(connected == False and test_ed_con.edge_has_been_co):
        test_ed_con.edge_has_been_co = False
        test_ed_con.edge_has_been_deco = True
        terminal.addConnection("slam", "off")
        connection_ed_close()

test_ed_con.edge_has_been_co = False
test_ed_con.edge_has_been_deco = True

def connection_ed_open():
    pass#param_edge.state_edge["edge_next"]["http_connected"] = True

def connection_ed_close():
    pass#param_edge.state_edge["edge_next"]["http_connected"] = False
    pass#param_edge.state_edge["edge_next"]["socket"]["l1_connected"] = False
    pass#param_edge.state_edge["edge_next"]["socket"]["l2_connected"] = False