import pygame 
from collectable import *
class Player:
    def __init__(self,name,ip,image):
        self.ip = ip
        self.name = name
        self.balance = 2000
        # self.image = [y]
        self.property = {
            
        }
    def recieve(self, val):
        self.balance += val
    def send(self,val):
        assert val < self.balance
        self.balance -= val
        return val
    
class Banker:
    def __init__(self,file) -> None:
        self.file = file
        self.deck = {}
        
    def create_prop(self):
        with open(self.file,"r") as f:
            data = json.load(f)
        
        for x in data:
            
            self.deck[x["Name"]] = (Collectable(x["Name"],x["Color"],x["Price"],x["Rent"],x["PriceBuild"],x["x"],x["y"]))

        

