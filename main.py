"""Main programm of the game"""
# -*- coding: utf8 -*-

import module.game_mecanism as Game
import module.graphism as Graphic

def main():
    """Main fonction: work on two phase:
    First we initialise the game and the graphics
    Second we play the game in a loop (instruction-refresh the windows)"""
    Graphic.open_window()
    Game.init()
    while Game.ON:
        Graphic.refresh()
        Game.instruction()

main()
