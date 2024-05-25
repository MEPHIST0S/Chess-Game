import mysql.connector
from Helpers.connection import get_connection

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
        name = input("Enter player name: ")
        rating = int(input("Enter player rating: "))
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO players (name, rating) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, rating))
        self.connection.commit()
        print("Successfully added player.")
        cursor.close()
        
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
        player_id = input("Enter Player ID to update: ")
        new_name = input("Enter new name: ")
        new_rating = input("Enter new rating: ")
        cursor = self.connection.cursor()
        cursor.execute("UPDATE players SET name = %s, rating = %s WHERE player_id = %s", (new_name, new_rating, player_id))
        self.connection.commit()
        cursor.close()
        print("Player data updated successfully.")

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