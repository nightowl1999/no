#Relevant Professor:Dr.MasoudKargar
#Programmer:AlirezaAsadzadeh  SN:102962228409
#snakes&ladders game project

from pygame import *
import pygame
import sys
import random
import os

pygame.init()


screen = display.set_mode((600,750))

display.set_caption("Snakes & Ladders by AlirezaAsadzadeh")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

bg = image.load("bg.jpg")
bg = transform.scale(bg,(600,600))

icon = image.load("icon.png")
display.set_icon(icon)


# setting variables
player_blue_x = 20
player_blue_y = 560
player_red_x = 45 
player_red_y = 585
turn = "blue"
dice = 0

player_red_score = 1
player_red_score_list = []

player_blue_score = 1
player_blue_score_list = []


# colors
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
black =(0,0,0)


# making a matrix for the game board
grid = []
for i in range(0,10):
    row = []
    if i % 2 == 0:
        row = list(range(i*10+1,i*10+11))
    else :
        row = list(range(i*10+10,i*10,-1))
    grid.append(row)
grid.reverse()
print(grid)

# locating the pieces on the board
def location(score):
    counter1 = 0
    for list in grid:
        counter1 +=1
        counter2 = 0
        if score in list :
            for m in list:
                counter2+=1
                if m == score :
                    return counter1,counter2


def return_x_y(score):
    row , column = location(score)
    x = (60*column)-60
    y = (60*row)-60
    return x , y

#locations of snakes heads & ladders
Stings = [(99,6),(88,67),(71,29),(55,13),(24,1)]
ladders = [(8,31),(15,97),(42,81),(66,87)]


# Defining functions for Snakes & Ladders
def sting(score):
    is_sting = False
    for i in Stings:
        x,y = i 
        if score == x :
            is_sting = True
            break
    return is_sting


def bitten(score):
    for i in Stings:
        x,y = i
        if score == x :
            return y


def ladder(score):
    is_ladder=False
    for i in ladders:
        x,y = i
        if score == x :
            is_ladder = True
            break
    return is_ladder


def climb(score):
    for i in ladders:
        x,y = i
        if score == x:
            return y

# Movements
def move():
    global turn
    global dice
    if turn == "blue":
        global player_blue_x
        global player_blue_y
        global player_blue_score
        dice =random.randint(1,6)
        if dice + player_blue_score < 100:
            player_blue_score += dice
        elif dice + player_blue_score == 100:
             import bluewins
             quit()
             sys.exit()
        player_blue_x , player_blue_y = return_x_y(player_blue_score)
        display.update()
        if sting(player_blue_score):
            player_blue_score = bitten(player_blue_score)
            player_blue_x , player_blue_y = return_x_y(player_blue_score)
        elif ladder(player_blue_score):
            player_blue_score = climb(player_blue_score)
            player_blue_x , player_blue_y = return_x_y(player_blue_score)
        player_blue_x += 20
        player_blue_y += 20
        player_blue_score_list.append(player_blue_score)
        turn = "red"
    else :
        global player_red_x
        global player_red_y
        global player_red_score
        dice =random.randint(1,6)
        if dice + player_red_score < 100:
            player_red_score += dice
        elif dice + player_red_score == 100:
             import redwins
             quit()
             sys.exit()
        player_red_x , player_red_y = return_x_y(player_red_score)
        display.update()
        if sting(player_red_score):
            player_red_score = bitten(player_red_score)
            player_red_x , player_red_y = return_x_y(player_red_score)
        elif ladder(player_red_score):
            player_red_score = climb(player_red_score)
            player_red_x , player_red_y = return_x_y(player_red_score)
        player_red_x += 40
        player_red_y += 40
        player_red_score_list.append(player_red_score)
        turn = "blue"

# setting up the info on screen
display.update()
while True:
    font_player_name = font.Font("Snake Chan.ttf",25)
    font_player_score = font.Font("Snake Chan.ttf",35)
    font_dice = font.Font("Snake Chan.ttf",45)
    player_blue_name = font_player_name.render("Player blue",True,blue)
    player_red_name = font_player_name.render("Player Red",True,red)
    player_blue_score_display = font_player_score.render(str(player_blue_score),True,black)
    player_red_score_display = font_player_score.render(str(player_red_score),True,black)
    dice_render = font_dice.render(str(dice),True,black)
    dice_counter = font_player_name.render("Dice",True,black)
    screen.fill(white)
    screen.blit(bg,(0,0))
    draw.circle(screen,blue,(player_blue_x,player_blue_y),15)
    draw.circle(screen,red,(player_red_x,player_red_y),15)
    screen.blit(player_blue_name,(5,620))
    screen.blit(player_blue_score_display,(90,685))
    screen.blit(player_red_name,(395,620))
    screen.blit(player_red_score_display,(480,685))
    screen.blit(dice_render,(285,660))
    screen.blit(dice_counter,(270,620))
    
    for e in event.get():
        if e.type == QUIT:
            quit();
            sys.exit()
        if e.type == MOUSEBUTTONDOWN:
            move()
            print(player_blue_score_list)
            print(player_red_score_list)
            
    display.update()
    
