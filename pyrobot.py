# mandatory: PAYLOAD
# opt: TYPOLOGY
# opt: BASE_URL
# opt: DISPLAY
#help(PyroFactory)

from pyro_factory import pyro_factory as PyroFactory
import pyrobot_config as config
pyrofactory = PyroFactory.PyroFactory().run(config)