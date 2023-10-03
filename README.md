# Chess-Game
## I was experiencing severe muscle ache and fever during the night after taking the first dose of the Moderna vaccine that day. After taking several futile attempts to fall asleep I decided to work on something fun. So here it is! A fully functioning chess game!

It took me approximately two weeks to build the game. Coding up the movement logic for individual pieces was an obvious challenge. However, since it was my first big project which I built entirely from scratch without referring to any tutorial, the BIGGEST CHALLENGE for me was to architect the codebase(which consists of 800+ lines of code) and make everything work together as a whole.

The game is fully functioning with a few exceptions.

I haven't gotten around to implementing the "Pawn Enpassant" movement yet. I Will do that once I get some free time. Other than that Castling, Checkmate, Stalemate, Pawn Promotion all works just fine. I sort of rushed during the last part where I implemented pawn promotion and casting. That's where the code got quite messy. Besides that, I tried to code everything in an extensible, maintainable, and easily debuggable way.

My original plan was to make the game online multiplayer. But since I have little to no experience with sockets and networking I have decided to push back the networking part for a while until I get some free time. 

### !!! Authors Note (October 2023) !!!: It's been two years since I coded the game. Since then, I've become quite busy with university and my thesis; hence, I could not get a chance to come back to this project and fix the small things that needed to be refined. I probably won't be doing any more updates to this codebase myself unless I get really enthusiastic again. But if any kind soul wants to contribute to this project, feel free to do so. Either create an issue for others to see or fork the repository, make the changes in the code, and make a pull request. I will check and merge them into this repository. I hope you will have fun messing around with the code and probably pick up something useful. Thank you!

## To run the code on your computer 

Clone the repository using the terminal command:
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
