# ###############################################################################
# #  Description: Luna game with a simple interactive story
# #  Author: Abdullah Najjar
# #  Date: 4 March, 2020
# #  Version: 0.1
# ###############################################################################

class Player():

    game=None

    #Edit method to remove the AI part
    def __init__(self,scenario,ID,name,AI=False):
        self.__ID=ID
        self.finished_movement=False
        self.name=name
        if AI:
            self.__AI=AI
            self.__AI.init(self)
        else:
            self.__AI=False

    #
    def getAI(self):
        return self.__AI

    #
    def act(self):
        if self.__AI:
            self.__AI.act()

    # Getting the ID of the player
    def getID(self):
        return self.__ID

    # The player collecting the units from the game
    def getUnits(self):
        myunits=[]
        for unit in self.game.getUnits():
            if unit.getOwner()==self:
                myunits.append(unit)

        return myunits
