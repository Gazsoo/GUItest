# Data handling


import types
from matplotlib.pyplot import text
import buildParsingToJSON         # Paring Module, custom
import settings_file        # Handle enviroment settings file, custom
import time
from appdirs import user_data_dir 
import pprint
import json
from collections import OrderedDict

t = time.process_time()  

APPNAME = "PythonXMLBuilder"
APPAUTHOR = "EPTAR"

appdata_path = user_data_dir(APPNAME, APPAUTHOR)
print(appdata_path)

def main():
    XML_file_path = './test_files/build.xml'
    # Paring Module TODO the return value and its structure
    yyy = buildParsingToJSON.XMLDataObject(XML_file_path, appdata_path)
    #jsonData = json.dumps(yyy, indent = 3, sort_keys = True)
    #print ("Key: ",yyy)

    print (yyy.new_dict)

    settings_dict = settings_file.start_json_settings(appdata_path)


    #print (settings_dict)


if __name__ == "__main__":
    main()

print("Runtime:")
#do some stuff
elapsed_time = time.process_time() - t
print(elapsed_time)
