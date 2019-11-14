import random
import chess
import bot_shell




class captureBot(bot_shell.UCIBot):

    name = "Capture Bot"
    author = "Hydraulic Sheep"

    def move(self,commands):

        if len(self.line)> 0: #Checks if starting player
            self.board.push(chess.Move.from_uci(self.line[-1])) #Updates board after opponent's move

        movelist = list(self.board.legal_moves)

        capturemoves = []

        for move in movelist:
            if self.board.piece_at(move.to_square):
                capturemoves.append(move)

        if len(capturemoves)>0:
            chosenmove = capturemoves[random.randint(0,len(capturemoves))-1]
        else:
            chosenmove = movelist[random.randint(0,len(movelist))-1]
        
        self.board.push(chosenmove)
        print("bestmove", chosenmove)