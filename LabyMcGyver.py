# -*- coding: utf8 -*-
import random

class Game:
	def __init__(self):
		self.on = True

	def over(self):
		self.on = False
		
		
class Position:
	def __init__(self, latitude, longitude):
		self.lat = latitude
		self.lon = longitude
		
	
class McGyver:
	def __init__(self):
		self.pos = Position(1, 1)
		self.seringue = False
		
	def move(self, direction):
		pass
		
	def craft_seringue(self)
		self.seringue = True
			
			
class Labyrinthe:

	Lat_Min = 1
	Lon_min = 1
	Lat_Max = 15
	Lon_Max = 15
	Walls = []
	Items = []
	
	def recencement_wall(cls)
		open laby.txt
		for i in lines:
			for j in i:
				if j == 'X':
					position = Position(len(i),j)
					wall = Wall(position)
					cls.walls.append(wall)
	
	def recencement_item(cls):
		for i in 2:
			do = True
			while do:
				latitude = random.randint (cls.Lat_Min,cls.Lat_Max)
				longitude = random.randint (cls.Lon_Min,cls.Lon_Max)	
				position = Position (latitude, longitute)
				wall = Wall(position)
					if wall not in cls.walls:
						do = False
			item = Item(name, position)
			cls.items.append(item)
			
			
class Item:
	def __init__(self, name, position):
		self.pos = position
		self.name = name
		self.loot = False
		
	def loot(self):
		self.loot = True

		
class Wall:
	def __init__(self, position):
		self.pos = position

def main():
	game = Game()
	laby = Labyrinthe()
    joueur = McGyver()

main()