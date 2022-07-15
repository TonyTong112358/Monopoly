import pygame
import json



class property:
    def __init__(self,name,color):
        pass

#mortgaging is half the buy price
class collectable:
    def __init__(self,name,color,cost,rent,rent_build,house_cost) -> None:
        self.name = name
        self.color = color
        self.cost = cost
        self.rent = rent
        self.rent_build = rent_build
        self.house_cost = house_cost
    

class Board:
    def __init__(self) -> None:
        pass