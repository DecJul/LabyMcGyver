"""Programme pour le Projet3 de la formation dev appli: Python"""
# -*- coding: utf8 -*-
import random
import pygame
from pygame.locals import *



class Game:
    """Class for game's mecanism"""
    ON = True
    RULE = True
    PLAY = False
    END = False

    @staticmethod
    def init():
        """Build the labyrinthe and show the rules"""
        Laby.place_wall()
        Graphic.show_case(Image.RULE, Position(0, 0))

    @classmethod
    def event(cls):
        """collect the user's instructions and separate the phases of the game """
        for event in pygame.event.get():
            if event.type == QUIT:
                cls.off()
            if cls.RULE:
                cls.rule(event)
            elif cls.PLAY:
                McGyver.move(event)
                if McGyver.POS == Gardien.POS:
                    cls.end()
            elif cls.END:
                cls.replay(event)

    @classmethod
    def rule(cls, event):
        """the rule's phase before the beginning of the game"""
        if event.type == KEYDOWN:
            cls.new_game()
            cls.RULE = False

    @classmethod
    def new_game(cls):
        """initialise or reinitialise the game's variables"""
        cls.PLAY = True
        cls.END = False
        Laby.ITEMS = []
        McGyver.new_game()
        Graphic.create_laby()
        Laby.place_item("Aiguille")
        Laby.place_item("Tube")
        Laby.place_item("Ether")
        Graphic.new_item()
        Graphic.show_case(Image.MCGYVER_DOWN, McGyver.POS)
        Graphic.show_case(Image.GARDIEN, Gardien.POS)

    @staticmethod
    def new_case(position, file):
        """Analyse the future's position of the player and decide if he can move on"""
        item = Item("new_case", position)
        if item in Laby.WALLS or position.lat not in range(15) or position.lon not in range(15):
            Graphic.show_case(Image.SOL, McGyver.POS)
            Graphic.show_case(file, McGyver.POS)
        elif position == McGyver.POS:
            pass
        else:
            Graphic.show_case(Image.SOL, McGyver.POS)
            McGyver.POS = position
            Graphic.show_case(Image.SOL, McGyver.POS)
            Graphic.show_case(file, McGyver.POS)
            if item in Laby.ITEMS:
                Item.loot_item(position)

    @classmethod
    def end(cls):
        """when the player reach the guardian, show if he win and activate the end' phase"""
        cls.END = True
        cls.PLAY = False
        if McGyver.SERINGUE:
            Graphic.show_case(Image.WIN, Position(5, 1))
        else:
            Graphic.show_case(Image.LOOSE, Position(5, 1))

    @classmethod
    def replay(cls, event):
        """end phase, the player can play a new game"""
        if event.type == KEYDOWN:
            cls.new_game()

    @classmethod
    def off(cls):
        """use when we want leave the game"""
        cls.ON = False


class Graphic:
    """Class only for the game's graphism"""
    WIDTH_CASE = 48
    HEIGTH_CASE = 48

    @classmethod
    def open(cls):
        """open the windows"""
        width = Graphic.WIDTH_CASE * (Laby.LAT_MAX + 1)
        heigth = Graphic.HEIGTH_CASE * (Laby.LON_MAX + 2)
        cls.WINDOW = pygame.display.set_mode((width, heigth))

    @classmethod
    def create_laby(cls):
        """Build the graphism's part of the labyrinthe after Laby.place_wall"""
        for i in range(Laby.LAT_MAX + 1):
            for j in range(Laby.LON_MAX + 1):
                wall = Wall(Position(j, i))
                if wall in Laby.WALLS:
                    cls.show_case(Image.WALL, wall.pos)
                else:
                    cls.show_case(Image.SOL, wall.pos)
        cls.show_case(Image.INTERFACE, Position(Laby.LON_MAX + 1, 0))

    @classmethod
    def new_item(cls):
        """place all of the items on the map"""
        for i in Laby.ITEMS:
            cls.item(i.name, i.pos)

    @classmethod
    def item(cls, name, pos):
        """place each item with their name"""
        if name == "Aiguille":
            cls.show_case(Image.AIGUILLE, pos)
        elif name == "Tube":
            cls.show_case(Image.TUBE, pos)
        elif name == "Ether":
            cls.show_case(Image.ETHER, pos)

    @classmethod
    def show_case(cls, file, position):
        """show the image with his position"""
        pos_lon = position.lon * Graphic.WIDTH_CASE
        pos_lat = position.lat * Graphic.HEIGTH_CASE
        cls.WINDOW.blit(file, (pos_lon, pos_lat))

    @staticmethod
    def refresh():
        """refresh the graphism after each new turn of the game"""
        pygame.display.flip()


class Position:
    """Manage the position in the map with latitude
    and longitude for every object, wall, player....
    """
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.lon = longitude

    def __eq__(self, other):
        """Allows to compare two different instance of position
        with the sames longitude and latitude
        """
        return (self.lat == other.lat) and (self.lon == other.lon)


