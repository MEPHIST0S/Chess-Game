from connection import get_connection

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
        print("5 - Exit")

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
                self.exit_menu()
                break
            else:
                print("Invalid choice. Please select a valid option.")
                
    def add_player(self):
        # Code to add a new player
        pass

    def search_player(self):
        # Code to search for a player
        pass

    def filter_players(self):
        # Code to filter players based on criteria
        pass

    def exit_menu(self):
        # Return to the main menu
        return