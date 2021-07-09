from abc import ABC, abstractmethod


# based on the opponents throw, what would win
def getWinningThrow(opponentThrow):
    if opponentThrow == "Rock":
        return "Paper"
    elif opponentThrow == "Paper":
        return "Scissors"
    elif opponentThrow == "Scissors":
        return "Rock"
    else:
        return "Error"


# based on the opponents throw, what would lose
def getLosingThrow(opponentThrow):
    if opponentThrow == "Rock":
        return "Scissors"
    elif opponentThrow == "Paper":
        return "Rock"
    elif opponentThrow == "Scissors":
        return "Paper"
    else:
        return "Error"


# abstract class for all other bots to implement
class Bot(ABC):
    def __init__(self):
        self._previousResult = None

    # What the bot will throw for the first round
    @abstractmethod
    def getFirstThrow(self): pass

    # What the bot will throw after the first round
    @abstractmethod
    def getNextThrow(self): pass

    # What is to be printed based on the bot
    @abstractmethod
    def __str__(self): pass

    # Tell the bot what the result of the previous round was
    def setPreviousResult(self, previousGameStatus):
        self._previousResult = previousGameStatus
