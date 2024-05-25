from Helpers.a_menu import Menu
from Helpers.b_players_sub import PlayersSubMenu

main_menu = Menu()
players_submenu = PlayersSubMenu()

def main():
    choice = main_menu.show_main_menu()

    if choice == '1':
        # Handle Players option
        players_submenu.handle_players_menu()
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
    
    choice = main_menu.show_main_menu()

if __name__ == "__main__":
    main()