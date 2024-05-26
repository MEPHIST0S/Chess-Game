import mysql.connector
import datetime

from Helpers.connection import get_connection
from Helpers.validate_player import PlayerValidator
from Helpers.validate_game_res import GameResultValidator
from Helpers.validate_date import DateValidator
from Helpers.cash_games import display_games_history

class MovesSubMenu:
    def __init__(self):
        self.connection = get_connection()

    def show_moves_menu(self):
        # Display the moves submenu options
        print("Moves History Menu:")
        print("1 - All Moves")
        print("2 - Specific Game Moves")
        print("3 - Exit")

    def show_all_moves(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT move_id, game_id, move_text FROM moves")
            moves = cursor.fetchall()
            if moves:
                print("All Moves:")
                print("Move ID | Game ID | Move Text")
                for move in moves:
                    print("{:<8} | {:<8} | {:<10}".format(move[0], move[1], move[2]))
            else:
                print("No moves found.")
        except mysql.connector.Error as err:
            print("Error fetching moves:", err)
        finally:
            cursor.close()

    def show_specific_game_moves(self):
        cursor = self.connection.cursor()
        try:
            # Display games table
            display_games_history(cursor, self.connection)
            game_id = input("Choose Game ID: ")
            
            # Fetch and display moves for the selected game
            cursor.execute("SELECT move_id, game_id, move_text FROM moves WHERE game_id = %s", (game_id,))
            moves = cursor.fetchall()
            if moves:
                print(f"Moves for Game ID {game_id}:")
                print("Move ID | Game ID | Move Text")
                for move in moves:
                    print("{:<8} | {:<8} | {:<10}".format(move[0], move[1], move[2]))
            else:
                print("No moves found for the selected game.")
        except mysql.connector.Error as err:
            print("Error fetching moves:", err)
        finally:
            cursor.close()

    def handle_moves_menu(self):
        while True:
            self.show_moves_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.show_all_moves()
            elif choice == "2":
                self.show_specific_game_moves()
            elif choice == "3":
                print("Exiting Moves History Menu.")
                break
            else:
                print("Invalid choice. Please select a valid option.")