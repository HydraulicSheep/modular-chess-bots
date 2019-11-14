import random
import chess
import bot_shell


class randBot(bot_shell.UCIBot):

  name = "Random Bot"
  author = "Hydraulic Sheep"

  def move(self,commands): 

    if len(self.line)> 0: #Checks if starting player
      self.board.push(chess.Move.from_uci(self.line[-1])) #Updates board after opponent's move

    movelist = list(self.board.legal_moves)
    chosenmove = movelist[random.randint(0,len(movelist))-1]
    self.board.push(chosenmove)
    if chosenmove.drop:
      print("DROP:")
      print(chosenmove.drop)
    print("bestmove", chosenmove)