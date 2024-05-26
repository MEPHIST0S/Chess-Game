from Entities.x_menu import Menu
from Entities.y_players_sub import PlayersSubMenu
from Entities.z_games_sub import GamesSubMenu
from Entities.zx_moves_sub import MovesSubMenu

main_menu = Menu()
players_submenu = PlayersSubMenu()
games_submenu = GamesSubMenu()
moves_submenu = MovesSubMenu()

def main():
    while True:
        choice = main_menu.show_main_menu()

        if choice == '1':
            # Handle Players option
            players_submenu.handle_players_menu()
        elif choice == '2':
            # Handle Games option
            games_submenu.handle_games_menu()
        elif choice == '3':
            # Handle Moves History option
            moves_submenu.handle_moves_menu()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()