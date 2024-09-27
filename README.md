Please look at his like you would code it looks weird if not.

This code creates a sliding block puzzle game using Pygame. The objective is to move a red "target" block horizontally to the exit on the right side of the grid. Each block can only move in one direction (horizontal or vertical), and they cannot overlap with other blocks. The game progresses through multiple levels with different block arrangements. The user interacts with the blocks by clicking on them and using arrow keys to move them. If the target block reaches the exit, the game moves to the next level. The game is finished when the third level is completed and the user is given a congratulations.

For a more in-depth look: 
  Objective: Move the red "target block" horizontally to the exit (green square) on the far right.
  Setup: The game runs on a 6x6 grid with blocks of various sizes and orientations. Blocks are either horizontal (move left/right) or vertical (move up/down).
  Win Condition: When the target block reaches the exit, the level completes, and the next level loads.
Key Components:
  1. Constants:
    WINDOW_SIZE, GRID_SIZE, and CELL_SIZE define the game window, grid size, and cell dimensions.
    Colors like BACKGROUND_COLOR, BLOCK_COLOR, TARGET_COLOR, and EXIT_COLOR are predefined for different elements (background, blocks, target block, exit).
  2. Block Class:
    Represents each block with properties like position (x, y), size (width, height), color, and orientation (is_horizontal).
    Methods:
      draw(): Draws the block on the screen.
      move(): Handles movement logic based on block orientation (horizontal or vertical). It checks if the new position is valid and doesn't overlap with other     blocks.
  3. Level Creation:
    create_level(level_num) generates different block arrangements for each level.
    Currently, three levels are implemented, with blocks arranged to make the puzzle more challenging in each successive level.
  4. Main Game Loop:
    Initializes Pygame, sets up the game window, and starts with the first level.
    Handles user interactions:
      Mouse Click: Selects a block.
      Arrow Keys: Moves the selected block in the allowed direction (left/right for horizontal, up/down for vertical).
      If the target block reaches the rightmost side, the game progresses to the next level.
  5. Game Mechanics:
    Blocks can't move past the grid's edges or through other blocks.
    The game features a simple win condition: when the target block reaches the exit, the level is completed.
    Potential Expansions: 
      More levels could be added by extending the create_level() function.
      Additional features like a move counter, time tracking, or undo functionality could enhance gameplay.


Midterm questions
• How long (cumulative) have you spent on the code?
  I spent most of my time trying to figure out how to use Renpy, it took me about a week of working with it before I had to change my strategy. Watching videos and looking at workarounds within Renpy took me around 10 hours during a week until I gave up. The rest of the code took me some time as any time I tried to use ChatGPT it would not produce what I wanted. In total, I took around 20 hours, about 3 or 4 a week on average to finish the project.
• What was the most time consuming part?
  It was definitely trying to figure out Renpy, but after that I think I spent most of my time trying to figure out how to get the blocks to move and then get them to move in the right direction. I had blocks at first that were square and not rectangular so anytime I tried to get them to move they wouldn't go anywhere and fixing them caused the rest of the blocks to be unable to move. Limiting the amount of constraints on the blocks was really difficult as I was told during one of my checkpoints to try to shorten my code to make it less complicated.
• In retrospect, how could you have worked more efficiently?
I think limiting the amount of things I wanted to add would have made me much more efficient. I kept trying to include everything that I first envisioned that I was lacking on the base of the code to get it to run. Knowing more about how !!!!!!!
• What libraries/starter code were most useful? To what extent did you need to modify them?
  There was a YouTube video of a different puzzle game that I watched a lot to understand how puzzle games were created. (https://www.youtube.com/watch?v=xpcuAWcEUnM&ab_channel=Tech%26Gaming) Looking at this video helped me create boundaries for my game. It is a very different type of code but the basics of moving blocks in a puzzle really helped me visualize my code better.
