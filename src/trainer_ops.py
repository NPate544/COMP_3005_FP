#trainer_ops
import json
from db_operations import db_connect, execute_query

@db_connect
def view_member_profile_by_trainer(conn):
    member_id = input("Enter the member's ID to view their profile: ")
    try:
        member_id = int(member_id)  # Convert input to int to match the ID's data type in the database
    except ValueError:
        print("Invalid member ID. Please enter a numeric ID.")
        return
    
    query = """
    SELECT member_id, name, email, health_metrics, fitness_goals
    FROM Members
    WHERE member_id = %s;
    """
    with conn.cursor() as cur:
        cur.execute(query, (member_id,))
        result = cur.fetchone()  # Fetch the single matching member profile
        if result:
            # Check if health_metrics and fitness_goals are in string format, if so, convert them to dict
            health_metrics = result[3] if isinstance(result[3], dict) else json.loads(result[3])
            fitness_goals = result[4] if isinstance(result[4], dict) else json.loads(result[4])
            
            print(f"Member ID: {result[0]}, Name: {result[1]}, Email: {result[2]}")
            print(f"Health Metrics: Weight - {health_metrics.get('weight')}, Height - {health_metrics.get('height')}")
            print(f"Fitness Goals: Goal - {fitness_goals.get('goal')}, Target - {fitness_goals.get('target')}")
        else:
            print("Member not found.")

@db_connect
def set_trainer_availability(conn, trainer_id):
    """Allow a trainer to set their availability."""
    print(f"Setting availability for Trainer ID: {trainer_id}")
    available_date = input("Enter the date you are available (YYYY-MM-DD): ")
    start_time = input("Enter the start time (HH:MM): ")
    end_time = input("Enter the end time (HH:MM): ")
    

    query = """
    INSERT INTO TrainerAvailability (trainer_id, available_date, start_time, end_time)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (trainer_id, available_date) DO UPDATE
    SET start_time = EXCLUDED.start_time, end_time = EXCLUDED.end_time;
    """
    with conn.cursor() as cur:
        cur.execute(query, (trainer_id, available_date, start_time, end_time))
        conn.commit()

        print("Availability set successfully.")


@db_connect
def view_member_profile(conn):
    """View a member's profile by their name or ID."""
    search_term = input("Enter the member's name or ID to view their profile: ")
    try:
        # Try to interpret the search term as an ID (integer)
        member_id = int(search_term)
        query = "SELECT member_id, name, email, health_metrics, fitness_goals FROM Members WHERE member_id = %s;"
        args = (member_id,)
    except ValueError:
        # If it's not an integer, interpret it as a name
        query = "SELECT member_id, name, email, health_metrics, fitness_goals FROM Members WHERE name LIKE %s;"
        args = (f"%{search_term}%",)

    with conn.cursor() as cur:
        cur.execute(query, args)
        results = cur.fetchall()
        if results:
            for result in results:
                # Print out the member details
                print(f"Member ID: {result[0]}, Name: {result[1]}, Email: {result[2]}, Health Metrics: {json.loads(result[3])}, Fitness Goals: {json.loads(result[4])}")
        else:
            print("No members found with that term.")
