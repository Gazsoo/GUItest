""""Parsing the BUILD XML file"""

temp_path = "C/:"

# build_parsing
import os
import re
import xml.etree.ElementTree as ET
import time
#import pprint
t = time.process_time()

# os.system("ping google.com")

class XMLDataObject():
    my_data = {}

    def __init__(self,xml_root) -> None:
        self.my_data["basedir"] = "."                   ### TODO
        self.my_data["ant.project.name"] = "Test00"     ### TODO
        self.my_data.update(self.property_fill(xml_root, "property"))
        #self.my_data = self.property_fill(xml_root, "project")

    # GETing the values of the named objects in the xml_root dict
    def property_fill(self, xml_root, tag_string):
        dict_to_add = {}
        found_property = (xml_root.findall(tag_string))

        for items in found_property:
            try: 
                first_value_name = items.attrib["name"]
            except:
                first_value = ""
                print("An exception occurred at: name, ", items.attrib) 
            try: 
                first_value = items.attrib["location"]
            except:
                try: 
                    first_value = items.attrib["value"]
                except:
                    first_value = ""
                    print("An exception occurred at: value, ", items.attrib) 

            dict_to_add[first_value_name] = first_value
        return dict_to_add

# Make path for directories
def make_path(XML_data):
    mycwd = os.getcwd()
    path = os.path.join(mycwd,XML_data)
    if os.path.exists :
        raise RuntimeError('Directory already exists')
    else:
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

def my_parse ():
    tree = ET.parse('./test_files/build.xml')
    root = tree.getroot()

    # my_data = property_fill(root, "property")

    test_XML = XMLDataObject(root)
    print (test_XML.my_data["build.dir"])

    # select the ${...} regex
    replace_all_re = '\$\{.*?\}'
    # select the ... (content) regex
    replace_selection_re = "\$\{(.*?)\}"

    compiled_replace_all_re         = re.compile(replace_all_re)
    compiled_replace_selection_re   = re.compile(replace_selection_re)

    # Try to replace the regexed values 
    for i_dict in test_XML.my_data:
        replace_dict = compiled_replace_selection_re.findall(test_XML.my_data[i_dict])
        
        for x in  replace_dict:
            try:
                test_XML.my_data[i_dict] = compiled_replace_all_re.sub(test_XML.my_data[x], \
                test_XML.my_data[i_dict])
            except: 
                print ("Warning: ", x, " is not defined")

    print(test_XML.my_data["build.dir"])

    for valami in test_XML.my_data:
        print(valami," ------> ", test_XML.my_data[valami])

    # Make direktories
    make_path(test_XML.my_data["bin"])

my_parse()

print("Runtime:")
#do some stuff
elapsed_time = time.process_time() - t
print(elapsed_time)