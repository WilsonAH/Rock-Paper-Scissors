from Bot import Bot


class RockThenPaperThenScissorsBot(Bot):
    def __init__(self):
        self.__previousThrow = "Rock"

    def getFirstThrow(self):
        return "Rock"

    def getNextThrow(self):
        # if we won the previous match, using the same throw will win
        if self.__previousThrow == "Rock":
            self.__previousThrow = "Paper"
            return self.__previousThrow
        elif self.__previousThrow == "Paper":
            self.__previousThrow = "Scissors"
            return self.__previousThrow
        elif self.__previousThrow == "Scissors":
            self.__previousThrow = "Rock"
            return self.__previousThrow
        else:
            return "Error"

    def __str__(self):
        return "Rock->Paper->Scissors Bot"
