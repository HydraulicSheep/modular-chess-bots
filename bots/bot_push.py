import random
import chess
import bot_shell


class pushBot(bot_shell.UCIBot):

    name = "Push Bot"
    author = "Hydraulic Sheep"

    def move(self,commands): 

        if len(self.line)> 0: #Checks if starting player
            self.board.push(chess.Move.from_uci(self.line[-1])) #Updates board after opponent's move

        legallist = list(self.board.legal_moves)
        forward = []
        same = []
        for move in legallist:
            if int(move.to_square/8) > int(move.from_square/8) and self.board.turn:
                forward.append(move)

            elif int(move.to_square/8) == int(move.from_square/8):
                same.append(move)
            elif int(move.to_square/8) < int(move.from_square/8) and not self.board.turn:
                print(move)
                forward.append(move)

        if len(forward)>0:
            chosenmove = forward[random.randint(0,len(forward))-1]
        elif len(same)>0:
            chosenmove = same[random.randint(0,len(same))-1]
        else:
            chosenmove = legallist[random.randint(0,len(legallist))-1]
        self.board.push(chosenmove)
        print("bestmove", chosenmove)
