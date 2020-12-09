from RockBot import RockBot
from ScissorsBot import ScissorsBot
from PaperBot import PaperBot
from BeatLastBot import BeatLastBot
from RockThenPaperThenScissorsBot import RockThenPaperThenScissorsBot
from ScissorsThenPaperThenRockBot import ScissorsThenPaperThenRockBot
from Arena import Arena


if __name__ == '__main__':
    rockBot = RockBot()
    scissorsBot = ScissorsBot()
    paperBot = PaperBot()
    beatLastBot = BeatLastBot()
    rockThenPaperThenScissorsBot = RockThenPaperThenScissorsBot()
    scissorsThenPaperThenRockBot = ScissorsThenPaperThenRockBot()
    arena = Arena()
    arena.battle(beatLastBot, rockThenPaperThenScissorsBot, 20)
    arena.__init__()
    beatLastBot.__init__()
    arena.battle(beatLastBot, scissorsThenPaperThenRockBot, 20)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
