# Data handling
import buildParsing         # Paring Module, custom
import settings_file        # Handle enviroment settings file, custom
import time



t = time.process_time()    

def main():
    # Paring Module TODO the return value and its structure
    yyy = buildParsing.XMLDataObject
    # print (yyy.my_data)
    # print (yyy.my_target)

    settings_dict = settings_file.start_json_settings()
    # print (settings_dict)





if __name__ == "__main__":
    main()

print("Runtime:")
#do some stuff
elapsed_time = time.process_time() - t
print(elapsed_time)
