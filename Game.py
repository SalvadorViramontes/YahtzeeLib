from Models.Diceware import Dice, DiceArray
from Models.Player import Player
from Utilities.RandomMethods import get_random_name as randomName
from Utilities.Constants import lowerBoxes, upperBoxes

class Game:
    turns = len(lowerBoxes)+len(upperBoxes)
    def __init__(self):
        self.players = []
        self.currentPlayer = None
        self.dices = DiceArray()
        self.gameOver = False
        self.gameTurn = 0

    def newPlayer(self, player):
        self.players.append(player)

    #
    def TurnAction():
        pass

    def NewTurn():
        self.dices.roll()
    #

    def StartGame(self):
        self.currentPlayer = self.players[0]
        self.gameTurn = 0

        for i in range(self.turns):
            for player in self.players:
                print("Turn of", player.name, sep=" ")
                self.dices.roll()
                while player.throws < 3:
                    self.ViewTurnInfo(player)
                    rollAgain = player.toRollAgain()
                    if(rollAgain):
                        savedDices = []
                        selectedIndices = player.selectedIndices()
                        selectedIndices.reverse()
                        for i in selectedIndices:
                            savedDices.append(self.dices.pop(i))
                        savedDices.reverse()
                        player.saveDices(savedDices)
                        self.dices.roll()
                        print("Rolled Dices:", self.dices.faces(), sep=" ")
                        self.dices.addDices(player.dumpDices())
                        player.throws += 1
                    else:
                        break
                player.throws = 0
                vM = self.ViewTurnInfo(player)
                selectedBox = player.selectBox(vM)
                player.setScore(*selectedBox)
                print(" -------------------- ")
        self.EndGame()

    def ViewTurnInfo(self, player):
        print("Dices: ", self.dices.faces(), sep=" ")
        lVm, uVm = player.getScoreCardVm(self.dices.faces())
        vM = dict(lVm, **uVm)
        print(vM)
        return vM

    def EndGame(self):
        playerScores = { player.name: player.getTotalScore() for player in self.players }
        maxScore = max(playerScores.values())
        indexMaxScore = [index for index, element in enumerate(playerScores.values()) if element == maxScore]
        winners = [element for index, element in enumerate(playerScores.keys()) if index in indexMaxScore]

        print("Final Scores:", playerScores, sep=" ")
        if(len(winners) > 1):
            message = "There is a tie between "
            for index, winner in enumerate(winners):
                if index + 1 == len(winners):
                    message += " and "
                elif index == 0: pass
                else: message += ", "
                message += winner
            message += ", with a score of " + str(maxScore)
            print(message)
        else:
            print("The winner is", winners[0] + ",", "with a score of", maxScore, "points", sep=" ")
