#user_interface

from member_ops import user_registration, update_member_profile, display_member_dashboard, schedule_personal_training_session, add_member_feedback, manage_membership, sign_up, login
from trainer_ops import set_trainer_availability, view_member_profile_by_trainer
from admin_ops import manage_room_bookings, update_equipment_status, manage_class_schedules, process_payments

def initial_menu():
    print("Welcome to the Health and Fitness Club Management System")
    print("1. Sign up")
    print("2. Log in")
    choice = input("Enter your choice (1 for Sign up, 2 for Log in): ")
    return choice

def user_menu(role, member_id=None, trainer_id=None, staff_id=None):
    if role == "member":
        while True:
            choice = member_menu(member_id)
            if choice == "1":
                update_member_profile(member_id)
            elif choice == "2":
                display_member_dashboard(member_id)
            elif choice == "3":
                schedule_personal_training_session(member_id)
            elif choice == "4":
                add_member_feedback(member_id)
            elif choice == "5":
                manage_membership(member_id)
            elif choice == "0":
                print("Returning to the main menu...")
                break
            else:
                print("Invalid choice. Please try again.")

    elif role == "trainer":
        trainer_menu(trainer_id)

    elif role == "admin":
        while True:
            choice = admin_menu()
            if choice == "1":
                manage_room_bookings()
            elif choice == "2":
                update_equipment_status()
            elif choice == "3":
                manage_class_schedules()
            elif choice == "4":
                process_payments()
            elif choice == "0":
                print("Returning to the main menu...")
                break  # Break out of the loop to allow exiting to the main menu
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Invalid role. Please try again.")

def main_menu(role):
    if role == "member":
        options = """
        1. Register User
        2. Update Member Profile
        3. Display Member Dashboard
        4. Schedule Personal Training Session
        0. Exit
        """
    elif role == "trainer":
        options = """
        1. View Member Profile
        0. Exit
        """
    elif role == "admin":
        options = """
        1. Manage Room Bookings
        2. Update Equipment Status
        3. Manage Class Schedules
        4. Process Payments
        0. Exit
        """
    else:
        options = "Invalid role selected."
    print(options)
    choice = input("Enter your choice: ")
    return choice


def member_menu(member_id):
    options = """
    1. Update Member Profile
    2. Display Member Dashboard
    3. Schedule Personal Training Session
    4. Leave Feedback
    5. Manage Membership
    0. Exit
    """
    print(options)
    return input("Enter your choice: ")


def trainer_menu(trainer_id):
    while True:
        print("Trainer Menu:")
        print("1. Set Availability")
        print("2. View Member Profile")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            set_trainer_availability(trainer_id)
        elif choice == "2":
            view_member_profile_by_trainer()
        elif choice == "0":
            print("Exiting trainer menu...")
            return  # Break out of the loop to allow exiting to the main menu
        else:
            print("Invalid choice. Please try again.")
    return  # This ensures that after breaking out of the loop, the function actually exits.


def admin_menu():
    options = """
    1. Manage Room Bookings
    2. Update Equipment Status
    3. Manage Class Schedules
    4. Process Payments
    0. Exit
    """
    print(options)
    return input("Enter your choice: ")


def main_menu(role):
    if role == "member":
        options = """
        1. Register User
        2. Update Member Profile
        3. Display Member Dashboard
        4. Schedule Personal Training Session
        0. Exit
        """
    elif role == "trainer":
        options = """
        1. View Member Profile
        0. Exit
        """
    elif role == "admin":
        options = """
        1. Manage Room Bookings
        2. Update Equipment Status
        3. Manage Class Schedules
        4. Process Payments
        0. Exit
        """
    else:
        options = "Invalid role selected."
    print(options)
    choice = input("Enter your choice: ")
    return choice
