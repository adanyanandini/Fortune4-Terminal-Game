
import random
import os
import time


# ============================================================
# FORTUNE 4 - THE MYSTERY BOARD
# 1-4 HUMAN PLAYERS + COMPUTER PLAYERS
#
# Single Python source file
# No graphics
# No external libraries
# ============================================================


# ------------------------------------------------------------
# CLEAR SCREEN
# ------------------------------------------------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ------------------------------------------------------------
# PAUSE
# ------------------------------------------------------------
def pause():
    input("\nPress ENTER to continue...")


# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------
def title():
    print("=" * 72)
    print("                     F O R T U N E   4")
    print("                      THE MYSTERY BOARD")
    print("=" * 72)


# ------------------------------------------------------------
# PLAYER CLASS
# ------------------------------------------------------------
class Player:

    def __init__(self, name, symbol, is_computer=False):
        self.name = name
        self.symbol = symbol
        self.is_computer = is_computer

        self.position = 0
        self.coins = 10
        self.lives = 3
        self.points = 0

        self.shield = 0
        self.double_points = 0
        self.finished = False

    def status(self):

        player_type = "COMPUTER" if self.is_computer else "PLAYER"

        return (
            f"{self.symbol} {self.name:<14} "
            f"{player_type:<9} "
            f"Pos:{self.position + 1:>2}  "
            f"Lives:{self.lives}  "
            f"Coins:{self.coins:<3} "
            f"Points:{self.points:<3}"
        )


# ------------------------------------------------------------
# QUESTIONS
# ------------------------------------------------------------
QUESTIONS = [

    {
        "q": "What is the capital of India?",
        "options": [
            "A) Mumbai",
            "B) New Delhi",
            "C) Chennai",
            "D) Kolkata"
        ],
        "answer": "B"
    },

    {
        "q": "Which language is mainly used to create web pages?",
        "options": [
            "A) HTML",
            "B) Python",
            "C) SQL",
            "D) Java"
        ],
        "answer": "A"
    },

    {
        "q": "How many bits are there in one byte?",
        "options": [
            "A) 4",
            "B) 6",
            "C) 8",
            "D) 16"
        ],
        "answer": "C"
    },

    {
        "q": "Which planet is known as the Red Planet?",
        "options": [
            "A) Earth",
            "B) Mars",
            "C) Venus",
            "D) Jupiter"
        ],
        "answer": "B"
    },

    {
        "q": "What does CPU stand for?",
        "options": [
            "A) Central Processing Unit",
            "B) Computer Personal Unit",
            "C) Central Program Utility",
            "D) Control Processing User"
        ],
        "answer": "A"
    },

    {
        "q": "Which data structure follows FIFO?",
        "options": [
            "A) Stack",
            "B) Queue",
            "C) Tree",
            "D) Graph"
        ],
        "answer": "B"
    },

    {
        "q": "Which number system uses only 0 and 1?",
        "options": [
            "A) Decimal",
            "B) Octal",
            "C) Binary",
            "D) Hexadecimal"
        ],
        "answer": "C"
    },

    {
        "q": "Which device is used to connect networks?",
        "options": [
            "A) Router",
            "B) Keyboard",
            "C) Monitor",
            "D) Printer"
        ],
        "answer": "A"
    }
]


# ------------------------------------------------------------
# MYSTERY EVENTS
# ------------------------------------------------------------
EVENTS = [
    "TREASURE",
    "TRAP",
    "SHIELD",
    "TELEPORT",
    "DOUBLE",
    "SWAP",
    "LUCKY",
    "CHALLENGE"
]


# ------------------------------------------------------------
# CREATE BOARD
# ------------------------------------------------------------
def create_board():

    board = {}

    for i in range(25):
        board[i] = None

    positions = list(range(1, 24))
    random.shuffle(positions)

    index = 0

    # Two of every mystery type
    for event in EVENTS:

        for _ in range(2):

            if index < len(positions):
                board[positions[index]] = event
                index += 1

    return board


