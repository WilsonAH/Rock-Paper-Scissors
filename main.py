from RockBot import RockBot
from ScissorsBot import ScissorsBot
from PaperBot import PaperBot
from Arena import Arena


if __name__ == '__main__':
    rockBot = RockBot()
    scissorsBot = ScissorsBot()
    paperBot = PaperBot()
    arena = Arena()
    arena.battle(rockBot, scissorsBot, 5)
    arena.__init__()
    arena.battle(paperBot, paperBot, 5)
    arena.__init__()
    arena.battle(rockBot, scissorsBot, 5)
    arena.__init__()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
