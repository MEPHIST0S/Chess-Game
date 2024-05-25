from connection import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS Players (player_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), rating INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Games (game_id INT AUTO_INCREMENT PRIMARY KEY, player1_id INT, player2_id INT, result VARCHAR(10), date_played DATE, FOREIGN KEY (player1_id) REFERENCES Players(player_id), FOREIGN KEY (player2_id) REFERENCES Players(player_id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Moves (move_id INT AUTO_INCREMENT PRIMARY KEY, game_id INT, move_number INT, move_text VARCHAR(10), FOREIGN KEY (game_id) REFERENCES Games(game_id))")

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_tables()