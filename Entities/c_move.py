# Entities/move.py
from connection import get_connection

class Move:
    def __init__(self, move_id, game_id, move_number, move_text):
        self.move_id = move_id
        self.game_id = game_id
        self.move_number = move_number
        self.move_text = move_text

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        if self.move_id is None:
            cursor.execute(
                "INSERT INTO Moves (game_id, move_number, move_text) VALUES (%s, %s, %s)",
                (self.game_id, self.move_number, self.move_text)
            )
            self.move_id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE Moves SET game_id=%s, move_number=%s, move_text=%s WHERE move_id=%s",
                (self.game_id, self.move_number, self.move_text, self.move_id)
            )
        connection.commit()
        cursor.close()
        connection.close()