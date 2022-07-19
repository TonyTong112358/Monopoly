import pygame
from Button_obj import *
import os,sys
import socket
from dice import Randomizer

#configuration
LENGTH,WIDTH = 1400,800
CODE = "utf-8"

directory = os.getcwd()



pygame.init()
window= pygame.display.set_mode((LENGTH,WIDTH))
pygame.display.set_caption("Monopoly")
pygame.key.set_repeat(500,50)
font = pygame.font.SysFont('comic sans', 40)




# socket programming 
PORT = 5555

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(SERVER,PORT)

print(socket.gethostname())



#Color 
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLACK = (0,0,0)
LBLUE = (36, 114, 240)
BLACK = (0,0,0)


#Button creation 
name = Entry(WHITE,400,20,500,100)
ip = Entry(WHITE,400,140,500,100)
submit = Button(WHITE,500,600,100,100,"Submit")
user_text = font.render("IP ADDRESS", 1, WHITE)
ip_text = font.render("USERNAME", 1, WHITE)

#methods 
# def send_message(ip,):


# cc = pygame.image.load(os.path.join(directory,"Sprites","Cards.png"))

def main_menu():
    #implement some some fuckign buttons to submit your shit 
    # implement some text
    #implement netoworking
    #holy shit please order this shit around
    #if possible implement shift keys 
    while True:
        window.fill(BLACK)
        window.blit(ip_text,(100,40))
        window.blit(user_text,(100,160))
        ip.draw(window,True)
        name.draw(window,True)
        submit.draw(window,True)
        pos = pygame.mouse.get_pos()
        # key = pygame.key.get_pressed()
        # press = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                s.close()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                name.type(window,pygame.key.name(event.key))
                ip.type(window,pygame.key.name(event.key))
            #    if name.isOver(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if name.isOver(pos):
                    name.toggle(True)
                    name.color = LBLUE
                elif not name.isOver(pos):
                    name.toggle(False)
                    name.color = WHITE
                if ip.isOver(pos):
                    ip.toggle(True)
                    ip.color = LBLUE
                elif not ip.isOver(pos):
                    ip.toggle(False)
                    ip.color = WHITE
                #button portion

                if submit.isOver(pos):
                    #send the data to hsot
                    # print({name.get_val()},{socket.gethostbyname(socket.gethostname())})
                    s.connect((ip.get_val(),5555))
                    s.send(f"{name.get_val()},{socket.gethostbyname(socket.gethostname())}".encode(CODE))
                    # data = s.recv(1024)
                    return
            # if event
            if event.type == pygame.MOUSEMOTION:
                if submit.isOver(pos):
                    submit.color = RED
                else:
                    submit.color = WHITE
        pygame.display.update()


#object creation for main
board = pygame.image.load(os.path.join(directory,"Sprites","monopoly.jpg"))
board = pygame.transform.scale(board,(800,800))
die_roller = Button(RED,1200,000,200,200,"roll")
die1 = Randomizer(800,0)
die2 = Randomizer(1000,0)
die1.make_options(),die2.make_options()        #making dices here
option1,option2 = die1.chose(),die2.chose()    #setting two default values

pull_out = Expand(RED,800,200,600,800)


money_entry = Entry(RED,1300,200,200,100)

test_button = Button(LBLUE,LENGTH-50, 350,50,100,"open")
pull_out.set_assets(money_entry=money_entry)
# print(pull_out.assets)

def main():
    screen = False
    global option1,option2
    while True:
        
        window.fill(BLACK)
        pygame.draw.line(window,BLACK,(800,200),(1400,200),2)
        die_roller.draw(window,1)
        test_button.draw(window)
        # pull_out.draw(window)
        window.blit(board,(0,0))
        pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEMOTION:
                if die_roller.isOver(pos):
                    die_roller.color = GREEN
                else:
                    die_roller.color = RED
            if event.type == pygame.MOUSEBUTTONDOWN:
                if die_roller.isOver(pos):
                    option1,option2 = die1.chose(),die2.chose()
                    print(option1.get_val(),option2.get_val())
                if test_button.isOver(pos):
                    # screen = True
                    if screen:
                        screen = False
                    else: screen = True
            if event.type == pygame.KEYDOWN:
                



                if pull_out.assets["money_entry"].isOver(pos):
                    pull_out.assets["money_entry"].color = LBLUE
                else:
                    pull_out.assets["money_entry"].color = RED
        option1.draw(window)
        option2.draw(window)
        
        if screen:
            pull_out.draw(window)
        pygame.display.update()

# main_menu()
main()
