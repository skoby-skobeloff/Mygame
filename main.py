import tkinter as tk
import random

game = tk.Tk()
number = 0
guess = None
guess = tk.Entry(game)
def start():
    global number, guess, button
    number = random.randint(1, 100)
    button.destroy()
    button = tk.Button(text="skip round", command=start)
    submit.pack()
    guess.pack()

def done():
    global guess, number
    button.pack()
    try:
        guess_value = int(guess.get())
        if guess_value == number:
            label1.config(text="you win", font=("arial", 25))
            button.config(text="play again")
        elif guess_value > number:
            label1.config(text="guess smaller", font=("arial", 25))
        elif guess_value < number:
            label1.config(text="guess bigger", font=("arial", 25))
    except ValueError:
        label1.config(text="error!", font=("arial", 25))

submit = tk.Button(game, text="submit", command=done)

label = tk.Label(game, text="guess the number (1-100)")
label.pack()

label1 = tk.Label(game, text="")
label1.pack()

button = tk.Button(game, text="start!", command=start)
button.pack()

game.mainloop()
