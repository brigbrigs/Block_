import pygame
import random
import sys

# Constants
WINDOW_SIZE = 600
GRID_SIZE = 6
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
FPS = 30

# Colors
BACKGROUND_COLOR = (240, 240, 240)
BLOCK_COLOR = (60, 60, 255)
TARGET_COLOR = (255, 60, 60)
LOCKED_COLOR = (100, 100, 100)
EXIT_COLOR = (60, 255, 60)
LINE_COLOR = (0, 0, 0)

# Block class to represent each block in the game
class Block:
    def __init__(self, x, y, width, height, color, is_target=False, is_locked=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.is_target = is_target
        self.is_locked = is_locked
        self.is_horizontal = self.width > self.height

    def draw(self, screen, is_selected=False): #color thickness and highlighting
        pygame.draw.rect(screen, self.color, (self.x * CELL_SIZE, self.y * CELL_SIZE, self.width * CELL_SIZE, self.height * CELL_SIZE))
        if self.is_locked:
            pygame.draw.rect(screen, LOCKED_COLOR, (self.x * CELL_SIZE, self.y * CELL_SIZE, self.width * CELL_SIZE, self.height * CELL_SIZE))
        if is_selected:
            pygame.draw.rect(screen, (255, 255, 0), (self.x * CELL_SIZE, self.y * CELL_SIZE, self.width * CELL_SIZE, self.height * CELL_SIZE), 3)
        else:
            pygame.draw.rect(screen, LINE_COLOR, (self.x * CELL_SIZE, self.y * CELL_SIZE, self.width * CELL_SIZE, self.height * CELL_SIZE), 1)

    def move(self, dx, dy, board): #locks blocks in 1D movement
        if self.is_locked:
            return False
        if self.is_horizontal and dy != 0:
            return False
        if not self.is_horizontal and dx != 0:
            return False

        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < GRID_SIZE - self.width + 1 and 0 <= new_y < GRID_SIZE - self.height + 1: #check to make sure blocks stay locked
            for block in board:
                if block != self:
                    if (new_x < block.x + block.width and new_x + self.width > block.x and
                            new_y < block.y + block.height and new_y + self.height > block.y):
                        return False

            self.x = new_x
            self.y = new_y
            return True

        return False

def create_static_level(level_num):
    if level_num == 1:
        return [
            Block(0, 2, 2, 1, TARGET_COLOR, is_target=True),
            Block(3, 0, 3, 1, BLOCK_COLOR),
            Block(3, 2, 1, 2, BLOCK_COLOR),
            Block(4, 1, 1, 3, BLOCK_COLOR),
        ]
    elif level_num == 2:
        return [
            Block(0, 2, 2, 1, TARGET_COLOR, is_target=True),
            Block(1, 0, 2, 1, BLOCK_COLOR),
            Block(2, 1, 1, 2, BLOCK_COLOR),
            Block(3, 3, 2, 1, BLOCK_COLOR),
            Block(0, 4, 3, 1, BLOCK_COLOR), 
        ]
    elif level_num == 3:
        return [
            Block(0, 2, 2, 1, TARGET_COLOR, is_target=True),
            Block(0, 0, 1, 2, BLOCK_COLOR),
            Block(2, 1, 1, 2, BLOCK_COLOR),
            Block(2, 0, 3, 1, BLOCK_COLOR),
            Block(1, 4, 2, 1, BLOCK_COLOR),
            Block(4, 5, 2, 1, BLOCK_COLOR),
        ]
    return []

def create_random_level(grid_size=6, num_blocks=7): #random level, can change number of blocks or grid size for random lecels
    blocks = []
    target_x = random.randint(0, grid_size // 3)
    blocks.append(Block(target_x, 2, 2, 1, TARGET_COLOR, is_target=True))  # Add the target block first

    for _ in range(num_blocks - 3): #eliminates blocks being in the way of the goal
        while True:
            is_horizontal = random.choice([True, False])
            if is_horizontal:
                width = random.randint(2, 3)
                height = 1
                x = random.randint(0, grid_size - width)
                y = random.choice([i for i in range(grid_size) if i != 2])  # Exclude the goal row
            else:
                width = 1
                height = random.randint(2, 3)
                x = random.randint(0, grid_size - 1)
                y = random.choice([i for i in range(grid_size) if i != 2])  # Exclude the goal row

            new_block = Block(x, y, width, height, BLOCK_COLOR)
            if not any(
                new_block.x < b.x + b.width and
                new_block.x + new_block.width > b.x and
                new_block.y < b.y + b.height and
                new_block.y + new_block.height > b.y
                for b in blocks
            ):
                blocks.append(new_block)
                break

    # Add locked blocks to increase difficulty
    for _ in range(2):
        while True:
            x = random.randint(0, grid_size - 1)
            y = random.choice([i for i in range(grid_size) if i != 2])  # Exclude the goal row
            if not any(
                x < b.x + b.width and x + 1 > b.x and
                y < b.y + b.height and y + 1 > b.y
                for b in blocks
            ):
                blocks.append(Block(x, y, 1, 1, LOCKED_COLOR, is_locked=True))
                break

    return blocks

def draw_grid(screen): #define x and y grids
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, LINE_COLOR, rect, 1)

def main(): #when to start random levels
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Unblock Me - Puzzle Game")
    clock = pygame.time.Clock()
    level_num = 1
    random_levels = False
    board = create_static_level(level_num) if level_num <= 3 else create_random_level()
    selected_block = None
    selected_index = 0
    exit_rect = pygame.Rect(WINDOW_SIZE - CELL_SIZE, 2 * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, EXIT_COLOR, exit_rect)

        for event in pygame.event.get(): #stoping the game and selecting blocks
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for block in board:
                        if block.is_target:
                            selected_block = block
                            break
                elif event.key == pygame.K_TAB:
                    selected_index = (selected_index + 1) % len(board)
                    selected_block = board[selected_index]
                elif selected_block:
                    if event.key == pygame.K_UP:
                        selected_block.move(0, -1, board)
                    elif event.key == pygame.K_DOWN:
                        selected_block.move(0, 1, board)
                    elif event.key == pygame.K_LEFT:
                        selected_block.move(-1, 0, board)
                    elif event.key == pygame.K_RIGHT:
                        selected_block.move(1, 0, board)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for block in board:
                    if block.x * CELL_SIZE <= mouse_x < (block.x + block.width) * CELL_SIZE and block.y * CELL_SIZE <= mouse_y < (block.y + block.height) * CELL_SIZE:
                        selected_block = block
                        break

        for block in board:
            if block.is_target and block.x + block.width == GRID_SIZE: #define win
                print(f"Level {level_num} completed!")
                level_num += 1
                board = create_static_level(level_num) if level_num <= 3 else create_random_level()
                selected_block = None
                selected_index = 0
                break

        draw_grid(screen)
        for block in board:
            block.draw(screen, is_selected=(block == selected_block))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
