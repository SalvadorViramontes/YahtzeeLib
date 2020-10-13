import random

class Dice:
	def __init__(self):
		self.face = 0
	
	def roll(self):
		self.face = random.randint(1,6)
		return self

class DiceArray:
	def __init__(self):
		self._dices = [Dice() for i in range(5)]

	def roll(self):
		self._dices = [dice.roll() for dice in self._dices]

	def faces(self):
		return [dice.face for dice in self._dices]

	def pop(self, index):
		poppedDice = self._dices.pop(index)
		return poppedDice

	def addDices(self, dices):
		for dice in dices:
			self._dices.append(dice)