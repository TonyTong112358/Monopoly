import json
new_val = []
with open("everything.json","r") as f:
    x = json.load(f)
    for val in x:
        if val["Rent"] != "0":
            new_val.append(val)
    
print(new_val)


with open("property.json", "w") as f:

    json.dump(new_val,f,indent = 2)