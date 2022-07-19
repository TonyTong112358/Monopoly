import pygame
class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.open = True
        self.rectangle = pygame.Rect(self.x-2,self.y-2,self.width+4,self.height+4)
    def toggle(self, mode = 1):
        self.open = bool(mode)
    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, self.rectangle,0)
            
        pygame.draw.rect(win, self.color, self.rectangle,0)
        
        if self.text != '':
            font = pygame.font.SysFont('comic sans', 30)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if not self.open:
            return False
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
                
        return False
    
        
h4h




class Entry ():
    def __init__(self,color, x,y,width,height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ""
        self.font = pygame.font.SysFont('comic sans', 30)
        self.focus = False
    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comic sans', 30)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    def type(self,win,text):
        if self.focus == False:
            return 

        if text == "backspace":
            self.text= self.text[0:-1]
            return
        self.text +=text
        
        text = self.font.render(self.text, 1, (0,0,0))
        win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    def get_val(self):
        return self.text

    def isOver(self, pos):
        
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False 


    
    
class Expand:
    def __init__(self, color, x,y,width,height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.text = text
        self.open = True
        self.assets = [] #(button,)
        self.hidden = True
        self.rectangle = pygame.Rect(x,y,width,height)
        self.full = [self.rectangle]
        
    
    
    def draw(self,window):
        if self.hidden:
            self.assets = []
            return 
        self.hidden = self.full
        for x in self.assets:
            x.draw(window,1)
    # def close(self):


            
    def set_assets(self,*args):
        for x in args:
            self.full.append(x)

