#member_ops
import json
from datetime import datetime
from db_operations import execute_query, db_connect

def user_registration():
    print("Registering a new user. Please provide the following details:")
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")  # Prompt for password

    print("\nEnter health metrics in the following format:")
    print("Weight (in kg), Height (in cm)")
    print("Example: 70, 175")
    health_metrics_input = input("Enter weight and height: ")
    weight, height = health_metrics_input.split(',')
    health_metrics = json.dumps({"weight": weight.strip(), "height": height.strip()})

    print("\nEnter fitness goals in the following format:")
    print("Goal (lose weight/gain muscle/etc), Target (specific target)")
    print("Example: lose weight, 65")
    fitness_goals_input = input("Enter goal and target: ")
    goal, target = fitness_goals_input.split(',')
    fitness_goals = json.dumps({"goal": goal.strip(), "target": target.strip()})

    # Insert the new user into the Members table
    query_members = """INSERT INTO Members (name, email, health_metrics, fitness_goals, registration_date)
                       VALUES (%s, %s, %s, %s, %s);"""
    execute_query(query_members, (name, email, health_metrics, fitness_goals, datetime.now().date()))
    
    # Insert the new user's authentication details (including password) into the UserAuthentication table
    query_auth = "INSERT INTO UserAuthentication (email, password_hash, user_role) VALUES (%s, %s, 'member');"
    execute_query(query_auth, (email, password))  # Password is stored directly without hashing

    print("Member registered successfully. You can now log in.")


def update_member_profile(member_id):
    member_id = input("Enter member ID: ")

    print("\nUpdate health metrics (leave blank to skip):")
    print("Weight (in kg), Height (in cm)")
    print("Example: 70, 175")
    health_metrics_input = input("Enter weight and height: ")
    if health_metrics_input:
        weight, height = health_metrics_input.split(',')
        health_metrics = json.dumps({"weight": weight.strip(), "height": height.strip()})
        query = "UPDATE Members SET health_metrics = %s WHERE member_id = %s;"
        execute_query(query, (health_metrics, member_id))

    print("\nUpdate fitness goals (leave blank to skip):")
    print("Goal (lose weight/gain muscle/etc), Target (specific target)")
    print("Example: lose weight, 65")
    fitness_goals_input = input("Enter goal and target: ")
    if fitness_goals_input:
        goal, target = fitness_goals_input.split(',')
        fitness_goals = json.dumps({"goal": goal.strip(), "target": target.strip()})
        query = "UPDATE Members SET fitness_goals = %s WHERE member_id = %s;"
        execute_query(query, (fitness_goals, member_id))


def display_member_dashboard(member_id):
    member_id = input("Enter member ID: ")
    query = "SELECT name, health_metrics, fitness_goals FROM Members WHERE member_id = %s;"
    results = execute_query(query, (member_id,), fetch=True)
    for result in results:
        print(f"Name: {result[0]}, Health Metrics: {result[1]}, Fitness Goals: {result[2]}")


def schedule_personal_training_session(member_id):
    member_id = input("Enter member ID: ")
    trainer_id = input("Enter trainer ID: ")
    schedule = input("Enter schedule (YYYY-MM-DD HH:MM:SS): ")
    # Add validation for trainer availability here
    query = "INSERT INTO PersonalTrainingSessions (member_id, trainer_id, schedule) VALUES (%s, %s, %s);"
    execute_query(query, (member_id, trainer_id, schedule))


@db_connect
def add_member_feedback(conn, member_id):
    print("Provide feedback for a class you attended.")
    class_id = input("Enter the class ID: ")
    rating = input("Enter your rating (1-5): ")
    comments = input("Enter your comments: ")
    feedback_date = datetime.now().strftime('%Y-%m-%d')

    query = """
    INSERT INTO Feedback (member_id, class_id, trainer_id, rating, comments, feedback_date)
    VALUES (%s, %s, (SELECT trainer_id FROM Classes WHERE class_id = %s), %s, %s, %s);
    """
    with conn.cursor() as cur:
        cur.execute(query, (member_id, class_id, class_id, rating, comments, feedback_date))
        conn.commit()
        print("Feedback submitted successfully.")

@db_connect
def manage_membership(conn, member_id):
    print("Available Membership Types:")
    cur = conn.cursor()
    cur.execute("SELECT type_id, type_name, duration_months, price FROM MembershipTypes;")
    memberships = cur.fetchall()
    for type_id, name, months, price in memberships:
        print(f"{type_id}. {name} - {months} months - ${price}")

    choice = input("Select the membership type ID you want to enroll in: ")
    payment_method = input("Enter your payment method (Credit Card/Bank Transfer): ")
    amount = next((price for type_id, name, months, price in memberships if str(type_id) == choice), None)

    if amount:
        query = """
        INSERT INTO Payments (member_id, type_id, payment_date, amount, payment_method)
        VALUES (%s, %s, CURRENT_DATE, %s, %s);
        """
        cur.execute(query, (member_id, choice, amount, payment_method))
        conn.commit()
        print("Membership enrolled successfully.")
    else:
        print("Invalid membership type selected.")

def sign_up():
    print("Sign up as a new member. Please provide the following details:")
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    # Health metrics and fitness goals are optional at sign up
    print("\nEnter health metrics in the following format:")
    print("Weight (in kg), Height (in cm) - you can skip this by pressing enter")
    print("Example: 70, 175")
    health_metrics_input = input("Enter weight and height: ")
    if health_metrics_input:
        weight, height = health_metrics_input.split(',')
        health_metrics = json.dumps({"weight": weight.strip(), "height": height.strip()})
    else:
        health_metrics = json.dumps({})
    
    print("\nEnter fitness goals in the following format:")
    print("Goal (lose weight/gain muscle/etc), Target (specific target) - you can skip this by pressing enter")
    print("Example: lose weight, 65")
    fitness_goals_input = input("Enter goal and target: ")
    if fitness_goals_input:
        goal, target = fitness_goals_input.split(',')
        fitness_goals = json.dumps({"goal": goal.strip(), "target": target.strip()})
    else:
        fitness_goals = json.dumps({})
    
    # Inserting member details into the Members table
    query_members = """INSERT INTO Members (name, email, health_metrics, fitness_goals, registration_date)
                       VALUES (%s, %s, %s, %s, %s);"""
    execute_query(query_members, (name, email, health_metrics, fitness_goals, datetime.now().date()))
    
    # Inserting user authentication details into the UserAuthentication table
    query_auth = "INSERT INTO UserAuthentication (email, password_hash, user_role) VALUES (%s, %s, 'member');"
    execute_query(query_auth, (email, password))
    
    print("Member registered successfully. You can now log in.")

def login():
    while True:
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        query = "SELECT user_role, member_id, trainer_id, staff_id FROM UserAuthentication WHERE email = %s AND password_hash = %s;"
        results = execute_query(query, (email, password), fetch=True)
        if results:
            print("Login successful.")
            return results[0][0], results[0][1], results[0][2], results[0][3]  # role, member_id, trainer_id, staff_id        else:
            print("Login failed. Please check your credentials.")
            retry = input("Do you want to try again? (yes/no): (ANY KEY TO MENU) ").lower()
            if retry != "yes":
                return None, None, None, None

