import os

cd = os.getcwd()

cd = os.path.join(cd,"Sprites","test_properties")
count = 0
for x in os.listdir(cd):
    cwd = os.path.join(cd,x)
    for y in os.listdir(cwd):
        
        new = y.split("-")[2]
        os.rename(os.path.join(cwd,y),os.path.join(cwd,new))


print(count)