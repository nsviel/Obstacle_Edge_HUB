#---------------------------------------------

# State
state_hu = {}
state_py = {}
state_perf = {}
state_kpi = {}
state_pred = {}

# Thread
run_loop = True
run_thread_con = False
run_thread_socket = False
run_thread_perf = False

# Socket
sock_server_l1 = None
sock_server_l2 = None
sock_client = None
sock_client_ok = False

# HTTP
https_server = None
http_server_daemon = None
http_server_ip = "";

# MQTT
mqtt_client  = None
mqtt_msg = 'hello world'

# Tic delay
tic_loop = 1
tic_message = 0.05
tic_connection = 0.5
tic_network = 0.5

# State file
path_config = "config.json"
path_state_hu = "src/state/state_hu.json"
path_state_py = "src/state/state_py.json"
path_state_perf = "src/state/state_perf.json"
path_state_kpi = "src/state/state_kpi.json"
path_state_pred = "src/state/state_pred.json"

# Data dir
path_data_dir =  "../data"
path_image_dir = "../data/image"
path_frame_dir = "../data/frames"
path_predi_dir = "../data/prediction"
path_generic = "src/param/generic/"

# Data file
path_geoloc = "../data/geo.dat"
path_image = "../data/image/image"
