from Bot import Bot


class RockBot(Bot):
    def getFirstThrow(self):
        return "Rock"

    def getNextThrow(self):
        return "Rock"

    def __str__(self):
        return "RockBot"
