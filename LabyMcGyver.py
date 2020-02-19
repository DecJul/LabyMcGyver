# -*- coding: utf8 -*-
import random
map = ["M        X     "," XXXXXXX   XXX ","    X   XXX  X ","XXX XX XXX   X ","          XX   ","XXX X   XX XXXX","    X X  X     "," XXXX XX X XXXX","      X  X     ","XXXXXXX XXXX XX","  X   X        "," XX X X XX XXX ","    X X X    X "," XXXXXX XXXXXX ","             XG"]
gotTube = '_'
gotAiguille = '_'
gotEther = '_'
j = 0
for i in map:
    map[j] = list(i)
    j = j + 1

def initGame():
    x, y = searchFreeSpace()
    map[x][y] = 'E' 
    x, y = searchFreeSpace()
    map[x][y] = 'T' 
    x, y = searchFreeSpace()
    map[x][y] = 'A' 


def searchFreeSpace():
    k = 'X'
    while k != ' ':
        x = random.randint(0, 14)
        y = random.randint(0, 14)
        k = map[x][y]
    return x,y


def showMap(map):
    for i in map:
        for j in i:
            print(j, end='')
        print('')
    print("Tube=("+gotTube+") Aiguille=("+gotAiguille+") Ether=("+gotEther+").")


def move(x, y,gameOn,win,gotTube,gotAiguille,gotEther):
    direction = input("Dans quel direction voulez vous allez? (z,q,s,d)")
    if direction == 'z' and x != 0 and map[x-1][y] != 'X':
        map[x][y]=' '
        x = x - 1
        item(x,y,gameOn,win,gotTube,gotAiguille,gotEther)
        map[x][y]='M'
    elif direction == 'q' and y != 0 and map[x][y-1] != 'X':
        map[x][y]=' '
        y = y-1
        item(x,y,gameOn,win,gotTube,gotAiguille,gotEther)
        map[x][y]='M'
    elif direction == 's' and x != 14 and map[x+1][y] != 'X':
        map[x][y]=' '
        x=x+1
        item(x,y,gameOn,win,gotTube,gotAiguille,gotEther)
        map[x][y]='M'
    elif direction == 'd' and y != 14 and map[x][y+1] != 'X':
        map[x][y]=' '
        y=y+1
        item(x,y,gameOn,win,gotTube,gotAiguille,gotEther)
        map[x][y]='M'
    else:
        print("Commande non autorisée!")
        x,y=move(x, y,gameOn,win,gotTube,gotAiguille,gotEther)
    return x,y

def item(x,y,gameOn,win,gotTube,gotAiguille,gotEther):
    if map[x][y] == 'E':
        gotEther = 'X'
    elif map[x][y] == 'A':
	    gotAiguille = 'X'
    elif map[x][y] == 'T':
        gotTube = 'X'
    elif x == 14 and y == 14:
        gameOn = False
        if gotEther == 'X' and gotAiguille == 'X' and gotTube == 'X':
            win = True


def main():
    gameOn = True
    win = False
    xMcG, yMcG = 0 , 0
    initGame()
    print("Bienvenue dans McGyver s'échape du labyrinthe infernal!")
    print(" ")
    print("Votre mission: sortir du labyrinthe après avoir neutralisé le garde")
    print("grace à une seringue fabriqué à partir d'un tube d'une aiguille et de l'Ether")
    print("que vous aurez précèdemment récupéré.")
    print("M=votre personnage G=Guardien E=Ether T=Tube A=Aiguille")
    print("Déplacement : z,q,s,d")
    print("Bonne chance!")
    input()
    
    showMap(map)
    while gameOn:
        xMcG, yMcG = move(xMcG, yMcG,gameOn,win,gotTube,gotAiguille,gotEther)
        showMap(map)

    print("Game Over!")
    print(" ")
    if win:
        print("Vous avez Gagnez!")
    else:
        print("Vous avez perdu!")

main()