from Bot import Bot


class PaperBot(Bot):
    def getFirstThrow(self):
        return "Paper"

    def getNextThrow(self):
        return "Paper"

    def __str__(self):
        return "PaperBot"
