# d_manual_player.py

import sys
import os

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (Entities) to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

# Now we can import the necessary modules
from a_player import Player

def add_players():
    # Add 5 new players
    new_players = [
        ("Cathy", 1450),
        ("David", 1380),
        ("Emily", 1525),
        ("George", 1410),
        ("Helen", 1470),
        ("Jason", 1750),
        ("Carlos", 1580),
        ("Donatello", 1125),
        ("Cesar", 1010),
        ("Atilla", 1370)
        
    ]
    for name, rating in new_players:
        player = Player(None, name, rating)
        player.save()
        print(f"Player {name} with rating {rating} added successfully!")

if __name__ == "__main__":
    add_players()