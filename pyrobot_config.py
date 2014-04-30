###############################################################################################################
# Configure Logging:
WORKSPACE = "workspace/"

###############################################################################################################
# Dynamic pybot variables:
# Specifies an 3D-array with variables passed to the single pybot instances
# Each row contains a variablename - value(s) combination (array, name at index 0, values at 1++)
# One variable value will be passed to each python instance using --variable name:value
# If multiple values are defined parabot will iterate over the values and assign one to each pybot
DYN_ARGS =  [
    # specify different users
    ["USER", "Hans", "Klaus", "Peter", "Martin", "Eric"],
    # passwords
    ["PASS", "HansPassword", "KlausPassword", "PetersPassword", "MartinsPassword", "EricsPassword"]
]

time_between_test_start_up = 0


####
# NEW
#
#######

DEFAULT_TOPOLOGY_FOLDER = "/mnt/wt/pyrobot_v1.1/pyrobot/dev/resources/topology/"
DEFAULT_TOPOLOGY = "topology_nightly.py"

SAUCE_USERNAME = 'talliskane'
SAUCE_ACCESSKEY = "6c3ed64b-e065-4df4-b921-75336e2cb9cf"
#DEFAULT_SAUCEURL = "username=%s&access-key=%s&os=%s&browser=%s&browser-version=%s&max-duration=null&idle-timeout=null"
DEFAULT_SAUCEURL = "sauce-ondemand:?username=%s&access-key=%s&os=%s&browser=%s&browser-version=%s&max-duration=null&idle-timeout=null"
DEFAULT_SOLO_BROWSER = 'chrome'
DEFAULT_BROWSER_DISPLAY = ":80"


BROWSER_CAPABILITIES = 'name:%s,platform:%s,version:%s,browserName:%s,javascriptEnabled:True,screen-resolution:1280x1024'

BASE_URL = "http://www.google.ca"

#WORKSPACE_HOME = "/mnt/wt/pyrobot_2/pyrobot/workspace/"
WORKSPACE_HOME = "/mnt/wt/pyrobot_v1.1/pyrobot/workspace/"