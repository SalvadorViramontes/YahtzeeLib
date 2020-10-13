from .Section import LowerSection, UpperSection
from Engines.PointCalculator import PointCalculator

class ScoreCard:
	def __init__(self):
		self.lowerSection = LowerSection()
		self.upperSection = UpperSection()
		self._pointCalculator = PointCalculator()
		self._yahtzeeBonus = 0

	def totalScore(self):
		lowerSectionScore = self.lowerSection.totalScore()
		upperSectionScore = self.upperSection.totalScore()
		totalScore = lowerSectionScore + upperSectionScore
		if lowerSectionScore >= 63:
			totalScore += 35
		totalScore += 100 * self._yahtzeeBonus
		return totalScore
	
	def Yahtzee(self):
		if(self.lowerSection.getScore("Yahtzee") == 50):
			self._yahtzeeBonus += 1

	def calculateScores(self, dices):
		self._pointCalculator.calculateBoxScores(dices)

	def calculatedLowerScores(self):
		return self._pointCalculator.lowerScores
	
	def calculatedUpperScores(self):
		return self._pointCalculator.upperScores
		