import pygame
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
EXIT_COLOR = (60, 255, 60)
LINE_COLOR = (0, 0, 0)

# Block class to represent each block in the game
class Block:
    def __init__(self, x, y, width, height, color, is_target=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.is_target = is_target
        self.is_horizontal = self.width > self.height
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * CELL_SIZE, self.y * CELL_SIZE, self.width * CELL_SIZE, self.height * CELL_SIZE))
    #Make the blocks move only on one plane
    def move(self, dx, dy, board):
        if self.is_horizontal and dy != 0:
            return False
        if not self.is_horizontal and dx != 0:
            return False

        new_x = self.x + dx
        new_y = self.y + dy
        
        if 0 <= new_x < GRID_SIZE - self.width + 1 and 0 <= new_y < GRID_SIZE - self.height + 1:
            for block in board:
                if block != self:
                    if (new_x < block.x + block.width and new_x + self.width > block.x and
                        new_y < block.y + block.height and new_y + self.height > block.y):
                        return False
            
            self.x = new_x
            self.y = new_y
            return True
        
        return False
#levels block(x,y,horizontal,vertical)
def create_level(level_num):
    if level_num == 1:
        return [
            Block(0, 2, 2, 1, TARGET_COLOR, is_target=True),  # Target block
            Block(3, 0, 3, 1, BLOCK_COLOR),  # Horizontal block
            Block(3, 2, 1, 2, BLOCK_COLOR),  # Vertical block
            Block(4, 1, 1, 3, BLOCK_COLOR),  # Vertical block
        ]
    elif level_num == 2:
        return [
            Block(0, 2, 2, 1, TARGET_COLOR, is_target=True),  # Target block
            Block(1, 0, 2, 1, BLOCK_COLOR),  # Horizontal block
            Block(2, 1, 1, 2, BLOCK_COLOR),  # Vertical block
            Block(3, 3, 2, 1, BLOCK_COLOR),  # Horizontal block
            Block(0, 4, 3, 1, BLOCK_COLOR),  # Horizontal block
        ]
    elif level_num == 3:
        return [
            Block(0, 2, 2, 1, TARGET_COLOR, is_target=True),  # Target block
            Block(0, 0, 1, 2, BLOCK_COLOR),  # Vertical block
            Block(2, 1, 1, 2, BLOCK_COLOR),  # Vertical block
            Block(2, 0, 3, 1, BLOCK_COLOR),  # Horizontal block
            Block(1, 4, 2, 1, BLOCK_COLOR),  # Horizontal block
            Block(4, 5, 2, 1, BLOCK_COLOR),  # Horizontal block
        ]
    #elif level_num == 4:
        #return [
            #Block(0, 2, 2, 1, TARGET_COLOR, is_target=True),  # Target block
            #Block(1, 0, 1, 3, BLOCK_COLOR),  # Vertical block
            #Block(0, 4, 3, 1, BLOCK_COLOR),  # Horizontal block
            #Block(4, 0, 1, 3, BLOCK_COLOR),  # Vertical block
            #Block(4, 3, 2, 1, BLOCK_COLOR),  # Horizontal block
            #Block(2, 4, 1, 2, BLOCK_COLOR),  # Vertical block
        #]
    #elif level_num == 5:
        #return [
            #Block(2, 2, 2, 1, TARGET_COLOR, is_target=True),  # Target block
            #Block(0, 0, 1, 2, BLOCK_COLOR),  # Vertical block
            #Block(0, 2, 1, 3, BLOCK_COLOR),  # Vertical block
            #Block(1, 0, 2, 1, BLOCK_COLOR),  # Horizontal block
            #Block(3, 3, 3, 1, BLOCK_COLOR),  # Horizontal block
            #Block(4, 0, 1, 2, BLOCK_COLOR),  # Vertical block
            #Block(1, 5, 2, 1, BLOCK_COLOR),  # Horizontal block
        #]
    else:
        return []

def draw_grid(screen):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, LINE_COLOR, rect, 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Unblock Me - Puzzle Game")
    
    clock = pygame.time.Clock()
    level_num = 1
    board = create_level(level_num)
    selected_block = None

    exit_rect = pygame.Rect(WINDOW_SIZE - CELL_SIZE, 2 * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, EXIT_COLOR, exit_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for block in board:
                    if block.x * CELL_SIZE <= mouse_x < (block.x + block.width) * CELL_SIZE and block.y * CELL_SIZE <= mouse_y < (block.y + block.height) * CELL_SIZE:
                        selected_block = block
                        break
            elif event.type == pygame.KEYDOWN and selected_block:
                if event.key == pygame.K_UP:
                    selected_block.move(0, -1, board)  # Only for vertical blocks
                elif event.key == pygame.K_DOWN:
                    selected_block.move(0, 1, board)   # Only for vertical blocks
                elif event.key == pygame.K_LEFT:
                    selected_block.move(-1, 0, board)  # Only for horizontal blocks
                elif event.key == pygame.K_RIGHT:
                    selected_block.move(1, 0, board)   # Only for horizontal blocks

        for block in board:
            if block.is_target and block.x + block.width == GRID_SIZE:
                level_num += 1
                if level_num > 3:  #if adding more levels increase this number
                    print("You've completed all levels! Congratulations!")
                    running = False
                else:
                    print(f"Level {level_num} completed! Loading next level...")
                    board = create_level(level_num)
                break
        
        draw_grid(screen)
        
        for block in board:
            block.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
