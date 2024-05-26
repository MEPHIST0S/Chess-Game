class Menu:
    def show_main_menu(self):
        print("Welcome to Chess Game!")
        print("Main Menu:")
        print("1 - Players")
        print("2 - Games")
        print("3 - Moves History")
        choice = input("Enter your choice: ")  # Get user input
        return choice  # Return the user's choice as a string