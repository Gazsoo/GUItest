""""Parsing the BUILD XML file"""

# build_parsing
import re
import xml.etree.ElementTree as ET


# os.system("ping google.com")

class XMLDataObject():
    my_data = {}
    my_target = {}
    print ("sheee")

    def __init__(self, xml_path:str) -> None:

        self.tree = ET.parse(xml_path)
        self.xml_root = self.tree.getroot()
        print ("hoo")

        self.my_data["basedir"] = "."                   ### TODO
        self.my_data["ant.project.name"] = "Test00"     ### TODO
        self.my_data.update(self.property_fill(self.xml_root, tag_string="property"))

        self.my_target.update(self.property_fill(self.xml_root, tag_string="target", attrib_value_1="depends"))

        for valami in self.my_data:
            print(valami," ------> ", self.my_data[valami])



        # select the ${...} regex
        replace_all_re = '\$\{.*?\}'
        # select the ... (content) regex
        replace_selection_re = "\$\{(.*?)\}"

        self.replace(replace_all_re , replace_selection_re)

    def replace(self, replace_all_re, replace_selection_re):
        compiled_replace_all_re         = re.compile(replace_all_re)
        compiled_replace_selection_re   = re.compile(replace_selection_re)
        print ("here")
        # Try to replace the regexed values 
        for i_dict in self.my_data:
            replace_dict = compiled_replace_selection_re.findall(self.my_data[i_dict])
            
            for x in  replace_dict:
                try:
                    self.my_data[i_dict] = compiled_replace_all_re.sub(self.my_data[x], \
                    self.my_data[i_dict])
                except: 
                    print ("Warning: ", x, " is not defined")
        #self.my_data = self.property_fill(xml_root, "project")

    # GETing the values of the named objects in the xml_root dict
    def property_fill(self, xml_root, tag_string="property", attrib_name="name", attrib_value_1="location", attrib_value_2="value"):
        dict_to_add = {}
        found_property = (xml_root.findall(tag_string))

        for items in found_property:
            # Get names
            try: 
                first_value_name = items.attrib[attrib_name]
            except:
                first_value = ""
                print(f"An exception occurred at: name, {attrib_name}", items.attrib) 

            # Get vaules
            try: 
                first_value = items.attrib[attrib_value_1]
            except:
                try: 
                    first_value = items.attrib[attrib_value_2]
                except:
                    first_value = ""
                    print(f"An exception occurred at: {attrib_value_1}/{attrib_value_2}, ", items.attrib) 

            dict_to_add[first_value_name] = first_value
        print ("DICK:", dict_to_add)
        return dict_to_add
        

# Make path for directories
def make_path(XML_data):
    pass
    # mycwd = os.getcwd()
    # path = os.path.join(mycwd,XML_data)
    # if os.path.exists :
    #     raise RuntimeError('Directory already exists')
    # else:
    #     try:
    #         os.makedirs(path)
    #     except OSError:
    #         print ("Creation of the directory %s failed" % path)
    #     else:
    #         print ("Successfully created the directory %s " % path)

# def my_parse ():
gaa =XMLDataObject('./test_files/build.xml')
print ("halikhó", XMLDataObject.my_data)
test_XML = XMLDataObject
#print (test_XML.my_data["build.dir"])