# ------------------------------------------------------------
# DISPLAY BOARD
# ------------------------------------------------------------
def display_board(players, board):

    print("\n")
    print("                         MYSTERY BOARD")
    print("-" * 72)

    for row in range(5):

        line = ""

        for col in range(5):

            position = row * 5 + col

            symbols = []

            for player in players:

                if (
                    player.position == position
                    and player.lives > 0
                ):
                    symbols.append(player.symbol)

            if symbols:

                cell = "".join(symbols)

            elif position == 0:

                cell = "S"

            elif position == 24:

                cell = "F"

            elif board[position] is not None:

                cell = "?"

            else:

                cell = "."

            line += f"[{cell:^3}]"

        print("        " + line)

    print("-" * 72)
    print("S = START     ? = MYSTERY     F = FINAL")
    print()


# ------------------------------------------------------------
# DISPLAY STATUS
# ------------------------------------------------------------
def show_status(players):

    print("\nPLAYER STATUS")
    print("-" * 72)

    for player in players:

        print(player.status())

    print("-" * 72)


# ------------------------------------------------------------
# DICE
# ------------------------------------------------------------
def roll_dice():

    return random.randint(1, 6)


# ------------------------------------------------------------
# TREASURE
# ------------------------------------------------------------
def treasure(player):

    coins = random.randint(5, 15)
    points = random.randint(5, 10)

    player.coins += coins
    player.points += points

    print("\n🎁 TREASURE FOUND!")
    print(f"+{coins} coins")
    print(f"+{points} points")


# ------------------------------------------------------------
# TRAP
# ------------------------------------------------------------
def trap(player):

    if player.shield > 0:

        player.shield -= 1

        print("\n🛡️ SHIELD ACTIVATED!")
        print("The trap was completely blocked.")

        return

    damage = random.choice([1, 1, 2])

    player.lives -= damage

    if player.lives < 0:
        player.lives = 0

    print("\n💣 TRAP!")
    print(f"-{damage} life/lives")

    if player.lives == 0:

        print("☠️ You have been eliminated!")


# ------------------------------------------------------------
# SHIELD
# ------------------------------------------------------------
def shield_event(player):

    player.shield += 1

    print("\n🛡️ MYSTERY SHIELD!")
    print("You received one shield.")


# ------------------------------------------------------------
# TELEPORT
# ------------------------------------------------------------
def teleport(player):

    new_position = random.randint(1, 23)

    player.position = new_position

    print("\n🌀 TELEPORT!")
    print(
        f"You were teleported to position "
        f"{new_position + 1}."
    )


# ------------------------------------------------------------
# DOUBLE POINTS
# ------------------------------------------------------------
def double_points(player):

    player.double_points = 3

    print("\n⚡ DOUBLE POINTS!")
    print("Your next 3 point rewards are doubled.")


# ------------------------------------------------------------
# SWAP
# ------------------------------------------------------------
def swap_player(player, players):

    available = [
        p for p in players
        if p != player and p.lives > 0
    ]

    if not available:

        print("\n🔄 No other active player available.")

        return

    target = random.choice(available)

    player.position, target.position = (
        target.position,
        player.position
    )

    print("\n🔄 POSITION SWAP!")
    print(
        f"{player.name} swapped position "
        f"with {target.name}!"
    )


# ------------------------------------------------------------
# LUCKY ROLL
# ------------------------------------------------------------
def lucky(player):

    print("\n🍀 LUCKY ROLL!")
    print("You receive one additional dice roll.")

    if not player.is_computer:
        input("Press ENTER to roll...")
    else:
        time.sleep(0.8)

    number = roll_dice()

    print(f"🎲 Lucky roll: {number}")

    player.position += number

    if player.position >= 24:

        player.position = 24
        player.finished = True

    player.points += number

    print(
        f"Moved to position "
        f"{player.position + 1}."
    )

    print(f"+{number} points")


