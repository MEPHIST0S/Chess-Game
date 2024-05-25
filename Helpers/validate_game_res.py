class GameResultValidator:
    @staticmethod
    def validate_game_result(game_result):
        # Assuming game result format is "1-0", "0-1", or "0.5-0.5"
        parts = game_result.split("-")
        if len(parts) == 2:
            try:
                score1, score2 = map(float, parts)
                if score1 in [0, 0.5, 1] and score2 in [0, 0.5, 1]:
                    return True
                else:
                    return False
            except ValueError:
                return False
        else:
            return False