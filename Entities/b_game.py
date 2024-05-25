# Entities/game.py
from Helpers.connection import get_connection

class Game:
    def __init__(self, game_id, player1_id, player2_id, result, date_played):
        self.game_id = game_id
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.result = result
        self.date_played = date_played

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        if self.game_id is None:
            cursor.execute(
                "INSERT INTO Games (player1_id, player2_id, result, date_played) VALUES (%s, %s, %s, %s)",
                (self.player1_id, self.player2_id, self.result, self.date_played)
            )
            self.game_id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE Games SET player1_id=%s, player2_id=%s, result=%s, date_played=%s WHERE game_id=%s",
                (self.player1_id, self.player2_id, self.result, self.date_played, self.game_id)
            )
        connection.commit()
        cursor.close()
        connection.close()