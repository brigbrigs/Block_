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


New Updates!!
I have added random levels after level 3 however they are sometimes impossible so I am still working on that, I have also started to create more levels that are more complex just in case the random levels don't work out. I know my code also lacks some explanations however, I am changing it in large chunks at a time and it was costing me a lot of time to type out everything so I have a word document that listens to the basics of what all my coed does so I can write it out better for whe I submit my final project. 
