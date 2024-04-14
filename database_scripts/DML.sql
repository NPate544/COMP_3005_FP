-- Inserting into Members
INSERT INTO Members (name, email, health_metrics, fitness_goals, registration_date) VALUES
('John Doe', 'john.doe@example.com', '{"weight": 80, "height": 180}', '{"goal": "lose weight", "target": 75}', '2024-01-01'),
('Jane Smith', 'jane.smith@example.com', '{"weight": 65, "height": 165}', '{"goal": "gain muscle", "target": 5}', '2024-01-02');

-- Inserting into Trainers
INSERT INTO Trainers (name, availability) VALUES
('Alex Johnson', '{"monday": ["09:00-11:00", "13:00-15:00"], "wednesday": ["10:00-12:00"], "friday": ["14:00-16:00"]}'),
('Samantha Brown', '{"tuesday": ["09:00-11:00", "13:00-15:00"], "thursday": ["10:00-12:00"], "saturday": ["14:00-16:00"]}');

-- Inserting into AdminStaff
INSERT INTO AdminStaff (name) VALUES
('Mark Admin'),
('Linda Admin');

-- Inserting into Classes
INSERT INTO Classes (class_name, room_id, schedule, trainer_id) VALUES
('Yoga Basics', 1, '2024-04-15 09:00:00+00', 1),
('Advanced Cardio', 2, '2024-04-16 11:00:00+00', 2);

-- Inserting into PersonalTrainingSessions
INSERT INTO PersonalTrainingSessions (member_id, trainer_id, schedule) VALUES
(1, 1, '2024-04-17 09:00:00+00'),
(2, 2, '2024-04-18 11:00:00+00');

-- Inserting into Equipment
INSERT INTO Equipment (name, last_maintenance, status) VALUES
('Treadmill 1', '2024-03-01', 'Good'),
('Yoga Mats', '2024-01-15', 'Needs Replacement');

-- Inserting into RoomBookings
INSERT INTO RoomBookings (room_id, booking_date, start_time, end_time) VALUES
(1, '2024-04-15', '08:00', '10:00'),
(2, '2024-04-16', '10:00', '12:00');

-- Inserting into MembershipTypes
INSERT INTO MembershipTypes (type_name, duration_months, price) VALUES
('Standard Monthly', 1, 30.00),
('Premium Yearly', 12, 300.00);

-- Inserting into Payments
INSERT INTO Payments (member_id, type_id, payment_date, amount, payment_method) VALUES
(1, 1, '2024-01-01', 30.00, 'Credit Card'),
(2, 2, '2024-01-02', 300.00, 'Bank Transfer');

-- Inserting into ClassRegistrations
INSERT INTO ClassRegistrations (class_id, member_id, registration_date) VALUES
(1, 1, '2024-01-03'),
(2, 2, '2024-01-04');

-- Inserting into Feedback (Optional)
INSERT INTO Feedback (member_id, class_id, trainer_id, rating, comments, feedback_date) VALUES
(1, 1, 1, 5, 'Great class!', '2024-01-05'),
(2, 2, 2, 4, 'Very challenging but rewarding.', '2024-01-06');

-- Inserting into UserAuthentication (Optional)
INSERT INTO UserAuthentication (email, password_hash, user_role, member_id) VALUES
('john.doe@example.com', 'hp111', 'member', 1),
('jane.smith@example.com', 'hp112', 'member', 2);

