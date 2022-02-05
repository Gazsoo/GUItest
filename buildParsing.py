# build_parsing
from html.parser import HTMLParser
#from html.entities import name2codepoint
import time

t = time.process_time()

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):

        for attr in attrs:
            if tag == "project" and attr[0] == "name" :
                print(attr[1])
                break


def parse_data ():

    parser = MyHTMLParser()

    with open('./test_files/build.xml') as fileXML:
        feed_file_content = fileXML.read()

        parser.feed(feed_file_content)

    print("ok")

parse_data()

print("Runtime:")
#do some stuff
elapsed_time = time.process_time() - t
print(elapsed_time)