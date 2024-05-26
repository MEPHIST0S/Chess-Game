import datetime

def display_games_history(cursor, connection):
    cursor.execute("SELECT g.game_id, p1.name as player1_name, p2.name as player2_name, g.result, g.date_played FROM games g JOIN players p1 ON g.player1_id = p1.player_id JOIN players p2 ON g.player2_id = p2.player_id")
    games = cursor.fetchall()

    # Define headers
    headers = ["Game ID", "Player 1 Name", "Player 2 Name", "Result", "Date"]
    header_format = "{:<10} {:<20} {:<20} {:<8} {:<12}"
    row_format = "{:<10} {:<20} {:<20} {:<8} {:<12}"

    # Print headers
    print(header_format.format(*headers))
    print("=" * 70)  # Separator line

    # Print each game in a formatted manner
    for game in games:
        game_id, player1_name, player2_name, result, date = game
        date_str = date.strftime("%Y-%m-%d") if isinstance(date, datetime.date) else str(date)
        print(row_format.format(game_id, player1_name, player2_name, result, date_str))