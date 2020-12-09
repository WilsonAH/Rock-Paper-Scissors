from Bot import Bot


class ScissorsBot(Bot):
    def getFirstThrow(self):
        return "Scissors"

    def getNextThrow(self):
        return "Scissors"

    def __str__(self):
        return "ScissorsBot"
