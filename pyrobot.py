# -*- coding: utf-8 -*-
#
# pip install git+https://github.com/Tallisado/pyrofactory.git#egg=PyroFactory
# pip install git+https://github.com/Tallisado/pyrolibrary.git#egg=PyroLibrary
# /mnt/wt/pyrobot/etc/sc-4.0-linux/bin/sc -u talliskane -k 6c3ed64b-e065-4df4-b921-75336e2cb9cf

import imp
#import PyroFactory
#foo = imp.load_source('pyro_factory', '/mnt/wt/pyrobot_v1.1/pyrofactory/src/pyro_factory/pyro_factory.py')



import inspect, importlib as implib

import types
from pyro_factory import pyro_factory as PyroFactory
import pyrobot_config as config

def imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val.__name__
if __name__ == "__main__":
    mod = implib.import_module( "pyro_factory" )
    for i in inspect.getmembers(mod, inspect.ismodule ):
        print i[0]
        
list(imports())
# mandatory: PAYLOAD
# opt: TYPOLOGY
# opt: BASE_URL
# opt: DISPLAY


# for name, val in globals().items():
    # if isinstance(val, types.ModuleType):
        # yield val.__name__
g = globals().copy()
for name, obj in g.iteritems():
    print "%s %s" % (name, obj)
        
#help(PyroFactory)
#pyrofactory = foo.pyro_factory().run(config)
#pyrofactory = PyroFactory.PyroFactory().run(config)
#pyrofactory = pyro_factory.pyro_factory().run(config)

