""""Parsing the BUILD XML file to JSON and to dictionary"""

# build_parsing
import os 
import re
import xmltodict 
import json
from appdirs import user_data_dir 
import pprint

# os.system("ping google.com")

class XMLDataObject():

    my_data = ""
    new_dict = {}

    def __init__(self, XML_file_path, appdata_path):

        # Open and Read file and save to appdata
        self.project_data_handle(XML_file_path, appdata_path)

        # Targeting the Properties and the values to new dict
        self.new_dict["ant.project.name"] = self.my_data["project"]["@name"]
        self.new_dict["basedir"] = self.my_data["project"]["@basedir"]

        target = self.my_data["project"]["property"]
        list_of_val = ["@location", "@value"]
        self.new_dict = self.getEm(target, self.new_dict, list_of_val)


        # self.replace(self.new_dict)

        # select the ${...} regex
        replace_all_re = '\$\{.*?\}'
        # select the ... (content) regex
        replace_selection_re = "\$\{(.*?)\}"

        self.new_dict = self.replace(replace_all_re , replace_selection_re, self.new_dict)

    def project_data_handle(self, XML_file_path, appdata_path):
        with open (os.path.join(appdata_path,"temp.json"), "w") as file:
            with open(XML_file_path) as hallo :
                self.my_data = xmltodict.parse(hallo.read())
                json.dump(self.my_data, file, indent=4)

                project_name = self.my_data["project"]["@name"]
        try:
            os.rename(os.path.join(appdata_path,"temp.json") , os.path.join(appdata_path,f"{project_name}.json"))
        except:
            print(f"allready exists {project_name}.json or could not make it ")

    # The named values set to a different dict
    def getEm(self, dict_from, new_dict, list_of_val):
        for item in dict_from:
            for val in list_of_val:
                if val in item:
                    new_dict[item["@name"]] = item[val]
        return new_dict

    def replace(self, replace_all_re, replace_selection_re, what_to_replace):
        compiled_replace_all_re         = re.compile(replace_all_re)
        compiled_replace_selection_re   = re.compile(replace_selection_re)
        # Try to replace the regexed values 
        for i_dict in what_to_replace:
            replace_dict = compiled_replace_selection_re.findall(what_to_replace[i_dict])
            
            for x in  replace_dict:
                try:
                    what_to_replace[i_dict] = compiled_replace_all_re.sub(what_to_replace[x], \
                    what_to_replace[i_dict])
                except: 
                    print ("Warning: ", x, " is not defined")
        return what_to_replace




