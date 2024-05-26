import mysql.connector
import datetime

from Helpers.connection import get_connection
from Helpers.cash_games import display_games_history

class CashPlayers:
    @staticmethod
    def display_players_table(self):
        try:
            # Connect to the database
            connection = get_connection()

            # Fetch players from the database
            cursor = connection.cursor()
            cursor.execute("SELECT player_id, name FROM players")
            players = cursor.fetchall()

            # Display players' ID and name table
            print("Player ID\tName")
            print("===================")
            for player in players:
                print(f"{player[0]}\t\t{player[1]}")

            # Close cursor and connection
            cursor.close()
            connection.close()
        except mysql.connector.Error as error:
            print(f"Error displaying players table: {error}")