import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 4, 4
TILE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = ("pink")

# Create the game board
board = [[i + j * COLS for i in range(COLS)] for j in range(ROWS)]
empty_row, empty_col = ROWS - 1, COLS - 1  # Position of the empty tile

# Shuffle the board
for _ in range(1000):
    direction = random.choice(['up', 'down', 'left', 'right'])
    if direction == 'up' and empty_row > 0:
        board[empty_row][empty_col], board[empty_row - 1][empty_col] = board[empty_row - 1][empty_col], board[empty_row][empty_col]
        empty_row -= 1
    elif direction == 'down' and empty_row < ROWS - 1:
        board[empty_row][empty_col], board[empty_row + 1][empty_col] = board[empty_row + 1][empty_col], board[empty_row][empty_col]
        empty_row += 1
    elif direction == 'left' and empty_col > 0:
        board[empty_row][empty_col], board[empty_row][empty_col - 1] = board[empty_row][empty_col - 1], board[empty_row][empty_col]
        empty_col -= 1
    elif direction == 'right' and empty_col < COLS - 1:
        board[empty_row][empty_col], board[empty_row][empty_col + 1] = board[empty_row][empty_col + 1], board[empty_row][empty_col]
        empty_col += 1

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sliding Puzzle")

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw tiles
    for row in range(ROWS):
        for col in range(COLS):
            tile = board[row][col]
            if tile != ROWS * COLS:
                pygame.draw.rect(screen, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                font = pygame.font.Font(None, 30)
                text = font.render(str(tile), True, WHITE)
                text_rect = text.get_rect(center=(col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_row, clicked_col = mouse_y // TILE_SIZE, mouse_x // TILE_SIZE
            if abs(clicked_row - empty_row) + abs(clicked_col - empty_col) == 1:
                board[clicked_row][clicked_col], board[empty_row][empty_col] = board[empty_row][empty_col], board[clicked_row][clicked_col]
                empty_row, empty_col = clicked_row, clicked_col

    # Check for win condition
    if all(board[row][col] == col + row * COLS + 1 for row in range(ROWS) for col in range(COLS - 1)):
        font = pygame.font.Font(None, 50)
        text = font.render("You Win!", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()

# Quit pygame
pygame.quit()