# ------------------------------------------------------------
# CHALLENGE
# ------------------------------------------------------------
def challenge(player):

    question = random.choice(QUESTIONS)

    print("\n🧠 MYSTERY CHALLENGE!")
    print("-" * 55)

    print(question["q"])

    for option in question["options"]:

        print(option)

    if player.is_computer:

        time.sleep(1)

        # Computer has 70% chance of choosing correctly
        if random.random() < 0.70:

            answer = question["answer"]

        else:

            wrong_answers = [
                "A", "B", "C", "D"
            ]

            wrong_answers.remove(
                question["answer"]
            )

            answer = random.choice(wrong_answers)

        print(
            f"\n🤖 {player.name} selected: {answer}"
        )

    else:

        answer = input(
            "\nYour answer: "
        ).strip().upper()

    if answer == question["answer"]:

        reward = random.randint(10, 20)

        player.points += reward
        player.coins += 5

        print("\n🎉 CORRECT!")
        print(f"+{reward} points")
        print("+5 coins")

    else:

        print("\n❌ WRONG ANSWER!")
        print("No reward this time.")


# ------------------------------------------------------------
# MYSTERY EVENT
# ------------------------------------------------------------
def mystery_event(player, players, board):

    event = board.get(player.position)

    if event is None:

        print("\nNothing special happened here.")

        return

    # Mystery is revealed only once
    board[player.position] = None

    print("\n")
    print("=" * 60)
    print("                  🔮 MYSTERY REVEALED!")
    print("=" * 60)

    if event == "TREASURE":

        treasure(player)

    elif event == "TRAP":

        trap(player)

    elif event == "SHIELD":

        shield_event(player)

    elif event == "TELEPORT":

        teleport(player)

    elif event == "DOUBLE":

        double_points(player)

    elif event == "SWAP":

        swap_player(player, players)

    elif event == "LUCKY":

        lucky(player)

    elif event == "CHALLENGE":

        challenge(player)

    print("=" * 60)


# ------------------------------------------------------------
# MOVEMENT POINTS
# ------------------------------------------------------------
def give_movement_points(player, dice):

    points = dice

    if player.double_points > 0:

        points *= 2
        player.double_points -= 1

        print(
            f"⚡ DOUBLE BONUS! "
            f"+{points} points"
        )

    else:

        print(f"⭐ +{points} points")

    player.points += points


# ------------------------------------------------------------
# HUMAN MOVE
# ------------------------------------------------------------
def human_turn(player):

    print(
        f"\n🎮 {player.name}'s turn "
        f"({player.symbol})"
    )

    print("Press ENTER to roll the dice.")
    print("Type Q to leave the current game.")

    choice = input("\nYour choice: ").strip().lower()

    if choice == "q":

        return None

    dice = roll_dice()

    print(
        f"\n🎲 {player.name} rolled: {dice}"
    )

    return dice


# ------------------------------------------------------------
# COMPUTER MOVE
# ------------------------------------------------------------
def computer_turn(player, players):

    print(
        f"\n🤖 {player.name}'s turn "
        f"({player.symbol})"
    )

    print("Computer is thinking...")

    time.sleep(1)

    dice = roll_dice()

    print(
        f"🎲 {player.name} rolled: {dice}"
    )

    return dice


# ------------------------------------------------------------
# MOVE PLAYER
# ------------------------------------------------------------
def move_player(player, dice):

    old_position = player.position

    player.position += dice

    if player.position >= 24:

        player.position = 24
        player.finished = True

    print(
        f"Moved from position "
        f"{old_position + 1} "
        f"to position "
        f"{player.position + 1}."
    )


