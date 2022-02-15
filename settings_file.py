'''Settings file in appdata'''

import json
import os
SETTINGSFILE = "setting.json"



def append_json_settings():
    pass

def delete_json_settings():
    pass

def save_json_settings():
    pass

def start_json_settings(appdata_path):
    # Sample deffault data to save
    settings_dict = {'employees' : [{'name' : 'John Doe','department' : 'Marketing','place' : 'Remote'},{'name' : 'Jane Doe','department' : 'Software Engineering','place' : 'Remote'},{ 'name' : 'Don Joe','department' : 'Software Engineering','place' : 'Office'}]}

    settings_path = os.path.join(appdata_path, SETTINGSFILE)

    settings_dict = initiate_json_settings(settings_path, settings_dict, appdata_path)

    return settings_dict

# Make settings file
# If exists, read. if not, make one to the appdata and put default in to it.
def initiate_json_settings(settings_path, settings_dict, appdata_path):

    # Check for folder and make if not present
    if os.path.exists(appdata_path) :
        print('Directory already exists')
    else:
        try:
            os.makedirs(appdata_path)
        except OSError:
            print ("Creation of the directory %s failed" % appdata_path)
        else:
            print ("Successfully created the directory %s " % appdata_path)

    if os.path.exists(settings_path) :
    # Read settings
        with open(settings_path, 'r') as out_file:
            settings_dict = json.load(out_file)
    else:
    # Make a save settings file
        with open(settings_path, 'w') as out_file:
            json.dump(settings_dict, out_file, indent=4,ensure_ascii=False)

    return settings_dict