class Laby:
    """Stock and manage the position of all objects and walls and the limit of the map"""
    LAT_MIN = 0
    LON_MIN = 0
    LAT_MAX = 14
    LON_MAX = 14
    WALLS = []
    ITEMS = []

    @classmethod
    def place_wall(cls):
        """place the wall in a list with a external file"""
        fichier = open("Map.txt", "r")
        contenu = fichier.read().split("\n")
        fichier.close()
        for i in range(cls. LAT_MAX+1):
            for j in range(cls. LON_MAX+1):
                if contenu[i][j] == 'X':
                    position = Position(i, j)
                    wall = Wall(position)
                    cls.WALLS.append(wall)

    @classmethod
    def place_item(cls, name):
        """place all the item on free position in the labyrinthe"""
        latitude = random.randint(cls.LAT_MIN, cls.LAT_MAX)
        longitude = random.randint(cls.LON_MIN, cls.LON_MAX)
        position = Position(latitude, longitude)
        item = Item(name, position)
        item_in_items = (item in cls.ITEMS)
        item_in_walls = (item in cls.WALLS)
        item_in_char = (item.pos in (McGyver.POS, Gardien.POS))
        if not item_in_items and not item_in_walls and not item_in_char:
            cls.ITEMS.append(item)
        else:
            cls.place_item(name)


class Image:
    """For manage all the images of the game"""
    @classmethod
    def load(cls):
        """load all the image we will use in the game"""
        cls.SOL = pygame.image.load("Ground.png").convert()
        cls.WALL = pygame.image.load("Wall.png").convert()
        cls.MCGYVER_UP = pygame.image.load("MacGyver_Up.png").convert_alpha()
        cls.MCGYVER_DOWN = pygame.image.load("MacGyver_Down.png").convert_alpha()
        cls.MCGYVER_LEFT = pygame.image.load("MacGyver_Left.png").convert_alpha()
        cls.MCGYVER_RIGHT = pygame.image.load("MacGyver_Right.png").convert_alpha()
        cls.GARDIEN = pygame.image.load("Gardien_Down.png").convert_alpha()
        cls.ETHER = pygame.image.load("Ether.png").convert_alpha()
        cls.AIGUILLE = pygame.image.load("Aiguille.png").convert_alpha()
        cls.TUBE = pygame.image.load("Tube.png").convert_alpha()
        cls.WIN = pygame.image.load("win.jpg").convert_alpha()
        cls.LOOSE = pygame.image.load("loose.jpg").convert_alpha()
        cls.RULE = pygame.image.load("rule.jpg").convert_alpha()
        cls.INTERFACE = pygame.image.load("Interface.jpg").convert_alpha()
        cls.SERINGUE = pygame.image.load("Seringue.jpg").convert_alpha()


class McGyver:
    """Character use by the player"""
    @classmethod
    def new_game(cls):
        """initialise the player character for a new game"""
        cls.POS = Position(0, 0)
        cls.SERINGUE = False
        cls.LOOT = 0

    @classmethod
    def craft_seringue(cls):
        """use when all item are loot"""
        cls.SERINGUE = True
        Graphic.show_case(Image.SERINGUE, Position(15, 11))

    @classmethod
    def move(cls, event):
        """play phase, we analyse the move decide by the player"""
        if event.type == KEYDOWN:
            if event.key == K_DOWN or event.key == K_s:
                newpos = Position(cls.POS.lat+1, cls.POS.lon)
                file = Image.MCGYVER_DOWN
                Game.new_case(newpos, file)
            elif event.key == K_UP or event.key == K_w:
                newpos = Position(cls.POS.lat-1, cls.POS.lon)
                file = Image.MCGYVER_UP
                Game.new_case(newpos, file)
            elif event.key == K_LEFT or event.key == K_a:
                newpos = Position(cls.POS.lat, cls.POS.lon-1)
                file = Image.MCGYVER_LEFT
                Game.new_case(newpos, file)
            elif event.key == K_RIGHT or event.key == K_d:
                newpos = Position(cls.POS.lat, cls.POS.lon+1)
                file = Image.MCGYVER_RIGHT
                Game.new_case(newpos, file)


class Gardien:
    """THE BAD GUY"""
    POS = Position(14, 14)


class Item:
    """manage the items loot by the player"""
    def __init__(self, name, position):
        self.pos = position
        self.name = name
        self.loot = False

    def __eq__(self, other):
        """Allows to compare two position of two different instance of items or walls"""
        return self.pos == other.pos

    @staticmethod
    def loot_item(position):
        """Check if an item is loot and if all item are loot"""
        for i in Laby.ITEMS:
            if i.pos == position and not i.loot:
                i.loot = True
                Graphic.item(i.name, Position(15, 1 + (McGyver.LOOT*3)))
                McGyver.LOOT += 1
                if McGyver.LOOT == 3:
                    McGyver.craft_seringue()
                break


class Wall:
    """manage the walls"""
    def __init__(self, position):
        self.pos = position

    def __eq__(self, other):
        """Allows to compare two position of two different instance of items or walls"""
        return self.pos == other.pos


def main():
    """Main fonction: work on two phase:
    First we initialise the game and the graphics
    Second we play the game in a loop (instruction-refresh the windows)"""
    pygame.init()
    Graphic.open()
    Image.load()
    Game.init()
    while Game.ON:
        Graphic.refresh()
        Game.event()

main()