# ------------------------------------------------------------
# FINAL MYSTERY
# ------------------------------------------------------------
def final_mystery(player, players):

    print("\n")
    print("=" * 72)
    print("                       👑 FINAL MYSTERY")
    print("=" * 72)

    print(
        f"\n{player.name} reached the FINAL position!"
    )

    print(
        "\nReaching the final does NOT automatically "
        "mean victory."
    )

    # COMPUTER FINAL CHOICE
    if player.is_computer:

        time.sleep(1)

        choice = random.choice(["1", "2", "3"])

        print(
            f"\n🤖 Computer selected option {choice}"
        )

    else:

        print("\nChoose your final action:")
        print("1. SAFE REWARD     → +30 points")
        print("2. GAMBLE          → Risk +50 / -20")
        print("3. STEAL           → Steal up to 15 coins")

        while True:

            choice = input(
                "\nYour choice: "
            ).strip()

            if choice in ["1", "2", "3"]:

                break

            print(
                "Invalid choice. "
                "Select 1, 2, or 3."
            )

    # SAFE REWARD
    if choice == "1":

        player.points += 30

        print("\n👑 SAFE REWARD!")
        print("+30 points")

    # GAMBLE
    elif choice == "2":

        number = roll_dice()

        print(
            f"\n🎲 Gamble roll: {number}"
        )

        if number >= 4:

            player.points += 50

            print("🍀 JACKPOT!")
            print("+50 points")

        else:

            player.points -= 20

            if player.points < 0:

                player.points = 0

            print("💥 Gamble failed!")
            print("-20 points")

    # STEAL
    elif choice == "3":

        available = [
            p for p in players
            if p != player
            and p.lives > 0
            and p.coins > 0
        ]

        if not available:

            print(
                "\nNo player has coins to steal."
            )

            player.points += 15

            print(
                "Instead, you received +15 points."
            )

        else:

            target = random.choice(available)

            amount = min(
                15,
                target.coins
            )

            target.coins -= amount
            player.coins += amount

            print("\n🕵️ SECRET THEFT!")
            print(
                f"You stole {amount} coins "
                f"from {target.name}."
            )


# ------------------------------------------------------------
# CHECK ELIMINATION
# ------------------------------------------------------------
def check_elimination(player):

    if player.lives <= 0:

        print(
            f"\n☠️ {player.name} "
            f"has been eliminated!"
        )

        return True

    return False


# ------------------------------------------------------------
# GET ACTIVE PLAYERS
# ------------------------------------------------------------
def active_players(players):

    return [
        player
        for player in players
        if player.lives > 0
    ]


# ------------------------------------------------------------
# DETERMINE WINNER
# ------------------------------------------------------------
def determine_winner(players):

    alive = active_players(players)

    if alive:

        return max(
            alive,
            key=lambda p: (
                p.points,
                p.coins,
                p.lives
            )
        )

    return max(
        players,
        key=lambda p: (
            p.points,
            p.coins,
            p.lives
        )
    )


# ------------------------------------------------------------
# SHOW WINNER
# ------------------------------------------------------------
def show_winner(players):

    clear_screen()

    title()

    print("\n")
    print("=" * 72)
    print("                         🏆 GAME OVER")
    print("=" * 72)

    winner = determine_winner(players)

    print(
        f"\n👑 WINNER: {winner.name}"
    )

    print(f"Symbol : {winner.symbol}")
    print(f"Points : {winner.points}")
    print(f"Coins  : {winner.coins}")
    print(f"Lives  : {winner.lives}")

    print("\nFINAL RANKINGS")
    print("-" * 72)

    ranking = sorted(
        players,
        key=lambda p: (
            p.points,
            p.coins,
            p.lives
        ),
        reverse=True
    )

    for index, player in enumerate(
        ranking,
        start=1
    ):

        player_type = (
            "COMPUTER"
            if player.is_computer
            else "HUMAN"
        )

        print(
            f"{index}. "
            f"{player.name:<15} "
            f"{player_type:<8} "
            f"Points:{player.points:<4} "
            f"Coins:{player.coins:<3} "
            f"Lives:{player.lives}"
        )

    print("-" * 72)

    pause()


