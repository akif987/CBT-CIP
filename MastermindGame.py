import tkinter as tk
from random import randint

class MastermindGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mastermind Game")

        self.player_turn = 1
        self.number_to_guess = str(randint(1000, 9999))
        self.guesses = 0
        self.guesses_label = tk.Label(self.window, text="Guesses: 0")
        self.guesses_label.pack()

        self.hints_label = tk.Label(self.window, text="Hints:")
        self.hints_label.pack()

        self.guess_entry = tk.Entry(self.window)
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.window, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        self.window.mainloop()

    def check_guess(self):
        guess = self.guess_entry.get()
        self.guesses += 1
        self.guesses_label['text'] = f"Guesses: {self.guesses}"

        hints = ""
        for i in range(4):
            if guess[i] == self.number_to_guess[i]:
                hints += "🔥"  # Correct digit in correct position
            elif guess[i] in self.number_to_guess:
                hints += "💡"  # Correct digit in incorrect position
            else:
                hints += "❌"  # Incorrect digit
        self.hints_label['text'] = f"Hints: {hints}"

        if guess == self.number_to_guess:
            self.result_label['text'] = f"Congratulations, Player {self.player_turn}! You guessed the number in {self.guesses} attempts."
            self.guess_button['state'] = tk.DISABLED

            # Switch player turns
            self.player_turn = 2 if self.player_turn == 1 else 1
            self.number_to_guess = str(randint(1000, 9999))
            self.guesses = 0
            self.guesses_label['text'] = "Guesses: 0"
            self.hints_label['text'] = "Hints:"
            self.guess_button['state'] = tk.NORMAL
            self.guess_entry.delete(0, tk.END)  # Clear the entry field

MastermindGame()