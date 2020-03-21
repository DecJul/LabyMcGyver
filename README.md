# LabyMcGyver
Projet 3

/!\ Be sure to have "Python 3" and "Pygame" on your computer for use this program

For User: 
	For play the game lanch "main.py" with Python 3.
	Follow the instruction on the first screen.
	You can quit the game anytime with a simple clic on the red cross.


For Developper:

	Repository tree:

		main.py
		.Module/
			constant.py
			object.py
			game_mechanism.py
			graphism.py
		.Data/
			Map.txt
			<Image_file>


	main.py: Main program, the user will launch the game with this file.


	constante.py: File with all constants of the game including:
		-the size of the labyrinthe
		-the resolution of each cases
		-the name of all image used
	If you want add a new image don't forget to add you file in data 
	and name yours variable like this: "Data/<file_name>" (don't forget the extention)

	/!\ Don't name a new constant "ON", "RULE", "PLAY", "END" or "WINDOW".
	They are already used in game_mechanism.py and graphism.py


	object.py: Class with all class used in the game like the labyrinthe or the positions.


	game_mechanism.py: File with all the functions for game mechanism like the collision system or the move.


	graphism.py: File with all the functions for all graphism using "pygame".


	Map.txt: the Map of the labyrinthe, the program use this file for construct the level. He will see only the wall ('X') and the line break.
		You can change this file as you want, but don't forget, MacGyver is on the upper left corner and the guardian is on the lower rigth corner.
		If you want a taller or bigger map, you need to change the constants. an you will, maybe, have some issues with the interface. 