""""Parsing the BUILD XML file"""

temp_path = "C/:"

# build_parsing
import xml.etree.ElementTree as ET
import time
t = time.process_time()

class XMLDataObject():
    project_name = ""
    build_dir = ""
    work_dir = ""



def parse_data ():
    tree = ET.parse('./test_files/build.xml')
    root = tree.getroot()
    print("it : ", root.tag)
    print(root.attrib)

    for child in root:
        print(child.tag, child.attrib)

parse_data()

print("Runtime:")
#do some stuff
elapsed_time = time.process_time() - t
print(elapsed_time)