import csv
import json
import os

directory = os.getcwd()
final_dict = []

with open(r"C:\Users\ttong\Documents\Monopoly\data cleansing\data.csv",newline = "") as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    
    # convert this into a lsit of dictionariews of attributews, take this witha  grain of salt cuz i am piss tired (:)
    for property in csv_reader:
        temp_dict = {}
        for title,val in zip(header,property):
            temp_dict[title] = val
        final_dict.append(temp_dict)
        


with open("data cleansing\properties.json","w") as f:
    json.dump(final_dict,f,indent = 4)
    print(final_dict)

# with open 
        
    

