from Bot import Bot


def getWinningThrow(opponentThrow):
    if opponentThrow == "Rock":
        return "Paper"
    elif opponentThrow == "Paper":
        return "Scissors"
    elif opponentThrow == "Scissors":
        return "Rock"
    else:
        return "Error"


def getLosingThrow(opponentThrow):
    if opponentThrow == "Rock":
        return "Scissors"
    elif opponentThrow == "Paper":
        return "Rock"
    elif opponentThrow == "Scissors":
        return "Paper"
    else:
        return "Error"


class BeatLastBot(Bot):
    def __init__(self):
        self.__previousThrow = "Rock"
        super().__init__()

    def getFirstThrow(self):
        return "Rock"

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
