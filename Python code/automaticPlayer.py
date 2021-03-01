import player
import strategy1 
import strategy2
import strategy3
import boardImage

class AutomaticPlayer(player.Player):
	def __init__(self):
		super().__init__()
		self.strategy = None

	def reset(self):
		self.turn = False		#bool
		self.winner = False		#bool
		self.strategy = None

	def defineStrategy(self, aState):
		if aState.getEmpty():
			self.strategy = strategy1.Strategy1()
		else:
			if aState.getEmptyCenter():
				self.strategy = strategy2.Strategy2()
			else:
				self.strategy = strategy3.Strategy3()
	 
	def enable(self, aState):
		self.turn = True
		if self.strategy == None:
			self.defineStrategy(aState)
		aMove = self.strategy.defineMove(aState)
		return aMove