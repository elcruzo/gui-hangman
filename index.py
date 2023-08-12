import tkinter as tk
import random

with open ('wordlist.txt', 'r') as f:
    words = f.readlines()

class HangmanGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.word_to_guess = random.choice(words)[:-1]  # The word the player needs to guess
        self.remaining_attempts = 6
        self.guesses = []
        
        self.word_display = tk.Label(root, text="_" * len(self.word_to_guess))
        self.word_display.pack()
        
        self.input_entry = tk.Entry(root)
        self.input_entry.pack()
        
        self.submit_button = tk.Button(root, text="Guess", command=self.make_guess)
        self.submit_button.pack()
        
        self.attempts_label = tk.Label(root, text=f"Attempts remaining: {self.remaining_attempts}")
        self.attempts_label.pack()
        
    def make_guess(self):
        guess = self.input_entry.get().lower()
        self.guesses.append(guess)
        
        # Update the displayed word with correctly guessed letters
        guessed_word = ""
        for letter in self.word_to_guess:
            if letter in self.guesses:
                guessed_word += letter
            else:
                guessed_word += "_"
        self.word_display.config(text=guessed_word)
        
        # Update attempts remaining
        self.remaining_attempts -= 1
        self.attempts_label.config(text=f"Attempts remaining: {self.remaining_attempts}")
        
        # Check win/lose condition and update message accordingly
        if "_" not in guessed_word:
            message = "Congratulations! You guessed the word!"
            self.word_display.config(text=message)
        elif self.remaining_attempts == 0:
            message = f"Sorry, you're out of attempts. The word was '{self.word_to_guess}'."
            self.word_display.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    hangman_game = HangmanGameGUI(root)
    root.mainloop()
