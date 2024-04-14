#admin_operations
from db_operations import execute_query

def manage_room_bookings():
    action = input("Do you want to (A)dd or (D)elete a booking? [A/D]: ").upper()
    if action == 'A':
        room_id = input("Enter room ID: ")
        booking_date = input("Enter booking date (YYYY-MM-DD): ")
        start_time = input("Enter start time (HH:MM): ")
        end_time = input("Enter end time (HH:MM): ")
        query = "INSERT INTO RoomBookings (room_id, booking_date, start_time, end_time) VALUES (%s, %s, %s, %s);"
        execute_query(query, (room_id, booking_date, start_time, end_time))
    elif action == 'D':
        booking_id = input("Enter booking ID to delete: ")
        query = "DELETE FROM RoomBookings WHERE booking_id = %s;"
        execute_query(query, (booking_id,))

def update_equipment_status():
    equipment_id = input("Enter equipment ID: ")
    status = input("Enter new status: ")
    query = "UPDATE Equipment SET status = %s WHERE equipment_id = %s;"
    execute_query(query, (status, equipment_id))

def manage_class_schedules():
    class_id = input("Enter class ID to update schedule: ")
    new_schedule = input("Enter new schedule (YYYY-MM-DD HH:MM:SS): ")
    query = "UPDATE Classes SET schedule = %s WHERE class_id = %s;"
    execute_query(query, (new_schedule, class_id))

def process_payments():
    member_id = input("Enter member ID for payment: ")
    amount = input("Enter payment amount: ")
    payment_method = input("Enter payment method: ")
    query = "INSERT INTO Payments (member_id, amount, payment_method, payment_date) VALUES (%s, %s, %s, CURRENT_DATE);"
    execute_query(query, (member_id, amount, payment_method))


