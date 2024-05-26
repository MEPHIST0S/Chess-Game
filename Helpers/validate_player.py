import mysql.connector
import datetime

from Helpers.connection import get_connection

class PlayerValidator:
    @staticmethod
    def validate_player_id(player_id):
        try:
            player_id = int(player_id)
            if player_id <= 0:
                return False

            # Check if the player ID exists in the database
            connection = get_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM players WHERE player_id = %s"
            cursor.execute(query, (player_id,))
            player = cursor.fetchone()
            cursor.close()
            connection.close()

            if player:
                return True
            else:
                return False
        except ValueError:
            return False