# ------------------------------------------------------------
# GAME RULES
# ------------------------------------------------------------
def show_rules():

    clear_screen()

    title()

    print("\nGAME RULES")
    print("-" * 72)

    print("""
1. You can choose between 1 and 4 HUMAN players.

2. The remaining positions are automatically filled
   by COMPUTER players.

   Examples:
      1 Human → 1 Human + 3 Computers
      2 Humans → 2 Humans + 2 Computers
      3 Humans → 3 Humans + 1 Computer
      4 Humans → 4 Human players

3. Every player starts with:
      ❤️ 3 Lives
      🪙 10 Coins
      ⭐ 0 Points

4. Players take turns rolling a dice.

5. The board contains hidden mystery cells.

6. Mystery events include:
      🎁 Treasure
      💣 Trap
      🛡️ Shield
      🌀 Teleport
      ⚡ Double Points
      🔄 Position Swap
      🍀 Lucky Roll
      🧠 Challenge

7. A shield can block a trap.

8. Rolling a SIX gives the player another turn.

9. Losing all lives eliminates the player.

10. Reaching the final cell activates the FINAL MYSTERY.

11. The final player can:
      - Take a safe reward
      - Gamble for a bigger reward
      - Steal coins

12. The winner is determined by:
      1. Points
      2. Coins
      3. Remaining Lives
""")

    pause()


# ------------------------------------------------------------
# CREATE PLAYERS
# ------------------------------------------------------------
def create_players():

    clear_screen()

    title()

    print("\n")
    print("PLAYER SETUP")
    print("-" * 72)

    print(
        "How many HUMAN players want to play?"
    )

    print("\n1. 1 Human + 3 Computers")
    print("2. 2 Humans + 2 Computers")
    print("3. 3 Humans + 1 Computer")
    print("4. 4 Humans")

    while True:

        choice = input(
            "\nEnter number of HUMAN players (1-4): "
        ).strip()

        if choice in ["1", "2", "3", "4"]:

            human_count = int(choice)

            break

        print(
            "Invalid choice. "
            "Please enter 1, 2, 3, or 4."
        )

    players = []

    symbols = ["A", "B", "C", "D"]

    # HUMAN PLAYERS
    for i in range(human_count):

        while True:

            name = input(
                f"\nEnter Player {i + 1} name: "
            ).strip()

            if name:

                break

            print(
                "Name cannot be empty."
            )

        players.append(
            Player(
                name,
                symbols[i],
                False
            )
        )

    # COMPUTER PLAYERS
    computer_count = 4 - human_count

    for i in range(computer_count):

        computer_number = i + 1

        players.append(
            Player(
                f"Computer {computer_number}",
                symbols[
                    human_count + i
                ],
                True
            )
        )

    print("\n")
    print("=" * 72)
    print("                    PLAYERS READY")
    print("=" * 72)

    for player in players:

        player_type = (
            "COMPUTER"
            if player.is_computer
            else "HUMAN"
        )

        print(
            f"{player.symbol}  "
            f"{player.name:<15} "
            f"[{player_type}]"
        )

    print("=" * 72)

    pause()

    return players


