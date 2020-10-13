from Utilities.Constants import lowerBoxes, upperBoxes

class PointCalculator:
    def __init__(self):
        self.lowerScores = {box:None for box in lowerBoxes}
        self.upperScores = {box:None for box in upperBoxes}

    def calculateBoxScores(self, dices):
        self.lowerScores = {box:0 for box in lowerBoxes}
        self.upperScores = {box:0 for box in upperBoxes}
        
        diceCount = {}
        for i in range(6):
            diceCount[i+1] = 0
        for dice in dices:
            diceCount[dice] += 1
        
        ladder = ""
        for i in range(6):
            self.upperScores[self.int2str(i+1,True)] = diceCount[i+1] * (i+1)
            ladder += str(diceCount[i+1])
        maxLadder = max([len(slabs) for slabs in ladder.split("0")])

        if maxLadder >= 4:
            if maxLadder == 5:
                self.lowerScores["Large Ladder"] = 40
            else:
                self.lowerScores["Small Ladder"] = 30
        
        allDiceSum = sum(dices)
        self.lowerScores["Chance"] = allDiceSum
            
        if 5 in diceCount.values():
            self.lowerScores["Yahtzee"] = 50
        if 4 in diceCount.values():
            self.lowerScores["Four of a Kind"] = allDiceSum
        if 3 in diceCount.values():
            self.lowerScores["Three of a Kind"] = allDiceSum
            if 2 in diceCount.values():
                self.lowerScores["Full House"] = 25
    
    @staticmethod
    def int2str(value, plural=False):
        mapper = {
			1: "One",
			2: "Two",
			3: "Three",
			4: "Four",
			5: "Five",
			6: "Six",
		}
        result = mapper.get(value)
        if(plural):
            if(result[-1] in ['s', 'x', 'z']):
                result += "es"
            else:
                result += "s"
        return result
