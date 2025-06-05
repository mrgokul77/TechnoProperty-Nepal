
import datetime
from read import read_land_info
from operations import display_available_lands, display_unavailable_lands
from write import generate_invoice, rent_land_transaction, return_land_transaction

def start():
    while True:
        print("\n")
        print("                                  WELCOME TO TechnoProperty Nepal")
        print("                               *************************************")
        print("\nWhat would you like to do?")
        print("1. Rent a land")
        print("2. Return a land")
        print("3. Quit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            print("\nAvailable Lands:")
            display_available_lands()
            print("\nUnavailable Lands:")
            display_unavailable_lands()
            rent_land_transaction()
        elif choice == '2':
            print("\nAvailable Lands:")
            display_available_lands()
            print("\nUnavailable Lands:")
            display_unavailable_lands()
            return_land_transaction()
        elif choice == '3':
            print("Exiting.....")
            break
        else:
            print("Invalid choice! Please enter a valid number.")

if __name__ == "__main__":
    start()
