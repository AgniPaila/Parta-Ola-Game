# 🎲 Parta Ola – (Python)
Parta Ola is a game of chance written in Python. It simulates a spinning wheel that determines each player's action. The last player remaining wins the game!

# 🕹️ Game Overview
Played by 2 or more players

Each player starts with an equal number of beans

The game is played in rounds, and each round consists of:

Every player placing 1 bean in the center at the start

One player spins the wheel and performs the action indicated

Play proceeds to the next active player

# 🎡 Wheel Outcomes & Actions
Put One: Player puts 1 bean in the center 

Put Two: Player puts 2 beans in the center 

Put All: All players put 1 bean in the center 

Take One: Player takes 1 bean from center

Take Two: Player takes 2 beans from center (or 1 if only one)

Take All: Player takes all beans from center; round ends

# 🔄 Round Rules
A round ends when the center is empty

The next round starts with all remaining players placing 1 bean

If a player cannot contribute, they are eliminated

The next player in line (after the last to play) starts the new round

# 💀 Elimination
A player is eliminated if:

They can't perform a required "put" action

They can't contribute at the start of a round

Eliminated players do not return in later rounds

# 🏆 Winning
The last player remaining is declared the winner!
