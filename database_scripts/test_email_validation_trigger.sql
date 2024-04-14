-- test_email_validation_trigger.sql
-- Attempt to insert a user with an invalid email format
-- Note: This operation should fail and raise an exception, showing the trigger is working.
-- It's expected that running this will produce an error, which indicates success.
BEGIN;
INSERT INTO UserAuthentication (email, password_hash, user_role) VALUES ('invalidemail', 'password123', 'member');
ROLLBACK;