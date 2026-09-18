# 🎮 FORTUNE 4 — The Mystery Board

> A unique terminal-based multiplayer mystery board game built with Python 3, featuring human players, computer opponents, hidden events, power-ups, traps, challenges, and a final mystery round.

---

## 📌 About the Project

**FORTUNE 4** is an interactive, text-based board game designed for **1 to 4 human players**, with the remaining players automatically controlled by the computer.

Unlike traditional board games, players cannot predict what will happen when they land on a mystery cell. Each mystery cell can reveal a different event such as a treasure, trap, shield, teleport, position swap, lucky roll, or quiz challenge.

The game also includes a **Final Mystery Round**, where reaching the final position does not automatically guarantee victory. Players must make a strategic choice that can change the final score.

The entire game is implemented in **a single Python source file** and requires **no graphics or external libraries**.

---

## ✨ Features

### 👥 Flexible Players

The user can decide how many human players participate:

| Selection | Game Setup             |
| --------- | ---------------------- |
| 1         | 1 Human + 3 Computers  |
| 2         | 2 Humans + 2 Computers |
| 3         | 3 Humans + 1 Computer  |
| 4         | 4 Humans               |

### 🎲 Game Mechanics

* Dice-based movement
* 5 × 5 mystery board
* Four-player support
* Human vs Computer gameplay
* Multiple computer opponents
* Turn-based gameplay
* Extra turn when rolling a 6
* Player elimination system
* Score calculation
* Final rankings

### 🔮 Mystery Events

Players discover hidden events when they land on `?` cells.

* 🎁 **Treasure** — Earn coins and points
* 💣 **Trap** — Lose lives
* 🛡️ **Shield** — Protect yourself from a future trap
* 🌀 **Teleport** — Move to a random position
* ⚡ **Double Points** — Double future point rewards
* 🔄 **Position Swap** — Swap position with another player
* 🍀 **Lucky Roll** — Get an additional dice roll
* 🧠 **Mystery Challenge** — Answer a quiz question for rewards

### 👑 Final Mystery

Reaching the final position activates a special final round.

Players can choose:

```text
1. Safe Reward
2. Gamble
3. Steal Coins
```

The gamble option can provide a large bonus but can also reduce the player's points.

---

## 🕹️ How to Play

### Step 1 — Start the Game

Run the program and select:

```text
1. Start New Game
```

### Step 2 — Select Human Players

Choose between 1 and 4 human players.

Example:

```text
1. 1 Human + 3 Computers
2. 2 Humans + 2 Computers
3. 3 Humans + 1 Computer
4. 4 Humans
```

### Step 3 — Enter Player Names

For example:

```text
Enter Player 1 name: Rahul
Enter Player 2 name: Priya
```

Computer players are created automatically.

### Step 4 — Roll the Dice

On a human player's turn:

```text
Press ENTER to roll the dice.
```

The player moves according to the dice result.

### Step 5 — Discover Mystery Events

When a player lands on:

```text
[ ? ]
```

the hidden event is revealed.

Example:

```text
🔮 MYSTERY REVEALED!

💣 TRAP!

-1 life
```

### Step 6 — Reach the Final

When a player reaches the final cell:

```text
[ F ]
```

the **Final Mystery** begins.

### Step 7 — Determine the Winner

The winner is determined using:

1. Highest points
2. Coins as the first tie-breaker
3. Remaining lives as the second tie-breaker

---

## 🖥️ Sample Terminal Interface

```text
======================================================================
                     F O R T U N E   4
                      THE MYSTERY BOARD
======================================================================

MAIN MENU
----------------------------------------------------------------------

1. 🎮 Start New Game
2. 📜 Game Rules
3. ℹ️  About Game
4. 🚪 Exit

----------------------------------------------------------------------

Enter your choice (1-4):
```

### Mystery Board

```text
                         MYSTERY BOARD
------------------------------------------------------------------------

        [ A ] [ . ] [ ? ] [ . ] [ . ]
        [ . ] [ ? ] [ . ] [ B ] [ . ]
        [ ? ] [ . ] [ . ] [ ? ] [ . ]
        [ . ] [ C ] [ ? ] [ . ] [ . ]
        [ . ] [ ? ] [ . ] [ D ] [ F ]

------------------------------------------------------------------------
S = START     ? = MYSTERY     F = FINAL
```

---

## ❤️ Player Statistics

Every player starts with:

```text
Lives  = 3
Coins  = 10
Points = 0
```

Example:

```text
PLAYER STATUS
------------------------------------------------------------------------
A Rahul          HUMAN     Pos: 8  Lives:3  Coins:18  Points:14
B Priya          HUMAN     Po
```
