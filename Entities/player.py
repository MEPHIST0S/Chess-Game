# Entities/player.py
from connection import get_connection

class Player:
    def __init__(self, player_id, name, rating):
        self.player_id = player_id
        self.name = name
        self.rating = rating

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        if self.player_id is None:
            cursor.execute(
                "INSERT INTO Players (name, rating) VALUES (%s, %s)",
                (self.name, self.rating)
            )
            self.player_id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE Players SET name=%s, rating=%s WHERE player_id=%s",
                (self.name, self.rating, self.player_id)
            )
        connection.commit()
        cursor.close()
        connection.close()