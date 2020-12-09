def evaluateThrows(bot1Throw, bot2Throw):
    if bot1Throw == bot2Throw:
        return "Tie"
    else:
        if bot1Throw == "Rock":
            if bot2Throw == "Scissors":
                return "Bot1"
            else:
                return "Bot2"
        elif bot1Throw == "Paper":
            if bot2Throw == "Scissors":
                return "Bot2"
            else:
                return "Bot1"
        elif bot1Throw == "Scissors":
            if bot2Throw == "Rock":
                return "Bot2"
            else:
                return "Bot1"
    return "Error"


class Arena:
    def __init__(self):
        self.__bot1Wins = 0
        self.__bot2Wins = 0
        self.__gamesPlayed = 0

    def reset(self):
        self.__bot1Wins = 0
        self.__bot2Wins = 0
        self.__gamesPlayed = 0

    def battle(self, bot1, bot2, numberOfRounds):
        print(bot1, "Vs.", bot2)
        bot1Throw = bot1.getFirstThrow()
        bot2Throw = bot2.getFirstThrow()
        self.tallyResult(evaluateThrows(bot1Throw, bot2Throw), bot1, bot2)
        while self.__gamesPlayed < numberOfRounds:
            bot1Throw = bot1.getNextThrow()
            bot2Throw = bot2.getNextThrow()
            self.printThrows(bot1Throw,bot2Throw,bot1,bot2)
            self.tallyResult(evaluateThrows(bot1Throw, bot2Throw), bot1, bot2)
        self.printResults(bot1, bot2)

    def printThrows(self, bot1Throw, bot2Throw, bot1, bot2):
        print(bot1, "-", bot1Throw, " ", bot2, "-", bot2Throw)

    def printResults(self, bot1, bot2):
        print(bot1, "won", self.__bot1Wins, "games")
        print(bot2, "won", self.__bot2Wins, "games")
        print("There were", (self.__gamesPlayed - self.__bot1Wins - self.__bot2Wins), "ties")
        print()

    def tallyResult(self, result, bot1, bot2):
        if result == "Bot1":
            self.__bot1Wins += 1
            bot1.setPreviousResult("Win")
            bot2.setPreviousResult("Lose")
        elif result == "Bot2":
            self.__bot2Wins += 1
            bot1.setPreviousResult("Lose")
            bot2.setPreviousResult("Win")
        else:
            bot1.setPreviousResult("Tie")
            bot2.setPreviousResult("Tie")
        self.__gamesPlayed += 1
