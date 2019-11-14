import chess
import random
import time
import chess.pgn

class UCIBot(): #This is a parent class for each bot. It implements the UCI Protocol

    author = "Hydraulic Sheep"
    board = None
    name = "UCI Bot"

    line = ""


    def __init__(self):
        self.commanddict = {
        "uci" : self.startup,
        "ucinewgame" : self.newgame,		
	    "isready" : self.isready,
		"position" : self.position,
		"go" : self.move,
    }


    def startup(self, commands):
        print("id name " + self.name)
        print("id author " + self.author)
        self.newgame(commands)
        print("uciok")

    def isready(self, commands):
        print("readyok")
       

    def newgame(self, commands): 
        self.board = chess.Board()
        self.line = ""

    def position(self, commands):
        if commands[0] == 'startpos':
            commands.pop(0) # remove 'startpos' or 'fen'
        # if not clist:
        if len(commands) != 0: # position startpos
            commands.pop(0) # remove moves
            self.line = commands
        else: # must be fen then
            print("FEN not working yet")  

    def move(self,commands): 

        pass

    def input(self, commandstring):
        commands = commandstring.split(" ")
        cmd = commands.pop(0)
        task = self.commanddict.get(cmd)
        if task:
            task(commands)  


    


