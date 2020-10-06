try:
 import importlib

 moduleName = input('Enter module name: ')
 importlib.import_module(moduleName)
except:
  print("Bruh that's wrong")