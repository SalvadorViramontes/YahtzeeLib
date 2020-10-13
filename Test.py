def pruebaDados():
	from Dice import Dice

	myDice = Dice()
	for roll in range(10):
		print(myDice.roll())

def pruebaMapFilterReduce():
	from functools import reduce

	myDict = {
		"Uno": 1,
		"Dos": 2,
		"Tres": 3,
		"Cuatro": 4,
		"Cinco": 5,
		"MenosDiez": -10,
	}

	myDictMapped = map(lambda x: x[1], myDict.items())
	myDictFiltered = filter(lambda x: x >= 0, myDictMapped)
	myDictReduced = reduce(lambda x, y: x + y, myDictFiltered)
	print(myDictReduced)

def pruebaSecciones():
	from Section import UpperSection

	seccion = UpperSection()
	seccion.setScore("Ones", 5)
	seccion.setScore("Fours", 12)
	resultado = seccion.availableBoxes()
	print("Disponibles:", resultado, sep=" ")

def pruebaCalculadorPuntos():
	from PointCalculator import PointCalculator
	from Dice import Dice

	calculator = PointCalculator()
	dices = [Dice().roll() for i in range(5)]
	calculator.calculateBoxScores(dices)
	print("Dices", dices, sep=" ")
	print("UpperSection", calculator.upperScores, sep=" ")
	print("LowerSection", calculator.lowerScores, sep=" ")

def pruebaPuntuacionVm():
	from Player import Player
	from Dice import Dice
	dices = [Dice().roll() for i in range(5)]
	player = Player("Salvador")
	player.setScore("Ones", 6)
	player.setScore("Chance", 21)
	player.setScore("Fours", 16)
	player.setScore("Full House", 25)
	vmLower, vmUpper = player.getScoreCardVm(dices)
	print("Dices: ", dices, sep=" ")
	print("Lower Section: ", vmLower, sep=" ")
	print("Upper Section: ", vmUpper, sep=" ")

def PruebaUtilities():
	from Utilities import get_random_name as randomName
	
	for i in range(10):
		print("Nombre:", randomName())

def PruebaRandomPlayers():
	from Player import RandomPlayer
	from Dice import Dice
	dices = [Dice().roll() for i in range(5)]

	player = RandomPlayer()
	player.setScore("Ones", 6)
	player.setScore("Chance", 21)
	player.setScore("Fours", 16)
	player.setScore("Full House", 25)
	vmLower, vmUpper = player.getScoreCardVm(dices)
	vmExtended = dict(vmLower, **vmUpper)
	print("Dices:", dices, sep=" ")
	print("ExtendedVm:", player.selectBox(vmExtended), sep=" ")

def PruebaJuego():
	from Game import Game
	from Models.Player import RandomPlayer, HumanPlayer
	game = Game()

	game.newPlayer(HumanPlayer("Salvador")) #input
	game.newPlayer(RandomPlayer()) #input

	game.StartGame()

def main():
	#pruebaDados()
	#pruebaMapFilterReduce()
	#pruebaSecciones()
	#pruebaCalculadorPuntos()
	#pruebaPuntuacionVm()
	#PruebaUtilities()
	#PruebaRandomPlayers()
	PruebaJuego()

if __name__ == "__main__":
	main()