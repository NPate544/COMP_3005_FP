#main
from user_interface import initial_menu, user_menu
from member_ops import user_registration, login

def main():
    while True:
        choice = initial_menu()
        if choice == "1":
            user_registration()
        elif choice == "2":
            role, member_id, trainer_id, staff_id = login()
            if role:
                user_menu(role, member_id, trainer_id, staff_id)

            else:
                print("Exiting...")
                break  # Exit if login is not successful
        else:
            print("Invalid choice. Please try again.")

        # Ask to exit the application only after returning to the main menu.
        exit_choice = input("Do you want to exit the application? (yes/no): ").lower()
        if exit_choice == "yes":
            print("Thank you for using the Health and Fitness Club Management System.")
            break  # Break out of the while loop to exit the application



if __name__ == "__main__":
    main()
