import json
new_val = []




#ask if this is a good way to unpack 
with open("property.json","r") as f:
    file = json.load(f)
    x,y = 725,300
    y_val = 300
    current_color = "white"
    for val in file:
        if val["Color"]!= current_color:
            x+=80
            y = y_val
            if x>=1320:
                x = 800
                y+=200
                y_val+=200
            current_color= val["Color"]
        else:
            y+=25
        val["x"] = x
        val["y"] =y

        

        
        
    



with open("property.json", "w") as f:
    print(file)
    json.dump(file,f,indent = 2)