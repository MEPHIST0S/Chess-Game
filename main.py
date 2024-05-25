from Helpers.a_menu import Menu
from Helpers.b_players_sub import PlayersSubMenu

def main():
    main_menu = Menu()
    choice = main_menu.show_main_menu()

    if choice == '1':
        # Handle Players option
        handle_players_menu()
    elif choice == '2':
        # Handle Games option
        pass
    elif choice == '3':
        # Handle Moves History option
        pass
    elif choice == '4':
        # Handle Play option
        pass
    else:
        print("Invalid choice. Please select a valid option.")

def handle_players_menu():
    players_submenu = PlayersSubMenu()
    while True:
        players_submenu.show_players_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            players_submenu.show_players_list()
        elif choice == "2":
            players_submenu.add_player()
        elif choice == "3":
            players_submenu.search_player()
        elif choice == "4":
            players_submenu.filter_players()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()