from Bot import Bot


class BeatLastBot(Bot):
    def __init__(self):
        self.__previousThrow = "Rock"
        super().__init__()

    # Previous throw is initialized to "Rock" so the first throw will be "Rock"
    def getFirstThrow(self):
        return self.__previousThrow

    # The bot will throw whatever will beat the opponents last throw
    def getNextThrow(self):
        # if we won the previous match, using the same throw will win
        if self._previousResult == "Win":
            return self.__previousThrow
        # if we tied the previous match, we know the opponents throw was our previous throw
        elif self._previousResult == "Tie":
            opponentsThrow = self.__previousThrow
            self.__previousThrow = getWinningThrow(opponentsThrow)
            return self.__previousThrow
        # if we lost the previous match, we know the winning throw against our throw, was the opponents throw
        else:
            opponentsThrow = getWinningThrow(self.__previousThrow)
            self.__previousThrow = getWinningThrow(opponentsThrow)
            return self.__previousThrow

    def __str__(self):
        return "BeatLastBot"
