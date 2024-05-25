import mysql.connector
from Helpers.connection import get_connection
import datetime

class GamesSubMenu:
    def __init__(self):
        self.connection = get_connection()

    def show_games_menu(self):
        # Display the games submenu options
        print("Games Menu:")
        print("1 - Games History")
        print("2 - Filter")
        print("3 - Exit")

    def show_games_history(self):
        # Code to display games history
        cursor = self.connection.cursor()
        cursor.execute("SELECT g.game_id, p1.name as player1_name, p2.name as player2_name, g.result, g.date_played FROM games g JOIN players p1 ON g.player1_id = p1.player_id JOIN players p2 ON g.player2_id = p2.player_id")
        games = cursor.fetchall()
        cursor.close()

        # Define headers
        headers = ["Game ID", "Player 1 Name", "Player 2 Name", "Result", "Date"]
        header_format = "{:<10} {:<20} {:<20} {:<8} {:<12}"
        row_format = "{:<10} {:<20} {:<20} {:<8} {:<12}"

        # Print headers
        print(header_format.format(*headers))
        print("="*70)  # Separator line

        # Print each game in a formatted manner
        for game in games:
            game_id, player1_name, player2_name, result, date = game
            date_str = date.strftime("%Y-%m-%d") if isinstance(date, datetime.date) else str(date)
            print(row_format.format(game_id, player1_name, player2_name, result, date_str))

        # Loop to handle 'Exit' input
        while True:
            exit_input = input("Type 'Exit' to return back to Games Sub-Menu: ")
            if exit_input.lower() == "exit":
                return  # Return to Games Sub-Menu
            else:
                print("Invalid Command. Please type 'Exit' to return back to Games Sub-Menu.")

    def filter_games(self):
        print("Filter Games:")
        print("1 - Wins")
        print("2 - Draws")
        filter_choice = input("Enter your choice: ")
        
        if filter_choice == "1":
            self.show_filtered_games("wins")
        elif filter_choice == "2":
            self.show_filtered_games("draws")
        else:
            print("Invalid choice. Please select a valid option.")

    def show_filtered_games(self, filter_type):
        cursor = self.connection.cursor()
        
        if filter_type == "wins":
            cursor.execute("SELECT g.game_id, p1.name as player1_name, p2.name as player2_name, g.result, g.date_played FROM games g JOIN players p1 ON g.player1_id = p1.player_id JOIN players p2 ON g.player2_id = p2.player_id WHERE g.result IN ('1-0', '0-1')")
        elif filter_type == "draws":
            cursor.execute("SELECT g.game_id, p1.name as player1_name, p2.name as player2_name, g.result, g.date_played FROM games g JOIN players p1 ON g.player1_id = p1.player_id JOIN players p2 ON g.player2_id = p2.player_id WHERE g.result = '0.5-0.5'")
        
        games = cursor.fetchall()
        
        print(f"{'Game ID':<10} {'Player 1 Name':<20} {'Player 2 Name':<20} {'Result':<8} {'Date':<12}")
        print("=" * 70)
        
        for game in games:
            game_id, player1_name, player2_name, result, date = game
            date_str = date.strftime("%Y-%m-%d") if isinstance(date, datetime.date) else str(date)
            print(f"{game_id:<10} {player1_name:<20} {player2_name:<20} {result:<8} {date_str:<12}")
        
        while True:
            exit_input = input("Type 'Exit' to return back to Games Sub-Menu: ")
            if exit_input.lower() == "exit":
                break
            else:
                print("Invalid input. Please type 'Exit' to return.")

    def handle_games_menu(self):
        while True:
            self.show_games_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.show_games_history()
            elif choice == "2":
                self.filter_games()
            elif choice == "3":
                return  # Exit to main menu
            else:
                print("Invalid choice. Please select a valid option.") 