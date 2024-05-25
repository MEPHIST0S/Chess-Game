class PlayerValidator:
    @staticmethod
    def validate_player_id(player_id):
        # Assuming player IDs are integers and must be positive
        try:
            player_id = int(player_id)
            if player_id > 0:
                return True
            else:
                return False
        except ValueError:
            return False