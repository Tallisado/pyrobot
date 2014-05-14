# mandatory: PAYLOAD
# opt: TYPOLOGY
# opt: BASE_URL
# opt: DISPLAY
#help(PyroFactory)

import os
from pyro_factory import pyro_factory as PyroFactory
import pyrobot_config as config

workspace_home = os.path.join(config.WORKSPACE_HOME, os.environ.get("WORKSPACE_UID"))
print workspace_home
pyrofactory = PyroFactory.PyroFactory()
pyrofactory.send_email(workspace_home)


