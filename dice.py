import os
import pygame
import random
path = os.getcwd()
class Randomizer:
    def __init__(self,x,y) -> None:
        self.options =[]
        self.x = x
        self.y = y 
    def make_options(self):
        for ind in range(1,7):
            self.options.append(Dice(ind,self.x,self.y,200,200))
    def chose(self):
        
        return random.choice(self.options)
    

class Dice:
    def __init__(self,number,x,y,width,height) -> None:
        self.number = number 
        self.die = pygame.image.load(os.path.join(path,"Sprites","dices",f"die{self.number}.png"))
        self.die = pygame.transform.scale(self.die,(width,height))
        self.x = x
        self.y = y 
    def draw(self,window):
        window.blit(self.die,(self.x,self.y))
    
    def get_val(self):
        return self.number 