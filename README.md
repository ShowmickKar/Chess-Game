# Chess-Game
## So I was experiencing severe muscle ache and fever during the night after taking the first dose of the Moderna vaccine that day. After taking several futile attempts to fall asleep I decided to work on something fun. So there it is! A fully functioning chess game!

It took me approximately two weeks to build the game. Coding up the movement logic for individual pieces was an obvious challenge. However, since it was my first big project which I built entirely from scratch without referring to any tutorial, the BIGGEST CHALLENGE for me was to architect the codebase(which consists of 800+ lines of code) and make everything work together as a whole.

The game is fully functioning with a few exceptions.

First of all, I haven't gotten around to implementing the "Pawn Enpassant" movement yet. I Will do that once I get some free time. Other than that Castling, Checkmate, Stalemate, Pawn Promotion all works just fine. I sort of rushed during the last part where I implemented pawn promotion and casting. That's where the code got quite messy. Besides, I tried to code everything in an extensible, maintainable, and easily debuggable way.

My original plan was to make the game online multiplayer. But since I have little to no experience with sockets and networking I have decided to push back the networking part for a while until I get some free time. 

To run the code on your computer, clone the repository using the terminal command:
<br>
``
git clone https://github.com/ShowmickKar/Chess-Game.git
``

If you don't have Pygame installed on your computer, install it via the terminal command
<br>
``
pip install pygame
``

Here's e demo of the game.

Enjoy!
<br>
<img src="demo01.gif" width="700" />
