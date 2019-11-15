# modular-chess-bots

This repository implements the Universal Chess Interface protocol (and hopefully xBoard soon) in python.

The aim of this is to allow easy modular access to the protocol by adding your own bot in the bots folder with all the intricacies taken care of.

All bots inherit from the UCIBot class which implements the protocol and handles the communication with the game.

## Installation

Install to a folder in normal fashion with git:

Over HTTPS:
```
git clone https://github.com/HydraulicSheep/modular-chess-bots.git
```
Over SSH:
```
git clone git@github.com:HydraulicSheep/modular-chess-bots.git 
```

## Directions for use

The bots should run as an executable within the relevant directory. Your system may require allowing this (e.g. via chmod+x on a mac).

```
./main.py <botname>

```

The botname is the (case-sensitive) name of the class which is in the bot's file.

There are multiple options for using this package:

You can use cute-chess cli as part of the [cutechess](https://github.com/cutechess/cutechess) library to run bot tournaments via the command line.

Cutechess also provides a GUI which I personally couldn't get working. For me, I found [Scid vs. PC](http://scidvspc.sourceforge.net/) to be a good option but any UCI-compatible chess gui should work.

Of course any other uci interface should work correctly.

## Included Bots

Within this library, some bots have been included by me:

Random Bot: Makes random moves
Capture Bot: Prefers moves which capture pieces (with no consideration of future captures)
King March Bot: Prefers to push its king if possible (does not consider future capability)
Push Bot: Prefers moves which move pieces to the opposite side of the board.

As you can probably tell, these AIs are currently quite simplistic but over time I hope to add some more functionality.

## See Also

This whole project was inspired by the video which certainly is entertaining [30 Weird Chess Algorithms: Elo World](https://www.youtube.com/watch?v=DpXy041BIlA). Feel free to take a look!