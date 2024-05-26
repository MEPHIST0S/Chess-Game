# d_manual_move.py

import sys
import os

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (Entities) to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from c_move import Move

# Define the base Move class
class Move:
    def __init__(self, move_id, game_id, move_number, move_text):
        self.move_id = move_id
        self.game_id = game_id
        self.move_number = move_number
        self.move_text = move_text

    def save(self):
        raise NotImplementedError("save method must be implemented by subclasses")

# Subclass for specific types of moves (if needed)
# For example, you could have subclasses for opening moves, mid-game moves, and end-game moves.

# Your add_moves function remains unchanged
def add_moves():
    new_moves = {
        1: ["e4", "d5", "Nf3", "c6", "d4", "Nf6", "Nc3", "e6"],
        2: ["c4", "c5", "Nf3", "Nc6", "d4", "cxd4", "Nxd4", "Nf6"],
        3: ["e4", "e5", "Nf3", "Nc6", "Bb5", "a6", "Ba4", "Nf6"],
        4: ["e4", "e5", "Nf3", "d6", "d4", "exd4", "Nxd4", "Bd7"],
        5: ["d4", "d5", "Nc3", "Nf6", "Bg5", "Be7", "e5", "Nfd7"]
    }
    for game_id, move_list in new_moves.items():
        for move_number, move_text in enumerate(move_list, start=1):
            move = Move(None, game_id, move_number, move_text)  # Create Move instance
            move.save()
            print(f"Move {move_number}: {move_text} added to game {game_id} successfully!")

if __name__ == "__main__":
    add_moves()