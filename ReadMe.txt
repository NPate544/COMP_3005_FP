

1. PREAMBLE:


	AUTHOR - NIRAJ PATEL - 101269614
	
	PURPOSE - Final Project -> Health and Fitness Club Management System for club members, trainers, and administrative staff using Postgres and Python scripting
	

	SOURCE FILES INCLUDED -  admin_ops.py, db_operations.py, main.py, member_ops.py, trainer_ops.py, user_interface.py

	SQL FILES INCLUDED - DDL.sql, DML.sql, test_email_validation_trigger.sql, test_price_change_trigger, triggers.sql  

	**NOTE: Video Demonstration Link in the END.  
	**NOTE: GitHub Link in the END -> VISIT LINK FIRST AND THEN PROCEED...
	
	DATE MODIFIED: 2024/04/13 - REV A   
	  
	
2. COMPLILATION COMMAND TO USE :


  - You shall find the above source files including the ReadME file.
  
  - there are NO compilation commands to run as you will be running 3 scripts based in the need.

  - However, make sure you have python and PostgreSql (PgAdmin4) installed.

	NOTE** - install the necessary package fro the script to run `pip install psycopg2`
	
	
3. LAUNCHING INSTRUCTIONS:

	1. Download the files (source code and the ReadME) or clone repository.
	
	2. open terminal and change working directory to where the files are kept
	


4. OPERATING INSTRUCTIONS:


	0. Open PgAdmin4 and create a database - since you will be running the scripts locally - MAKE SURE TO CHANGE THIS: (ESPECIALLY -> database, user and password);

		conn_params = {
		    "database": "Final_Project",
		    "user": "postgres",
		    "password": "postgres",
		    "host": "localhost",
		    "port": "5432"
		}


	A. Initialize the data schema:

		1. run `DDL.sql` in pgAdmin - This script will create the tables (INDEXES SETUP IN THE END OF DDL.)
		2. run `DML.sql` in pgAdmin - This script will populate some dummy data in the created tables 
		3. run `triggers.sql` in pgAdmin - This script will set up teh triggers for the created tables 
		2. You will see all the tables in the pgAdmin4 and be able to view the values.
 
	B. Test the CRUD App:

		1. run `python main.py`- This script will perform serveral operations (CRUD) on the existing tables.

		2. You will come across these options;

		Welcome to the Health and Fitness Club Management System
			1. Sign up
			2. Log in

		a. IF entereed 1; these messages will be shown -> simply input data to test. 

			Registering a new user. Please provide the following details:
			Enter name:
			Enter email:
			Enter password:

			Enter health metrics in the following format:
			Weight (in kg), Height (in cm)
			Example: 70, 175
			Enter weight and height:

			- Once this is done => successfull registration -> then you can log in with that id/pass.

		b. IF entereed 2; Use your credentials to login -> these messages will be shown -> simply input data to test. 
			
			**NOTE: These are member logins => below menu is only for members

			Login successful.

				1. Update Member Profile
    				2. Display Member Dashboard
    				3. Schedule Personal Training Session
    				4. Leave Feedback
    				5. Manage Membership	
    				0. Exit				

			- Perform any of those tasks to test (VIDEO DEMONSTRATES ALL FUNCTIONS)
			
		3. FOR "TRAINER" LOGINS; USE THE BELOW CREDENTIALS TO LOG IN;
			
			EMAIL: trainer@example.com
			PASSWORD: trainerpass

		- Upon using above credentials below menu will be seen

			Login successful.
			Trainer Menu:
			1. Set Availability
			2. View Member Profile
			0. Exit

		- Perform any of those tasks to test (VIDEO DEMONSTRATES ALL FUNCTIONS)

		4. FOR "ADMIN" LOGINS; USE THE BELOW CREDENTIALS TO LOG IN;
			
			EMAIL: admin@example.com
			PASSWORD: adminpass

		- Upon using above credentials below menu will be seen

			Login successful.

			1. Manage Room Bookings
    			2. Update Equipment Status
    			3. Manage Class Schedules
    			4. Process Payments
    			0. Exit
		
		- Perform any of those tasks to test (VIDEO DEMONSTRATES ALL FUNCTIONS)
			

		**NOTE: VIDEO Shows the code and database being modified based on the above segments being run.

		
	

		**EXTRA: TRIGGERS TESTING;

		- Run the two test queries;

		A. IF EXECUTED: `test_price_change_trigger.sql`;
			- It will change the price of membership to $35.00 This trigger will be logged in teh audits table.
			- call ROLLBACK; after verifying logging to revert changges
			- VIDEO DEMO SHOWS THIS.

		B. IF EXECUTED: `test_email_validation_trigger.sql`;
			- It will try to add a member with wrong email format and it will be flagged out in the display. It will rollback by itself here. 


 


	
VIDEO DEMONSTRATION LINK: https://youtu.be/e2jZq0dsEzI

GITHUB LINK: 




	   
