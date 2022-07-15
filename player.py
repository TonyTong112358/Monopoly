import pygame 
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
    
class 
        

