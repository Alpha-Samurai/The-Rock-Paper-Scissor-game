# 🪨📄✂️ The Stone-Paper-Scissor Game

The OG childhood game that we have played every day with our besties and BFFs, now in your terminal.
I made it during my **1st semester in college**, as one of my first Python projects.

![Language](https://img.shields.io/badge/language-Python-blue)
![Type](https://img.shields.io/badge/type-terminal%20game-lightgrey)

---

## 📖 About

Stone-Paper-Scissor (also called Rock-Paper-Scissors) is a hand game where each player picks one of three moves at the same time. In this version, **you play against the computer**, which picks its move at random.

I built it to practise the basics from my first semester: `while` loops, `if/elif/else`, dictionaries, string formatting and the `random` module.

---

## 🎮 Rules

| Your move | Beats | Loses to |
|---|---|---|
| 🪨 Rock | ✂️ Scissor | 📄 Paper |
| 📄 Paper | 🪨 Rock | ✂️ Scissor |
| ✂️ Scissor | 📄 Paper | 🪨 Rock |

If both players pick the same move, the round is a **draw**.

---

## ✨ Features

- The computer's move is chosen randomly with `random.choice()`
- Shows your move and the computer's move after every round
- Tells you whether you won, lost or drew
- Rejects invalid input instead of crashing
- Asks whether you want to play again, and keeps going until you quit

---

## 🚀 How to Run

You need **Python 3** installed.

```bash
git clone https://github.com/[your-username]/The-Stone-Paper-Scissor-game.git
cd The-Stone-Paper-Scissor-game
python game.py
```

---

## 💻 Working Example

```
Enter your choice to begin
 R for rock
 P for paper
 S for scissor : R

 You chose Rock
 Computer chose Scissor

You Won !!

 Play again? Type 'Yes' to continue or 'No' to quit : Yes

Enter your choice to begin :
 R for rock
 P for paper
 S for scissor : X
Invalid Input

Enter your choice to begin :
 R for rock
 P for paper
 S for scissor : P

 You chose Paper
 Computer chose Paper

That's a Draw

 Play again? Type 'Yes' to continue or 'No' to quit : No
 Thank you for playing !!
```

---

## 🧠 How It Works

1. The player types **R**, **P** or **S** (upper or lower case both work).
2. The input is checked against a dictionary of valid choices. Anything else prints `Invalid Input` and asks again.
3. `random.choice()` picks the computer's move.
4. If both moves are the same, it is a draw. Otherwise a second dictionary, `beats`, says which move wins.
5. The result is printed, and the player is asked whether to play again.

---


## 🔮 Future Improvements

- A running scoreboard (wins, losses, draws)
- Best-of-3 and best-of-5 modes
- Two-player mode
- A graphical version with Tkinter or a web page

---

## 👤 Author

** Daksh Nagarkar **, 1st-semester CSE(AI-ML) student
GitHub: [Alpha-Samurai](https://github.com/[your-username])

If you liked it, give the repo a ⭐ and challenge your bestie to a round!
