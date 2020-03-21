"""Class use in the game"""
# -*- coding: utf8 -*-
import random

from module.constant import *

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
    WALLS = []
    ITEMS = []

    @classmethod
    def place_wall(cls):
        """place the wall in a list with a external file"""
        fichier = open("Data/Map.txt", "r")
        contenu = fichier.read().split("\n")
        fichier.close()
        for i in range(LAT_MAX+1):
            for j in range(LON_MAX+1):
                if contenu[i][j] == 'X':
                    position = Position(i, j)
                    wall = Wall(position)
                    cls.WALLS.append(wall)

    @classmethod
    def place_item(cls, name):
        """place all the item on free position in the labyrinthe"""
        latitude = random.randint(LAT_MIN, LAT_MAX)
        longitude = random.randint(LON_MIN, LON_MAX)
        position = Position(latitude, longitude)
        item = Item(name, position)
        item_in_items = (item in cls.ITEMS)
        item_in_walls = (item in cls.WALLS)
        item_in_char = (item.pos in (McGyver.POS, Gardien.POS))
        if not item_in_items and not item_in_walls and not item_in_char:
            cls.ITEMS.append(item)
        else:
            cls.place_item(name)


class McGyver:
    """Character use by the player"""
    @classmethod
    def new_game(cls):
        """initialise the player character for a new game"""
        cls.POS = Position(0, 0)
        cls.SERINGUE = False
        cls.LOOT = 0



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


class Wall:
    """manage the walls"""
    def __init__(self, position):
        self.pos = position

    def __eq__(self, other):
        """Allows to compare two position of two different instance of items or walls"""
        return self.pos == other.pos
