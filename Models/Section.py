from functools import reduce
from Utilities.Constants import lowerBoxes, upperBoxes

class Section:
    def __init__(self):
        self._sectionScore = 0
        self._boxes = {}

    def setScore(self, boxName, score):
        if self._boxes[boxName] != -1:
            return
        self._boxes[boxName] = score

    def getScore(self, boxName):
        return self._boxes[boxName]

    def getScores(self):
        return self._boxes

    def totalScore(self):
        mappedBoxes = map(lambda x: x[1], self._boxes.items())
        filteredBoxes = filter(lambda x: x >= 0, mappedBoxes)
        self._sectionScore = reduce(lambda x, y: x + y, filteredBoxes)
        return self._sectionScore

    def availableBoxes(self):
        return { box: score == -1 for (box,score) in self._boxes.items() }

class UpperSection(Section):
    def __init__(self):
        super().__init__()
        self._boxes = { box: -1 for box in upperBoxes }
	
class LowerSection(Section):
    def __init__(self):
        super().__init__()
        self._boxes = { box: -1 for box in lowerBoxes }