# Classic Snake game which was popular in the late 90's and early 2000's with the Nokia phone.
# Project Created by Trishal Varma

import curses
from random import randint


                                        # setting up the window
curses.initscr()                        # init screen
win = curses.newwin(20, 60, 0, 0)       #(nLines: int, ncols: int, begin_y: int=..., begin_x: int=...) -> _CursesWindow
                                            # in curses.newwin, the entry points is from y, then to x, where in most application its the other way around
win.keypad(1)                           # Using the arrow keys
curses.noecho()                         # Not listen to any other keystrokes
curses.curs_set(0)                      # Hide the cursor
win.border(0)                           # Draw a border
win.nodelay(1)                          # 1 is true, not waiting for the next user input. (-1) so loop continues.


# snake and food
snake = [(4, 10), (4, 9), (4, 8)]                            # For creating the snake, we are using (y,x) coordinate
                                            # We use a tuple () because it is immutable
food = (10, 20)


# game logic using a while loop

win.addch(food[0], food[1], '#')
score = 0
ESC = 27                        # in the curses module, escape is key 27
key = curses.KEY_RIGHT

while key !=ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120)     # increase speed as snake gets bigger

    prev_key = key
    event = win.getch()                 # Here we are waiting for the next user input
        # in this block, we want to figure out what we want to do once there is an input.
        # this also includes keeping score.
    key = event if event != -1 else prev_key  # setting new key if not -1, then use already set key
    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # calculate the next coordinates for the snake
    # get current coordinate

    y = snake[0][0]     # y , x getting our head and tail
    x = snake[0][1]
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        y += 1

    snake.insert(0, (y, x))  # inserting the new coordinate.
                             # append O(n) which is much better. YOU CAN CHANGE THIS IN YOUR CODE

    # check if we git the border

    if y == 0: break
    if y == 19: break  # border is set to 20, so break at 19
    if x == 0: break
    if x == 59: break   # border is set to 60, so breka at 59

    # if snake runs over itself, then break
    if snake[0] in snake[1:]: break

    if snake[0] == food:
        # eat the food
        score +=1
        food = ()
        while food == ():
            food = (randint(1, 18), randint(1,58))           # we find the new coordinate using the import random import rand int
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
    else:
        # move snake
        last = snake.pop()                      # return the last coordinate
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '*')  # we add character with y coordinate then x

curses.endwin()
print(f"Final score = {score}")