# ------------------------------------------------------------
# PLAY GAME
# ------------------------------------------------------------
def play_game():

    players = create_players()

    board = create_board()

    current_index = 0

    # --------------------------------------------------------
    # GAME LOOP
    # --------------------------------------------------------
    while True:

        alive = active_players(players)

        # If only one player is alive, finish
        if len(alive) <= 1:

            break

        player = players[current_index]

        # Skip eliminated player
        if player.lives <= 0:

            current_index = (
                current_index + 1
            ) % len(players)

            continue

        clear_screen()

        title()

        print(
            f"\nCURRENT TURN: "
            f"{player.name} ({player.symbol})"
        )

        if player.is_computer:

            print("🤖 COMPUTER PLAYER")

        else:

            print("🎮 HUMAN PLAYER")

        display_board(
            players,
            board
        )

        show_status(players)

        # ----------------------------------------------------
        # GET DICE
        # ----------------------------------------------------
        if player.is_computer:

            dice = computer_turn(
                player,
                players
            )

        else:

            dice = human_turn(player)

            # Q = quit game
            if dice is None:

                print(
                    "\nReturning to main menu..."
                )

                time.sleep(1)

                return

        # ----------------------------------------------------
        # MOVE
        # ----------------------------------------------------
        move_player(
            player,
            dice
        )

        # ----------------------------------------------------
        # POINTS
        # ----------------------------------------------------
        give_movement_points(
            player,
            dice
        )

        time.sleep(0.8)

        # ----------------------------------------------------
        # FINAL MYSTERY
        # ----------------------------------------------------
        if player.position == 24:

            if not player.finished:

                player.finished = True

            final_mystery(
                player,
                players
            )

        # ----------------------------------------------------
        # NORMAL MYSTERY
        # ----------------------------------------------------
        else:

            if board.get(
                player.position
            ) is not None:

                mystery_event(
                    player,
                    players,
                    board
                )

        # ----------------------------------------------------
        # ELIMINATION
        # ----------------------------------------------------
        check_elimination(player)

        # ----------------------------------------------------
        # EXTRA TURN
        # ----------------------------------------------------
        if (
            dice == 6
            and player.lives > 0
        ):

            print("\n🎲 YOU ROLLED A SIX!")

            print(
                f"{player.name} gets another turn!"
            )

            pause()

            continue

        pause()

        # ----------------------------------------------------
        # NEXT PLAYER
        # ----------------------------------------------------
        current_index = (
            current_index + 1
        ) % len(players)

    # --------------------------------------------------------
    # GAME END
    # --------------------------------------------------------
    show_winner(players)


# ------------------------------------------------------------
# ABOUT
# ------------------------------------------------------------
def show_about():

    clear_screen()

    title()

    print("\nABOUT THE GAME")
    print("-" * 72)

    print("""
FORTUNE 4 is a mystery-based terminal board game
designed for up to four players.

The game supports both HUMAN and COMPUTER players.

The number of human players is selected at the
beginning of every game.

The remaining positions are automatically controlled
by the computer.

The board contains hidden events, so players cannot
predict what will happen when they land on a mystery
cell.

The game combines:

    🎲 Dice
    ❤️ Lives
    🪙 Coins
    ⭐ Points
    🎁 Treasure
    💣 Traps
    🛡️ Shields
    🌀 Teleportation
    🔄 Position Swapping
    ⚡ Power-ups
    🧠 Quiz Challenges
    👑 Final Mystery

Technology:
    Python 3
    Terminal Interface
    Object-Oriented Programming
    Randomized Game Logic

No external libraries are required.
""")

    print("-" * 72)

    pause()


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------
def main_menu():

    while True:

        clear_screen()

        title()

        print("\n")
        print("MAIN MENU")
        print("-" * 72)

        print("1. 🎮 Start New Game")
        print("2. 📜 Game Rules")
        print("3. ℹ️  About Game")
        print("4. 🚪 Exit")

        print("-" * 72)

        choice = input(
            "\nEnter your choice (1-4): "
        ).strip()

        if choice == "1":

            play_game()

        elif choice == "2":

            show_rules()

        elif choice == "3":

            show_about()

        elif choice == "4":

            clear_screen()

            title()

            print(
                "\nThank you for playing "
                "FORTUNE 4!"
            )

            print(
                "Goodbye! 👋\n"
            )

            break

        else:

            print(
                "\nInvalid option!"
            )

            print(
                "Please select 1, 2, 3, or 4."
            )

            time.sleep(1.5)


# ------------------------------------------------------------
# PROGRAM START
# ------------------------------------------------------------
if __name__ == "__main__":

    main_menu()

