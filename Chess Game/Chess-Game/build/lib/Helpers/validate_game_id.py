class GameIDValidator:
    @staticmethod
    def validate_game_id(game_id, connection):
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT COUNT(*) as count FROM games WHERE game_id = %s"
            cursor.execute(query, (game_id,))
            result = cursor.fetchone()
            return result['count'] > 0
        except Exception as e:
            print(f"Error validating game ID: {e}")
            return False
        finally:
            cursor.close()