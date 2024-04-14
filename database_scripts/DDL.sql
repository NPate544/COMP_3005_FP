-- Members Table
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    health_metrics JSON NOT NULL,
    fitness_goals JSON NOT NULL,
    registration_date DATE NOT NULL
);

-- Trainers Table
CREATE TABLE Trainers (
    trainer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    availability JSON NOT NULL
);

-- Admin Staff Table
CREATE TABLE AdminStaff (
    staff_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Classes Table
CREATE TABLE Classes (
    class_id SERIAL PRIMARY KEY,
    class_name VARCHAR(255) NOT NULL,
    room_id INT NOT NULL,
    schedule TIMESTAMPTZ NOT NULL,
    trainer_id INT REFERENCES Trainers(trainer_id)
);

-- Personal Training Sessions Table
CREATE TABLE PersonalTrainingSessions (
    session_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Members(member_id),
    trainer_id INT REFERENCES Trainers(trainer_id),
    schedule TIMESTAMPTZ NOT NULL
);

-- Equipment Table
CREATE TABLE Equipment (
    equipment_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    last_maintenance DATE NOT NULL,
    status VARCHAR(50) NOT NULL
);

-- Room Bookings Table
CREATE TABLE RoomBookings (
    booking_id SERIAL PRIMARY KEY,
    room_id INT NOT NULL,
    booking_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

-- Membership Types Table
CREATE TABLE MembershipTypes (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL,
    duration_months INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Payments Table
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Members(member_id),
    type_id INT REFERENCES MembershipTypes(type_id),
    payment_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50)
);

-- Class Registrations Table
CREATE TABLE ClassRegistrations (
    registration_id SERIAL PRIMARY KEY,
    class_id INT REFERENCES Classes(class_id),
    member_id INT REFERENCES Members(member_id),
    registration_date DATE NOT NULL
);

-- Feedback Table (Optional)
CREATE TABLE Feedback (
    feedback_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Members(member_id),
    class_id INT REFERENCES Classes(class_id),
    trainer_id INT REFERENCES Trainers(trainer_id),
    rating INT CHECK(rating >= 1 AND rating <= 5),
    comments TEXT,
    feedback_date DATE NOT NULL
);

-- Trainers avail. table
CREATE TABLE TrainerAvailability (
    trainer_id INT,
    available_date DATE,
    start_time TIME,
    end_time TIME,
    PRIMARY KEY (trainer_id, available_date),
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id)
);

-- User Authentication Table (Optional)
CREATE TABLE UserAuthentication (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    user_role VARCHAR(50) NOT NULL, -- E.g., 'member', 'trainer', 'admin'
    member_id INT NULL REFERENCES Members(member_id), -- NULL if not a member
    trainer_id INT NULL REFERENCES Trainers(trainer_id), -- NULL if not a trainer
    staff_id INT NULL REFERENCES AdminStaff(staff_id) -- NULL if not admin staff
);

-- Audit Table Creation
CREATE TABLE MembershipTypeAudit (
    audit_id SERIAL PRIMARY KEY,
    type_id INT NOT NULL,
    previous_price DECIMAL(10, 2),
    new_price DECIMAL(10, 2),
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES MembershipTypes(type_id)
);

-- Indexes for faster search
CREATE INDEX idx_member_email ON Members(email);
CREATE INDEX idx_trainer_name ON Trainers(name);
CREATE INDEX idx_class_schedule ON Classes(schedule);