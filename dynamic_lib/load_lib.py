#lib_path = "/lib/dyn_lib.py"
#mod = __import__(lib_path)
#mod.init("test")
#mod.print_it()


import importlib.util
spec=importlib.util.spec_from_file_location("dynlib","dynamic_lib\lib\dyn_lib.py")

foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
foo.dynlib.init("test text")
foo.print_it()