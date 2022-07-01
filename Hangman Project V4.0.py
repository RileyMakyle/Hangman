# Riley Hall, Jason Moore
# SDEV 220
# Hangman Final Project
# Due: 10/12/21

import random
from turtle import *

#globals
WORD_FILE = "words.txt"
LIVES = 7
DEFAULT_PENSIZE = 1
t = Turtle()

#function for pen cleanup
def _cleanup():  # this is run at the end of every draw action
    t.pensize(DEFAULT_PENSIZE)
    t.penup()

#function for drawing the lines
def draw_line(x1, y1, x2, y2, width=DEFAULT_PENSIZE):
    t.pensize(width)  # set the line width
    t.setpos(x1, y1)  # set the starting location of the line
    t.pendown()  # begin drawing
    t.goto(x2, y2)  # draw the line

    _cleanup()  # preform cleanup

# coordinate points for the lines
def house(lives):
    lines = [
        [-100, 0, 0, 100],
        [100, 0, 0, 100],
        [-100, 0, 100, 0],
        [-100, 1, 100, 1],
        [-100, 1, -100, -83],
        [100, 1, 100, -83],
        [-100, -88, 100, -88]   
    ]
   #lives check
    if lives >= 6:
        draw_line(*lines[0])
    elif lives >= 5:
        draw_line(*lines[1])
    elif lives >= 4:
        draw_line(*lines[2])
    elif lives >= 3:
        draw_line(*lines[3])
    elif lives >= 2:
        draw_line(*lines[4])
    elif lives >= 1:
        draw_line(*lines[5])
    elif lives >= 0:
        draw_line(*lines[6])
        
#opening file
def get_words(fp):
    with open(fp, "r") as f:
        return [line.strip() for line in f.readlines()]

#replacing * with guessed letter(s)
def special_replace(to_replace, template, final):
    template = list(template)

    for i in range(len(final)):
        if final[i] == to_replace:
            template[i] = to_replace

    return "".join(template)

#main func
def main():
    global count 
    answer = random.choice(get_words(WORD_FILE))
    hint_text = '*' * len(answer)

    guesses = 0


    lives = int(LIVES)
    guess = None
    while (guess != "Exit") and guesses < LIVES:
        if hint_text == answer:
            print("\nCongratulations, You've won!")
            break
        elif guesses < 6:
            print("You have", LIVES - guesses, "lives left.")
        else:
            print("You have", LIVES - guesses, "life left.")
        print("This is the puzzle so far:", hint_text)
        guess = input("Guess a letter: ")

        if guess in answer:
            hint_text = special_replace(guess, hint_text, answer)
        else:
            guesses += 1
            lives -= 1
            house(lives)

    print("\nThe Word Was:", answer)
    print("Game Over.")
    replay = input("Would you like to play again?:  y/n     ")
    if replay == "y":
        t.clear()
        main()


if __name__ == "__main__":
    main()
