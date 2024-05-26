# d_manual_game.py

import sys
import os

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (Entities) to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

# Now we can import the necessary modules
from b_game import Game

def add_games():
    # Add 5 new games
    new_games = [
        (1, 5, "1-0", "2024-05-29"),
        (3, 2, "1-0", "2024-05-30"),
        (4, 1, "0-1", "2024-06-01"),
        (5, 2, "0.5-0.5", "2024-06-03"),
        (3, 4, "1-0", "2024-06-05")
    ]
    for player1_id, player2_id, result, date in new_games:
        game = Game(None, player1_id, player2_id, result, date)
        game.save()
        print(f"Game between player {player1_id} and {player2_id} on {date} added successfully!")

if __name__ == "__main__":
    add_games()