# d_manual_move.py

import sys
import os

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (Entities) to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

# Now we can import the necessary modules
from c_move import Move

def add_moves():
    # Add moves for games 6 to 10
    new_moves = {
        6: ["e4", "d5", "Nf3", "c6", "d4", "Nf6", "Nc3", "e6"],
        7: ["c4", "c5", "Nf3", "Nc6", "d4", "cxd4", "Nxd4", "Nf6"],
        8: ["e4", "e5", "Nf3", "Nc6", "Bb5", "a6", "Ba4", "Nf6"],
        9: ["e4", "e5", "Nf3", "d6", "d4", "exd4", "Nxd4", "Bd7"],
        10: ["d4", "d5", "Nc3", "Nf6", "Bg5", "Be7", "e5", "Nfd7"]
    }
    for game_id, move_list in new_moves.items():
        for move_number, move_text in enumerate(move_list, start=1):
            move = Move(None, game_id, move_number, move_text)
            move.save()
            print(f"Move {move_number}: {move_text} added to game {game_id} successfully!")

if __name__ == "__main__":
    add_moves()
