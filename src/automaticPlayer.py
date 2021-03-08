import player
from strategies import Strategy1, Strategy2, Strategy3


class AutomaticPlayer(player.Player):
    def __init__(self):
        super().__init__()
        self.strategy = None

    def reset(self):
        self.turn = False  # bool
        self.winner = False  # bool
        self.strategy = None

    def defineStrategy(self, aState):
        if aState.getEmpty():
            self.strategy = Strategy1()
        else:
            if aState.getEmptyCenter():
                self.strategy = Strategy2()
            else:
                self.strategy = Strategy3()

    def enable(self, aState):
        self.turn = True
        if self.strategy == None:
            self.defineStrategy(aState)
        aMove = self.strategy.defineMove(aState)
        return aMove
