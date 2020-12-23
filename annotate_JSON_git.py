import pandas as pd
import numpy as np
import re
import csv
import os

#path = os.getcwd() #check
#print(path) #check

#Read File
list_UUID = list(pd.read_csv("./Documents/Tickets/ky14386/IDs.txt", names=['UUID'])['UUID'])

# Start writing file with the openin bracket
B19_JSON = open("./Documents/Tickets/ky14386/B19.json", "w") 
B19_JSON.writelines("[") 
B19_JSON.close()

# Appending the UUIDs (data shattered for compliance to confidentiality)
for i in list_UUID:
    json_rec = '{"node_id": "' + i + '", "reason": "Duplicate item", "classification": "Notification", "category": "General"}'
    if list_UUID.index(i) < len(list_UUID)-1 :
        json_rec = json_rec + "," #skip comma for the last item
    
    B19_JSON = open("./Documents/Tickets/ky14386/B19.json", "a") #append
    B19_JSON.writelines(json_rec) 
    B19_JSON.close()

# Close bracket
B19_JSON = open("./Documents/Tickets/ky14386/B19.json", "a") #append
B19_JSON.writelines("]") 
B19_JSON.close()