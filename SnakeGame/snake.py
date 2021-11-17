# The Snake Game was popularized by the Nokia phone game in the early late 90's and early 2000's.
# The game continues to be a nostalgic experience, but also a learning experience for those programming.
# Today we will develop our own snake game using PyGame
# Project by Trishal Varma


import random
import pygame

pygame.init()  # Initialize pygame.

# Define the colors of the game in Pygame

white = (255, 255, 255)  # For the color of our snake
black = (0, 0, 0)  # Black will be our background color
red = (255, 0, 0)  # Color of the game over message
orange = (255, 165, 0)  # Food color that we will chase

# Height and width of the window to firstly fit the instructions for the game
# Second to allow a more challenging random food deposit at the edges
# Change the height and width to your liking

width, height = 1000, 500

game_display = pygame.display.set_mode((width, height))  # pygame display allow you to set the specified h x w
pygame.display.set_caption("Snake Game")  # Set caption

clock = pygame.time.Clock()

# both are set in pixels which we will later specify
# we don't need to write px like in CSS
snake_size = 10
snake_speed = 15

# You can change the font to your liking, check which fonts are supported by your OS
message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)


# Print score function
def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)  # we set the color that we declared above
    game_display.blit(text, [0, 0])

    # Drawing our snake and what it would look like. You can add characters in the empty array as well


def draw_snake(snake_size, snake_pixel):
    for pixel in snake_pixel:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])

        # Def game uses the target to set random range for food, which can be changed with size of window


def run_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixel = []
    snake_length = 1

    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    # We create this loop so we can exit or restart the game from the current pygame window that's open
    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over! 1 to quit 2 to restart", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:  # K_1 is 1 on the keyboard
                        game_over = True  # We can specify that 1 is game over, and not game close
                        game_close = False
                    if event.key == pygame.K_2:  # K_2 is 2 on the keyboard
                        run_game()  # we run the game again, since the option was 2.
                if event.type == pygame.QUIT:  # exiting the inner loop
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    # Left is (-), if you're in top left window, you are in position 0,0
                    # The more you move right, you increase the x value, or the position
                    # The more you move down you increase the y position
                    # So by having (-snake_size) you are decreasing the x value towards 0.
                    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    # y_speed is 0 because key right, we can't go diagonally
                    # the same logic follow for all those below.
                    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

                    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                    # We Lost the game, but we didn't quit, so we go into the loop that's
                    # defined above in the loops.
                    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        # Drawing the game board, and the food with the snake
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])
        snake_pixel.append([x, y])

        if len(snake_pixel) > snake_length:
            del snake_pixel[0]         # we use del to show the illusion of the snake getting bigger,
                                       # the append above adds when we eat.

        for pixel in snake_pixel[:-1]:
            if pixel == [x, y]:         # if the pixel is in the same position as the snake
                                        # then it ran into itself going in circles, or going directionally.
                game_close = True

        draw_snake(snake_size, snake_pixel)
        print_score(snake_length - 1)   # since default length of snake is 1, we use -1 to give us a 0 score.

        pygame.display.update()

        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        # This is eating the target food in the random range that we put.
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


run_game()
