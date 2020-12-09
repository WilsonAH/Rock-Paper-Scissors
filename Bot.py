from abc import ABC, abstractmethod


class Bot(ABC):
    def __init__(self):
        self._previousResult = None

    @abstractmethod
    def getFirstThrow(self): pass

    @abstractmethod
    def getNextThrow(self): pass

    @abstractmethod
    def __str__(self): pass

    def setPreviousResult(self, previousGameStatus):
        self._previousResult = previousGameStatus
