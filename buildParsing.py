""""Parsing the BUILD XML file"""

temp_path = "C/:"

# build_parsing
import os
import xml.etree.ElementTree as ET
import time
t = time.process_time()

# os.system("ping google.com")

class XMLDataObject():
    project_name = ""
    build_dir = ""
    work_dir = ""

    def __init__(self,hello) -> None:
        self.build_dir = hello["build.dir"]


def parse_data ():
    tree = ET.parse('./test_files/build.xml')
    root = tree.getroot()

    my_data = {}
    #print(tree)
    hello = (root.findall("property"))
    for items in hello:
        try: 
            first_value_name = items.attrib["name"]
        except:
            first_value = 0
            print("An exception occurred at: name, ", items.attrib) 
        try: 
            first_value = items.attrib["location"]
        except:
            try: 
                first_value = items.attrib["value"]
            except:
                first_value = 0
                print("An exception occurred at: value, ", items.attrib) 

        my_data[first_value_name] = first_value

    Initinit = XMLDataObject(my_data)
    
    
    print(Initinit.build_dir)
    for valami in my_data:
        print(valami," ------> ", my_data[valami])

    #print (hello[0].text)
    # for h in hello:
    #     print (h.text)

    #print (hello)
    # print(root.attrib)
    # for child in root:
    #     print (root.Element)
    # print (child)

    # for x in root:
    #     #if x.tag == "project":
    #     print(x.tag, x.attrib)


parse_data()

print("Runtime:")
#do some stuff
elapsed_time = time.process_time() - t
print(elapsed_time)