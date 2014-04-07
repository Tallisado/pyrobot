# -*- coding: utf-8 -*-
#
# pip install git+https://github.com/Tallisado/pyrofactory.git#egg=PyroFactory
# pip install git+https://github.com/Tallisado/pyrolibrary.git#egg=PyroLibrary
# pip uninstall git+https://github.com/Tallisado/pyrolibrary.git#egg=PyroLibrary
# /mnt/wt/pyrobot/etc/sc-4.0-linux/bin/sc -u talliskane -k 6c3ed64b-e065-4df4-b921-75336e2cb9cf
#BROWSER='chrome' BASE_URL=http://10.10.9.63 PAYLOAD=/mnt/wt/pyrobot_v1.1/pyrobot/dev/spec/02__pyrobot_library.txt python /mnt/wt/pyrobot_v1.1/pyrobot/pyrobot.py
# pip uninstall git+https://github.com/Tallisado/pyrolibrary.git#egg=pyrolibrary; git commit -am 'updates'; git push; pip ^Cnstall git+https://github.com/Tallisado/pyrolibrary.git#egg=pyrolibrary
# mandatory: PAYLOAD
# opt: TYPOLOGY
# opt: BASE_URL
# opt: DISPLAY
#help(PyroFactory)

from pyro_factory import pyro_factory as PyroFactory
import pyrobot_config as config
pyrofactory = PyroFactory.PyroFactory().run(config)

# import imp
# import inspect, importlib as implib, types
# # print "imports:"
# # def imports():
    # # for name, val in globals().items():
        # # if isinstance(val, types.ModuleType):
            # # yield val.__name__
# # list(imports())
# # print "get members:"
# # if __name__ == "__main__":
    # # mod = implib.import_module( "pyro_library" )
    # # for i in inspect.getmembers(mod, inspect.ismodule ):
        # # print i[0]
        
# print "iterate items:"
# g = globals().copy()
# for name, obj in g.iteritems():
    # print "%s %s" % (name, obj)
    
# #from pyro_library import pyro_library as PyroLibrary
# foo = imp.load_source('PyroLibrary', '/mnt/wt/pyrobot_v1.1/pyrolibrary/src/PyroLibrary/__init__.py')