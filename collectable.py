from ast import Param
import json
from sqlite3 import paramstyle
import pygame
import os
import sys

current = os.getcwd()
print(current)

class Collectable:
    def __init__(self,name,color,cost,rent,house_cost,x,y):
        """
        param rent takes in a list 
        index 0 is base rent with subsequent indexes repreenting incremental cost
        
        hotels and houses cost the same
     
        """
        
        self.x,self.y = x,y
        self.name = name
        self.color = color
        self.cost = int(cost)
        self.rent = rent
        
        self.house_cost = house_cost
        self.mortgage_price = int(cost)/2
        self.image = pygame.image.load(os.path.join(current,"Sprites","Properties",self.color,f"{self.name}.png")).convert()
        self.image = pygame.transform.scale(self.image,(75,150))
    def draw(self,window):
        window.blit(self.image,(self.x,self.y))    
    
        




    


# x = Collections("property.json")
# x.create_all()

# for val in x.deck:
#     print(val.name)