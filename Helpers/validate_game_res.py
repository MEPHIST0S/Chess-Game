class GameResultValidator:
    @staticmethod
    def validate_game_result(game_result):
        valid_results = ["1-0", "0-1", "0.5-0.5"]
        return game_result in valid_results