# -*- coding: utf8 -*-
import random

class Game:
	ON = True
	
	def init():
		Laby.rct_wall()
		Laby.plc_item("Aiguille")
		Laby.plc_item("Tube")
		Laby.plc_item("Ether")
	
	@classmethod
	def over(cls):
		cls.ON = False
	
	def show():
		for i in range(Laby.LAT_MAX+1):
			for j in range(Laby.LON_MAX+1):
				print(Game.show_case(Position(i,j)), end='')
			print('')
		for i in Laby.ITEMS:
			print(i.name, " :(", 'X' if i.loot else '_', ") ", end='')
		print('')
	
	def show_case(position):
		item = Item('case', position)
		if item in Laby.WALLS:
			case = 'X'
		elif item.pos == Gardien.POS:
			case = 'G'
		elif item.pos == McGyver.POS:
			case = 'M'
		elif item in Laby.ITEMS:
			case = Item.show_item(position)		
		else:
			case = ' '
		return case
	
	def new_case(position):
		item = Item("new_case",position)
		if item in Laby.WALLS or position.lat not in range(15) or position.lon not in range(15):
			print("Désolé, vous ne pouvez pas allez par là.")
			McGyver.move()
		elif position == McGyver.POS:
			print("Désolé, je n'ai pas compris.")
			McGyver.move()
		else:
			McGyver.POS = position
			if item in Laby.ITEMS:
				Item.loot_item(position)
			elif position == Gardien.POS:
				Game.over()

	
	def result():
		McGyver.craft_seringue()
		if McGyver.SERINGUE:
			print("Bravo! Vous vous êtes échappé du labyrinthe!")
		else:
			print("Dommage, vous n'avez pas réussi à neutraliser le gardien")

			
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
	def rct_wall(cls):
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
	def plc_item(cls,name):
		latitude = random.randint(cls.LAT_MIN,cls.LAT_MAX)
		longitude = random.randint(cls.LAT_MIN,cls.LAT_MAX)
		position = Position (latitude, longitude)
		item = Item(name, position)
		if item not in (cls.ITEMS or cls.WALLS ) and item.pos not in (McGyver.POS,Gardien.POS):
			cls.ITEMS.append(item)
		else:
			cls.plc_item(name)
					
class McGyver:
	POS = Position(0, 0)
	SERINGUE = False
	
	@classmethod
	def move(cls):
		direction = input("Dans quel direction voulez vous aller?(z,q,s,d)")
		if direction == 'z':
			newpos = Position(cls.POS.lat-1,cls.POS.lon)	
		elif direction == 'q':
			newpos = Position(cls.POS.lat,cls.POS.lon-1)
		elif direction == 's':
			newpos = Position(cls.POS.lat+1,cls.POS.lon)
		elif direction == 'd':
			newpos = Position(cls.POS.lat,cls.POS.lon+1)
		else:
			newpos = cls.POS
		Game.new_case(newpos)
		
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
		
	def show_item(position):
		for i in Laby.ITEMS:
			if i.pos == position and i.loot == False:
				return i.name[0]
		return ' '
				
	def loot_item(position):
		for i in Laby.ITEMS:
			if i.pos == position and i.loot == False:
				i.loot = True
				print("Bravo! Vous avez reçu l'objet suivant: ", i.name, "!")
				break
						
class Wall:
	def __init__(self, position):
		self.pos = position
	def __eq__(self, other):
		return (self.pos == other.pos)

def main():
	Game.init()
	Game.show()
	while Game.ON:
		McGyver.move()
		Game.show()
	Game.result()
	
main()