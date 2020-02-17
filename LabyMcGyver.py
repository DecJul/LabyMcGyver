# -*- coding: utf8 -*-
def initGame():
    for i de 0 à 14:
        for j de 0 à 14:
            map(i, j)=read('map.txt')............................................
    xItem, yItem = searchFreeSpace()
    map(xItem, yItem) = E //Ether
    xItem, yItem = searchFreeSpace()
    map(xItem, yItem) = T //Tube
    xItem, yItem = searchFreeSpace()
    map(xItem, yItem) = A //Aiguille


def searchFreeSpace():
    k = 'X'
    while k != '_':
        x = random(0-14)
        y = random(0-14)
        k = map(x,y)
    return (x,y)	


def showMap():
    for i de 0 à 14:
        for j de 0 à 14:
            print(map(i,j))
    print("Tube=("+gotTube+") Aiguille=("+gotAiguille+") Ether=("+gotEther+").")


def move():
    print("Dans quel direction voulez vous allez?")
    direction = read()
    if direction == 'z' && yMcG != 0 && map(xMcG, yMcG+1) != 'X':
        map(xMcG, yMcG)='_'
        yMcG++
        item()
        map(xMcG, yMcG)='M'
    elif direction == 'q' && xMcG != 14 && map(xMcG-1, yMcG) != 'X':
        map(xMcG, yMcG)='_'
        xMcG--
        item()
        map(xMcG, yMcG)='M'
    elif direction == 's' && yMcG != 14 && map(xMcG, yMcG-1) != 'X':
        map(xMcG, yMcG)='_'
        yMcG--
        item()
        map(xMcG, yMcG)='M'
    elif direction == 'd' && xMcG != 0 && map(xMcG+1, yMcG) != 'X':
        map(xMcG, yMcG)='_'
        xMcG++
        item()
        map(xMcG, yMcG)='M'
    else:
        print("Commande non autorisée!")


def item():
    if map(xMcG, yMcG) == 'E':
        gotEther = 'X'
    elif map(xMcG, yMcG) == 'A':
	    gotAiguille = 'X'
    elif map(xMcG, yMcG) == 'T':
        gotTube = 'X'
    elif xMcG == 14 && yMcG == 14:
        gameOn = False
        if gotEther == 'X' && gotAiguille == 'X' && gotTube == 'X':
            win = True


def main():
    map = []
    xMcG, yMcG = 0 , 0
    gotTube = '_'
    gotAiguille = '_'
    gotEther = '_'
    gameOn = True
    win = False

    initGame()
    
    print("Bienvenue dans McGyver s'échape du labyrinthe infernal!")
    print(" ")
    print("Votre mission: sortir du labyrinthe après avoir neutralisé le garde")
    print("grace à une seringue fabriqué à partir d'un tube d'une aiguille et de l'Ether")
    print("que vous aurez précèdemment récupéré.")
    print("M=votre personnage G=Guardien E=Ether T=Tube A=Aiguille")
    print("Déplacement : z,q,s,d")
    print("Bonne chance!")
    read()
    
    showMap()
    while gameOn:
        move()
        showMap()

    print("Game Over!")
    print(" ")
    if win:
        print("Vous avez Gagnez!")
    else:
        print("Vous avez perdu!")