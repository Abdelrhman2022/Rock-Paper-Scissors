# Rock Paper Scissors 🪨📄✂️

Welcome to the Rock Paper Scissors game project! This Python project demonstrates object-oriented programming concepts and provides a playable terminal-based game where a human competes against various AI strategies.

---

## 🧠 Project Overview

This game includes:
- A base `Player` class and multiple strategy subclasses
- Game logic for comparing moves and tracking scores
- A `Game` class that handles the match, rounds, and UI prompts

---

## 🎮 How the Game Works

- The game is played between **two players**: a human and a computer.
- The player selects a **difficulty level** that maps to a different strategy:
  - `Starter`: Always plays rock
  - `Easy`: Cycles through rock → paper → scissors
  - `Medium`: Mimics your previous move
  - `Hard`: Picks moves randomly
- The game is played in a **Best of 3** format.
- At the end of the game, a winner is declared or a rematch is offered in case of a draw.

---

## 🧑‍💻 Hints for Understanding the Code

### 📁 Code Structure

| Class           | Description |
|----------------|-------------|
| `Player`        | Abstract base class with `.move()` and `.learn()` methods |
| `Rock`          | Always plays `'rock'` |
| `RandomPlayer`  | Chooses randomly from `['rock', 'paper', 'scissors']` |
| `ReflectPlayer` | Plays opponent's last move |
| `CyclePlayer`   | Cycles through the moves |
| `HumanPlayer`   | Accepts user input |
| `Game`          | Manages game rounds, scores, and mode selection |

### 🔍 Key Methods

- `beats(one, two)`:
  Determines if `one` beats `two` according to RPS rules.

- `Player.learn(my_move, their_move)`:
  Remembers the opponent's last move (used by ReflectPlayer).

- `CyclePlayer.move()`:
  Uses the index of the last move to cycle through the list.

### 🧪 Example Game Output

```text
Welcome to Rock Paper Scissors!
Type Starter, Easy, Medium, or Hard to Begin!
Type Exit to quit.
Please select a game mode: hard

Hard Mode Selected
Game start!

Round 1:
Rock, Paper, Scissors? rock
Player 1: rock  Player 2: scissors
Player 1 wins this round!
Score -> Player 1:1 | Player 2:0
