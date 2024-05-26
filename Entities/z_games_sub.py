import mysql.connector
import datetime

from Helpers.connection import get_connection
from Helpers.cash_games import display_games_history

from Helpers.validate_player import PlayerValidator
from Helpers.validate_game_res import GameResultValidator
from Helpers.validate_date import DateValidator
from Helpers.validate_game_id import GameIDValidator
from Helpers.validate_move import MovesValidation

class GamesSubMenu:
    def __init__(self):
        self.connection = get_connection()

    def show_games_menu(self):
        # Display the games submenu options
        print("Games Menu:")
        print("1 - Games History")
        print("2 - Filter")
        print("3 - Add Game")
        print("4 - Update Game")
        print("5 - Delete Game")
        print("6 - Exit")

    def show_games_history(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT g.game_id, p1.name as player1_name, p2.name as player2_name, g.result, g.date_played
            FROM games g
            JOIN players p1 ON g.player1_id = p1.player_id
            JOIN players p2 ON g.player2_id = p2.player_id
        """)
        games = cursor.fetchall()

        headers = ["Game ID", "Player 1 Name", "Player 2 Name", "Result", "Date"]
        header_format = "{:<10} {:<20} {:<20} {:<8} {:<12}"
        row_format = "{:<10} {:<20} {:<20} {:<8} {:<12}"

        print(header_format.format(*headers))
        print("="*70)

        for game in games:
            game_id, player1_name, player2_name, result, date = game
            date_str = date.strftime("%Y-%m-%d") if isinstance(date, datetime.date) else str(date)
            print(row_format.format(game_id, player1_name, player2_name, result, date_str))

            # Fetch and display moves for each game
            cursor.execute("SELECT move_text FROM moves WHERE game_id = %s ORDER BY move_number", (game_id,))
            moves = cursor.fetchall()
            moves_texts = [move[0] for move in moves]
            print(f"Moves: {', '.join(moves_texts)}")
        
        cursor.close()

        while True:
            exit_input = input("Type 'Exit' to return back to Games Sub-Menu: ")
            if exit_input.lower() == "exit":
                return
            else:
                print("Invalid Command. Please type 'Exit' to return back to Games Sub-Menu.")

    def filter_games(self):
        print("Filter Games:")
        print("1 - Wins")
        print("2 - Draws")
        print("3 - Data")
        filter_choice = input("Enter your choice: ")
        
        if filter_choice == "1":
            self.show_filtered_games("wins")
        elif filter_choice == "2":
            self.show_filtered_games("draws")
        elif filter_choice == "3":
            from_date = input("Enter From Date (YYYY-MM-DD): ")
            to_date = input("Enter To Date (YYYY-MM-DD): ")
            self.show_filtered_games("date", from_date, to_date)
        else:
            print("Invalid choice. Please select a valid option.")

    def show_filtered_games(self, filter_type, from_date=None, to_date=None):
        cursor = self.connection.cursor()
        
        if filter_type == "wins":
            cursor.execute("""
                SELECT g.game_id, p1.name as player1_name, p2.name as player2_name, g.result, g.date_played 
                FROM games g 
                JOIN players p1 ON g.player1_id = p1.player_id 
                JOIN players p2 ON g.player2_id = p2.player_id 
                WHERE g.result IN ('1-0', '0-1')
            """)
        elif filter_type == "draws":
            cursor.execute("""
                SELECT g.game_id, p1.name as player1_name, p2.name as player2_name, g.result, g.date_played 
                FROM games g 
                JOIN players p1 ON g.player1_id = p1.player_id 
                JOIN players p2 ON g.player2_id = p2.player_id 
                WHERE g.result = '0.5-0.5'
            """)
        elif filter_type == "date":
            cursor.execute("""
                SELECT g.game_id, p1.name as player1_name, p2.name as player2_name, g.result, g.date_played 
                FROM games g 
                JOIN players p1 ON g.player1_id = p1.player_id 
                JOIN players p2 ON g.player2_id = p2.player_id 
                WHERE g.date_played BETWEEN %s AND %s
            """, (from_date, to_date))

        games = cursor.fetchall()
        
        wins = 0
        draws = 0
        
        print(f"{'Game ID':<10} {'Player 1 Name':<20} {'Player 2 Name':<20} {'Result':<8} {'Date':<12}")
        print("=" * 70)
        
        for game in games:
            game_id, player1_name, player2_name, result, date = game
            date_str = date.strftime("%Y-%m-%d") if isinstance(date, datetime.date) else str(date)
            print(f"{game_id:<10} {player1_name:<20} {player2_name:<20} {result:<8} {date_str:<12}")
            
            if result in ('1-0', '0-1'):
                wins += 1
            elif result == '0.5-0.5':
                draws += 1
        
        if filter_type == "date":
            print(f"\nTotal games: {len(games)}")
            print(f"Wins: {wins}")
            print(f"Draws: {draws}")
        
        while True:
            exit_input = input("Type 'Exit' to return back to Games Sub-Menu: ")
            if exit_input.lower() == "exit":
                break
            else:
                print("Invalid input. Please type 'Exit' to return.")

    def add_game(self):
        
        self.display_players_table()
        
        player1_id = input("Enter Player 1 ID: ")
        player2_id = input("Enter Player 2 ID: ")
        game_result = input("Enter game result (1-0, 0-1, or 0.5-0.5): ")
        game_date = input("Enter game date (YYYY-MM-DD): ")
        
        new_game_id = self.add_game_to_table(player1_id, player2_id, game_result, game_date)
        
        if new_game_id:
            print("Adding moves for the game...")
            moves = []
            for i in range(1, 9):  # Assuming you want to add 8 moves
                move = input(f"Enter move {i} for the game: ")
                moves.append((new_game_id, move, i))
            self.add_moves_to_database(new_game_id, moves)
            print(f"Game added successfully with ID: {new_game_id}")

    def get_last_game_id(self):
            cursor = self.connection.cursor()
            cursor.execute("SELECT MAX(game_id) FROM games")
            max_game_id = cursor.fetchone()[0]
            cursor.close()
            return max_game_id if max_game_id is not None else 0

    def add_moves_for_game(self, game_id):
        print("Adding moves for the game...")
        moves = []
        for i in range(1, 9):  # Limiting to 8 moves per game
            move = input(f"Enter move {i} for the game: ")
            # Validate move format (You need to implement this)
            if not MovesValidation.validate_move(move):
                print("Invalid move format. Please enter a valid move.")
                continue
            moves.append((game_id, move))

        # Store moves in the database
        if moves:
            self.add_moves_to_database(moves)
            print("Moves added successfully.")

    def add_moves_to_database(self, game_id, moves):
        try:
            cursor = self.connection.cursor()
            insert_query = "INSERT INTO moves (game_id, move_text, move_number) VALUES (%s, %s, %s)"
            cursor.executemany(insert_query, moves)
            self.connection.commit()
            print("Moves added successfully.")
        except mysql.connector.Error as error:
            print(f"Error adding moves: {error}")
        finally:
            if self.connection.is_connected():
                cursor.close()

    def display_players_table(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT player_id, name FROM players")
        players = cursor.fetchall()
        cursor.close()

        # Define headers
        headers = ["Player ID", "Name"]
        header_format = "{:<12} {:<20}"
        row_format = "{:<12} {:<20}"

        # Print headers
        print(header_format.format(*headers))
        print("="*32)  # Separator line

        # Print each player's ID and name in a formatted manner
        for player in players:
            player_id, name = player
            print(row_format.format(player_id, name))

        return players
    
    def add_game_to_table(self, player1_id, player2_id, game_result, game_date):
        # Validate game result format
        if not GameResultValidator.validate_game_result(game_result):
            print("Invalid game result format. Please use format: '1-0', '0-1', or '0.5-0.5'.")
            return None  # Return None if validation fails

        # Validate game date
        if not DateValidator.validate_date(game_date):
            print("Invalid date format or value. Please use format: 'YYYY-MM-DD'.")
            return None  # Return None if validation fails

        # Fetch the next available game ID
        cursor = self.connection.cursor()
        cursor.execute("SELECT MAX(game_id) FROM games")
        max_game_id = cursor.fetchone()[0]
        new_game_id = max_game_id + 1 if max_game_id is not None else 1

        # Code to add the new game to the table
        insert_query = "INSERT INTO games (game_id, player1_id, player2_id, result, date_played) VALUES (%s, %s, %s, %s, %s)"
        game_data = (new_game_id, player1_id, player2_id, game_result, game_date)
        cursor.execute(insert_query, game_data)
        self.connection.commit()
        cursor.close()
        print(f"Game added successfully with ID: {new_game_id}")
        return new_game_id  # Return the new game ID

    def update_game(self):
        # Display a list of all games
        cursor = self.connection.cursor()
        display_games_history(cursor, self.connection)
        cursor.close()
    
        # Prompt the user to select a game to update
        while True:
            game_id_to_update = input("Enter the Game ID you want to update, or type 'Exit' to return to the Games Menu: ")

            # Check if the user wants to exit
            if game_id_to_update.lower() == 'exit':
                return

            # Validate game ID using the GameIDValidator
            if GameIDValidator.validate_game_id(game_id_to_update, self.connection):
                break
            else:
                print("Invalid Game ID. Please enter a valid Game ID.")

        # Prompt the user to enter the new result for the selected game
        while True:
            new_result = input("Enter the new result for the game (1-0, 0-1, or 0.5-0.5): ")

            # Validate the new result format using GameResultValidator
            if GameResultValidator.validate_game_result(new_result):
                break
            else:
                print("Invalid game result format. Please enter the result in the correct format.")

        # Update the game record in the database
        cursor = self.connection.cursor()
        update_query = "UPDATE games SET result = %s WHERE game_id = %s"
        update_data = (new_result, game_id_to_update)
        cursor.execute(update_query, update_data)
        self.connection.commit()
        cursor.close()
        
        print("Game updated successfully.")

    def delete_game(self):
        try:
            # Display a list of all games
            cursor = self.connection.cursor()
            display_games_history(cursor, self.connection)
            
            # Prompt the user to select a game to delete
            game_id_to_delete = input("Enter the Game ID you want to delete, or type 'Exit' to return to the Games Menu: ")

            # Check if the user wants to exit
            if game_id_to_delete.lower() == 'exit':
                cursor.close()
                return

            # Validate game ID
            if not game_id_to_delete.isdigit():
                print("Invalid game ID. Please enter a valid Game ID.")
                cursor.close()
                return

            # Delete the moves associated with the game
            delete_moves_query = "DELETE FROM moves WHERE game_id = %s"
            cursor.execute(delete_moves_query, (game_id_to_delete,))

            # Delete the game record from the database
            delete_query = "DELETE FROM games WHERE game_id = %s"
            cursor.execute(delete_query, (game_id_to_delete,))
            
            self.connection.commit()
            cursor.close()
            
            print("Game and associated moves deleted successfully.")
        except mysql.connector.Error as err:
            print("Error deleting game:", err)

    def handle_games_menu(self):
        while True:
            self.show_games_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.show_games_history()
            elif choice == "2":
                self.filter_games()
            elif choice == "3":
                self.add_game()
            elif choice == "4":
                self.update_game()
            elif choice == "5":
                self.delete_game()
            elif choice == "6":
                return  # Exit to main menu
            else:
                print("Invalid choice. Please select a valid option.")  