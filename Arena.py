# Determines whether Bot1, Bot2, or Tie from the two throws
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

    # Has the two bots battle for the given number of rounds and prints the results
    def battle(self, bot1, bot2, numberOfRounds):
        # Introductions
        print(bot1, "Vs.", bot2)
        # First round
        bot1Throw = bot1.getFirstThrow()
        bot2Throw = bot2.getFirstThrow()
        self.tallyResultAndTellBots(evaluateThrows(bot1Throw, bot2Throw), bot1, bot2)
        # Each subsequent round
        while self.__gamesPlayed < numberOfRounds:
            bot1Throw = bot1.getNextThrow()
            bot2Throw = bot2.getNextThrow()
            self.printThrows(bot1Throw, bot2Throw, bot1, bot2)
            self.tallyResultAndTellBots(evaluateThrows(bot1Throw, bot2Throw), bot1, bot2)
        self.printResults(bot1, bot2)

    # Helper class to see what each bot threw
    def printThrows(self, bot1Throw, bot2Throw, bot1, bot2):
        print(bot1, "-", bot1Throw, " ", bot2, "-", bot2Throw)

    #For displaying final results
    def printResults(self, bot1, bot2):
        print(bot1, "won", self.__bot1Wins, "games")
        print(bot2, "won", self.__bot2Wins, "games")
        print("There were", (self.__gamesPlayed - self.__bot1Wins - self.__bot2Wins), "ties")
        print()

    #Records the winners, tells the bots, and updates number of games played
    def tallyResultAndTellBots(self, result, bot1, bot2):
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
