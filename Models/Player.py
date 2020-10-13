from .ScoreCard import ScoreCard
from Utilities.Constants import lowerBoxes, upperBoxes
from Utilities.RandomMethods import randomChoice, get_random_name as randomName
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.scoreCard = ScoreCard()
        self._savedDices = []
        self.throws = 0

    def setScore(self, boxName, score):
        if(boxName in lowerBoxes):
            self.scoreCard.lowerSection.setScore(boxName, score)
        elif (boxName in upperBoxes):
            self.scoreCard.upperSection.setScore(boxName, score)
        else:
            return
    
    def getTotalScore(self):
        return self.scoreCard.totalScore()

    @staticmethod
    def __constructVm(calc, availability, score):
        viewModel = {}
        for (key, available) in availability.items():
            if available:
                viewModel[key] = (calc[key], True)
            else:
                viewModel[key] = (score[key], False)
        return viewModel

    def getScoreCardVm(self, dices):
        self.scoreCard.calculateScores(dices)
        lowerCalc = self.scoreCard.calculatedLowerScores()
        upperCalc = self.scoreCard.calculatedUpperScores()
        lowerAvailable = self.scoreCard.lowerSection.availableBoxes()
        upperAvailable = self.scoreCard.upperSection.availableBoxes()
        lowerScore = self.scoreCard.lowerSection.getScores()
        upperScore = self.scoreCard.upperSection.getScores()
        lowerVm = self.__constructVm(lowerCalc, lowerAvailable, lowerScore)
        upperVm = self.__constructVm(upperCalc, upperAvailable, upperScore)
        return lowerVm, upperVm

    def saveDices(self, dices):
        for dice in dices:
            self._savedDices.append(dice)

    def dumpDices(self):
        dices = self._savedDices
        self._savedDices = []
        return dices

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        print("Hello, my name is", self.name, sep=" ")

    @staticmethod
    def toRollAgain():
        while(True):
            print("Roll again?", HumanPlayer._hmiString(), sep=" ")
            choice = input()
            if(choice in ["Y", "y", "Yes", "yes", "1"]):
                print("I decided to roll again")
                choice = True
                break
            elif(choice in ["N", "n", "No", "no", "0"]):
                print("I decided to select a box")
                choice = False
                break
            else:
                print("Invalid choice, please try again.")
        return choice

    def _hmiString():
        return "\033[1m\033[4mY\033[0mes, \033[1m\033[4mN\033[0mo"

    @staticmethod
    def selectedIndices():
        selected = []
        for i in range(5):
            while(True):
                print("Save dice #", str(i+1) + "?", HumanPlayer._hmiString(), sep=" " )
                choice = input()
                if(choice in ["Y", "y", "Yes", "yes", "1"]):
                    selected.append(i)
                    break
                elif(choice in ["N", "n", "No", "no", "0"]):
                    break
                else:
                    print("Invalid choice, Please try again")
        print("I selected these indices:", selected, sep=" ")
        return selected
    
    @staticmethod
    def selectBox(viewModel):
        boxes = {k:v[0] for k, v in viewModel.items() if v[1]}
        while(True):
            choice = input("Select a box: ")
            if (choice in boxes.keys()):
                break
            else:
                print("Invalid choice! Try Again")
        print("I selected the box", choice, "with score", boxes[choice], sep=" ")
        return (choice, boxes[choice])

    def getScoreCardVm(self, dices):
        lowerVm, upperVm = super().getScoreCardVm(dices)

        return lowerVm, upperVm

class RandomPlayer(Player):
    def __init__(self):
        super().__init__(randomName())
        print("Hello, my name is", self.name, sep=" ")

    @staticmethod
    def toRollAgain():
        choice = randomChoice()
        if(choice): print("I decided to roll again")
        else: print("I decided to select a box")
        return choice

    @staticmethod
    def selectedIndices():
        selected = [i for i in range(5) if randomChoice()]
        print("I selected these indices:", selected, sep=" ")
        return selected
    
    @staticmethod
    def selectBox(viewModel):
        boxes = [(k, v[0]) for k, v in viewModel.items() if v[1]]
        choice = random.choice(boxes)
        print("I selected the box", choice[0], "with score", choice[1], sep=" ")
        return choice

    def getScoreCardVm(self, dices):
        lowerVm, upperVm = super().getScoreCardVm(dices)

        return lowerVm, upperVm