import pygame
import time
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    """Display the player's current score."""
    value = score_font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [0, 0])

def draw_snake(block_size, snake_list):
    """Draw the snake on the screen."""
    for segment in snake_list:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], block_size, block_size])

def show_message(msg, color):
    """Display a message in the center of the screen."""
    message = font_style.render(msg, True, color)
    screen.blit(message, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            show_message("Game Over! Press Q-Quit or C-Play Again", RED)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        x += x_change
        y += y_change

        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_close = True

        screen.fill(BLUE)
        pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()
