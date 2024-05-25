# manual_move.py

import sys
import os

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (Entities) to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

# Now we can import the necessary modules
from connection import get_connection
from move import Move

def add_move(game_id, move_number, move_text):
    connection = get_connection()
    cursor = connection.cursor()

    query = "INSERT INTO moves (game_id, move_number, move_text) VALUES (%s, %s, %s)"
    values = (game_id, move_number, move_text)

    cursor.execute(query, values)
    connection.commit()

    print(f"Move {move_number}: {move_text} added to game {game_id} successfully!")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    # Define moves for games 3 and 4
    new_moves = {
        3: ["d4", "d5", "c4", "c6", "Nc3", "Nf6", "Nf3", "e6", "e3", "Nbd7"],
        4: ["c4", "c5", "Nf3", "Nf6", "d4", "cxd4", "Nxd4", "Nc6", "Nc3", "e5"]
    }
    
    for game_id, move_list in new_moves.items():
        for move_number, move_text in enumerate(move_list, start=1):
            add_move(game_id, move_number, move_text)