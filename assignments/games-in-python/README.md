
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game in Python to practice strings, loops, conditionals, lists, random selection, and user input.

## 📝 Tasks

### 🛠️ Create the game setup

#### Description

Use the provided starter code to select a secret word and initialize the variables needed to track the player's progress.

#### Requirements

Completed program should:

- Select a word randomly from the provided `words` list.
- Track guessed letters, incorrect guesses, and the maximum number of incorrect guesses.
- Keep the secret word hidden from the player.

### 🛠️ Implement the guessing loop

#### Description

Create the main game loop so the player can guess letters, see their progress, and receive a win or loss message when the game ends.

#### Requirements

Completed program should:

- Display the guessed word with unknown letters represented by underscores.
- Accept letter guesses and update the displayed progress when a guess is correct.
- Reduce the remaining attempts for incorrect guesses and end when the word is guessed or attempts are exhausted.
- Display a clear win or loss message at the end of the game.
