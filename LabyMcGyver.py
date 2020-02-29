# -*- coding: utf8 -*-
import random
import pygame
from pygame.locals import *

pygame.init()

class Game:
    ON = True
    
    def init():
        Laby.place_wall()
        Graphic.create_laby()
        
    def new_game():
        Laby.place_item("Aiguille")
        Laby.place_item("Tube")
        Laby.place_item("Ether")
        Graphic.item()
        Graphic.show_case(Image.MCGYVER,McGyver.POS)
        Graphic.show_case(Image.GARDIEN,Gardien.POS)

    def event():
        for event in pygame.event.get():
            if event.type == QUIT:
                Game.off()
            if event.type == KEYDOWN:
                if event.key == (K_DOWN or K_S):
                    newpos = Position(McGyver.POS.lat+1,McGyver.POS.lon)
                elif event.key == (K_UP or K_Z):
                    newpos = Position(McGyver.POS.lat-1,McGyver.POS.lon)
                elif event.key == (K_LEFT or K_Q):
                    newpos = Position(McGyver.POS.lat,McGyver.POS.lon-1)
                elif event.key == (K_RIGHT or K_D):
                    newpos = Position(McGyver.POS.lat,McGyver.POS.lon+1)
                else:
                    newpos = McGyver.POS
                Game.new_case(newpos)
      
    def new_case(position):
        item = Item("new_case",position)
        if item in Laby.WALLS or position.lat not in range(15) or position.lon not in range(15):
            pass
        elif position == McGyver.POS:
            pass
        else:
            Graphic.show_case(Image.SOL,McGyver.POS)
            McGyver.POS = position
            Graphic.show_case(Image.SOL,McGyver.POS)
            Graphic.show_case(Image.MCGYVER,McGyver.POS)
            if item in Laby.ITEMS:
                Item.loot_item(position)
    
    def end():
        while Game.ON:
            McGyver.craft_seringue()
            if McGyver.SERINGUE == True:
                Graphic.show_case(Image.WIN,Position(5,1))
            else:
                Graphic.show_case(Image.LOOSE,Position(5,1))
            Graphic.refresh()
            for event in pygame.event.get():
                if event.type == QUIT:
                    Game.off()
                    
    def off():
        Game.ON = False
                                        
class Graphic:
    WIDTH_CASE = 30
    HEIGTH_CASE = 30
    
    @classmethod
    def open(cls):
        cls.WINDOW = pygame.display.set_mode((Graphic.WIDTH_CASE*(Laby.LAT_MAX+1),Graphic.HEIGTH_CASE*(Laby.LON_MAX+1)))
    
    def create_laby():
        for i in range(Laby.LAT_MAX+1):
            for j in range(Laby.LON_MAX+1):
                wall = Wall(Position(j,i))
                if wall in Laby.WALLS:
                    Graphic.show_case(Image.WALL,wall.pos)
                else:
                    Graphic.show_case(Image.SOL,wall.pos)

    def item():
        for i in Laby.ITEMS:
            if i.name == "Aiguille":
                Graphic.show_case(Image.AIGUILLE,i.pos)
            elif i.name == "Tube":
                Graphic.show_case(Image.TUBE,i.pos)
            elif i.name == "Ether":
                Graphic.show_case(Image.ETHER,i.pos)
    
    def show_case(file,position):
        Graphic.WINDOW.blit(file, (position.lon*Graphic.WIDTH_CASE,position.lat*Graphic.HEIGTH_CASE))
        
    def refresh():
        pygame.display.flip()

class Position:
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.lon = longitude
        
    def __eq__(self, other):
        return (self.lat == other.lat) and (self.lon == other.lon)
            
class Laby:

    LAT_MIN = 0
    LON_MIN = 0
    LAT_MAX = 14
    LON_MAX = 14
    WALLS = []
    ITEMS = []

    @classmethod
    def place_wall(cls):
        fichier = open("Map.txt", "r")
        contenu = fichier.read()
        fichier.close()
        map = contenu.split("\n")
        for i in range(cls.LAT_MAX+1):
            for j in range(cls.LON_MAX+1):
                if map[i][j]=='X':
                    position = Position(i,j)
                    wall = Wall(position)
                    cls.WALLS.append(wall)
                    
    @classmethod
    def place_item(cls,name):
        latitude = random.randint(cls.LAT_MIN,cls.LAT_MAX)
        longitude = random.randint(cls.LON_MIN,cls.LON_MAX)
        position = Position (latitude, longitude)
        item = Item(name, position)
        if item not in cls.ITEMS and item not in cls.WALLS and item.pos not in (McGyver.POS,Gardien.POS):
            cls.ITEMS.append(item)
        else:
            cls.place_item(name)

class Image:
    
    @classmethod
    def load (cls):
        cls.SOL = pygame.image.load("sol.jpg").convert()
        cls.WALL = pygame.image.load("wall.jpg").convert()
        cls.MCGYVER = pygame.image.load("McGyver.jpg").convert_alpha()
        cls.GARDIEN = pygame.image.load("Gardien.jpg").convert_alpha()
        cls.ETHER = pygame.image.load("ether.jpg").convert_alpha()
        cls.AIGUILLE = pygame.image.load("aiguille.jpg").convert_alpha()
        cls.TUBE = pygame.image.load("tube.jpg").convert_alpha()
        cls.WIN = pygame.image.load("win.jpg").convert_alpha()
        cls.LOOSE = pygame.image.load("loose.jpg").convert_alpha()
           
class McGyver:
    POS = Position(0, 0)
    SERINGUE = False
        
    @classmethod
    def craft_seringue(cls):
        cls.SERINGUE = True
        for i in Laby.ITEMS:
            if not i.loot:
                cls.SERINGUE = False
                break

class Gardien:
    POS = Position(14,14)
        
class Item:
    def __init__(self, name, position):
        self.pos = position
        self.name = name
        self.loot = False
        
    def __eq__(self, other):
        return (self.pos == other.pos)
                
    def loot_item(position):
        for i in Laby.ITEMS:
            if i.pos == position and i.loot == False:
                i.loot = True
                break
                        
class Wall:
    def __init__(self, position):
        self.pos = position
    def __eq__(self, other):
        return (self.pos == other.pos)

def main():
    Graphic.open()
    Image.load()
    Game.init()    
    Game.new_game()
    while Game.ON:
        Graphic.refresh()
        Game.event()
        if McGyver.POS == Gardien.POS:
            Game.end()


main()