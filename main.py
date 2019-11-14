#!/usr/bin/env python3
import sys
import time
import chess
import random
import bots
import bot_shell

#List of Bots from the bots folder
botDict = {}

#Pairs the name of each bot with its class in the dict
for bot in bot_shell.UCIBot.__subclasses__():
  botDict[str(bot.__name__)] = bot


#Received messages from host
commandstring = ""

#Bot Selection
if len(sys.argv) > 1:
  if sys.argv[1] in botDict:
    try:
      bot = botDict.get(sys.argv[1])()
    except:
      print("Bot Initialisation Error")
      commandstring = "quit"
  else:
    print("Invalid Bot Name")
    commandstring = "quit"
else:
    print("Must include bot name as command line argument")
    commandstring = "quit"


while commandstring != "quit": #Hub Program Loop
  commandstring = input()
  bot.input(commandstring)
  
  
sys.exit()

