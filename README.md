# Colored Dots Game

The Colored Dots Game is a fun game written in Python using the pygame library for graphics. 

## Objective
Try to gain as many points as possible!

## Rules
1. The player (represented by a light blue square) can move around the game board one step at a time using the keyboard's left, right, up, and down arrow keys. 
2. Colored dots will randomly appear on the screen at random locations. 
3. The FIND label at the bottom of the game screen tells the player which colored dot to find - this is the treasure color. 
4. The player should use the arrow keys to move to a dot that has the treasure color.
5. When the player is on top of the treasure-colored dot, they gain 1 point for finding the treasure, and the treasure is removed from the board. 
6. The current treasure color is always shown next to the FIND label at the bottom of the screen. This color may change randomly, and the player should always look for this color, and avoid other colors.
7. The current score is always shown next to the SCORE label at the bottom of the screen.
8. The player must NOT step on any dot that is any color besides the treasure color. 
9. If the player steps on any dot whose color is not the treasure color, the game is over.
