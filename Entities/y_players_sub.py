import mysql.connector
import datetime

from Helpers.connection import get_connection
from Helpers.cash_games import display_games_history
from Helpers.cash_players import CashPlayers

from Helpers.validate_player import PlayerValidator
from Helpers.validate_game_res import GameResultValidator
from Helpers.validate_date import DateValidator
from Helpers.validate_player_name import ValidatingPlayerName
from Helpers.validate_player_rating import ValidatingPlayerRating

class PlayersSubMenu:
    def __init__(self):
        # Initialize the database connection
        self.connection = get_connection()

    def show_players_menu(self):
        # Code to display the players submenu
        print("Players Menu:")
        print("1 - Players List")
        print("2 - Add Player")
        print("3 - Search Player")
        print("4 - Filter")
        print("5 - Update Player Data")
        print("6 - Delete Player")
        print("7 - Exit")

    def show_players_list(self):
        # Code to fetch and display the list of players from the database
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM players")
        players = cursor.fetchall()
        print("List of Players:")
        for player in players:
            print(player)
        cursor.close()

        # Prompt the user to type 'exit' to return back to Player Sub-Menu
        while True:
            exit_input = input("Type 'Exit' to return back to Player Sub-Menu: ")
            if exit_input.lower() == "exit":
                break
            else:
                print("Invalid Command")
                
    def add_player(self):
        # Prompt the user to enter the player's name
        while True:
            name = input("Enter Name: ")
            if not name.isalpha():
                print("Invalid input. Please enter a valid name.")
            else:
                break

        # Prompt the user to enter the player's rating
        while True:
            rating = input("Enter Rating (0-10000): ")
            if not rating.isdigit():
                print("Invalid input. Please enter a valid rating.")
            elif not (0 <= int(rating) <= 10000):
                print("Invalid rating. Rating must be between 0 and 10000.")
            else:
                break

        # Add the player to the database
        self.add_player_to_table(name, int(rating))
        print("Player added successfully.")
    
    def add_player_to_table(self, name, rating):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            # SQL query to insert the player into the database
            insert_query = "INSERT INTO players (name, rating) VALUES (%s, %s)"
            player_data = (name, rating)

            # Execute the query
            cursor.execute(insert_query, player_data)
            connection.commit()

            print("Player added successfully.")

        except mysql.connector.Error as error:
            print(f"Error adding player: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        
    def search_player(self):
        while True:
            name = input("Enter Name: ")
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM players WHERE name = %s", (name,))
            player = cursor.fetchone()
            if player:
                print(f"Player found: ID - {player[0]}, Name - {player[1]}, Rating - {player[2]}")
            else:
                print("Player not found.")
            cursor.close()

            while True:
                option = input("1 - Search Again, 2 - Exit: ")
                if option == "1":
                    break  # Break inner loop to prompt for a new search
                elif option == "2":
                    return  # Exit the search player function
                else:
                    print("Invalid input. Please select a valid option.")

    def filter_players(self):
        print("Filter Menu:")
        print("1 - More")
        print("2 - Less")
        choice = input("Enter your choice: ")
        if choice == "1":
            threshold = int(input("Enter Rating Threshold: "))
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM players WHERE rating > %s", (threshold,))
            players = cursor.fetchall()
            print("Players with rating more than", threshold, ":")
            for player in players:
                print(player)
            cursor.close()
        elif choice == "2":
            threshold = int(input("Enter Rating Threshold: "))
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM players WHERE rating < %s", (threshold,))
            players = cursor.fetchall()
            print("Players with rating less than", threshold, ":")
            for player in players:
                print(player)
            cursor.close()
        else:
            print("Invalid choice.")

        while True:
            exit_input = input("Type 'Exit' to return back to Players Sub-Menu: ")
            if exit_input.lower() == "exit":
                break
            else:
                print("Invalid input. Please type 'Exit' to return to the Player Sub-Menu.")
                
    def update_player(self):
        # Display the updated list of players after the update operation
        self.show_players_list()

        # Prompt user to enter player ID to update
        player_id = input("Enter Player ID to update: ")

        # Check if the entered ID is valid
        if not PlayerValidator.validate_player_id(player_id):
            print("Invalid player ID. Please enter a valid Player ID.")
            return

        # Prompt user to enter new name
        new_name = input("Enter new name: ")
        # Validate new name
        if not ValidatingPlayerName.validate_name(new_name):
            print("Invalid name. Please enter letters only.")
            return

        # Prompt user to enter new rating
        new_rating = input("Enter new rating: ")
        # Validate new rating
        if not ValidatingPlayerRating.validate_rating(new_rating):
            print("Invalid rating. Rating must be an integer between 0 and 10000.")
            return

        # Update player data in the database
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE players SET name = %s, rating = %s WHERE player_id = %s", (new_name, new_rating, player_id))
            self.connection.commit()
            print("Player data updated successfully.")

        except mysql.connector.Error as error:
            print(f"Error updating player data: {error}")

        finally:
            if cursor:
                cursor.close()

    def delete_player(self):
        player_id = input("Enter Player ID to delete: ")
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM players WHERE player_id = %s", (player_id,))
        self.connection.commit()
        cursor.close()
        print("Player deleted successfully.")

        # Reset auto-increment value
        reset_auto_increment_query = "ALTER TABLE players AUTO_INCREMENT = 1;"
        cursor = self.connection.cursor()
        cursor.execute(reset_auto_increment_query)
        self.connection.commit()
        cursor.close()              

    def exit_menu(self):
        print("Exiting Players Sub-Menu.")
        return

    def handle_players_menu(self):
        while True:
            self.show_players_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.show_players_list()
                exit_input = input("Type 'Exit' to Confirm: ")
                if exit_input.lower() == "exit":
                    continue
                else:
                    print("Invalid input. Returning to Player Sub-Menu.")
            elif choice == "2":
                self.add_player()
            elif choice == "3":
                self.search_player()
            elif choice == "4":
                self.filter_players()
            elif choice == "5":
                self.update_player()
            elif choice == "6":
                self.delete_player()
            elif choice == "7":
                self.exit_menu()
                break
            else:
                print("Invalid choice. Please select a valid option.")