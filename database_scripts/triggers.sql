-- Trigger to log changes in membership type prices
-- Trigger Function for logging price changes
CREATE OR REPLACE FUNCTION log_membership_type_change()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.price IS DISTINCT FROM NEW.price THEN
        INSERT INTO MembershipTypeAudit (type_id, previous_price, new_price)
        VALUES (OLD.type_id, OLD.price, NEW.price);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger Definition
CREATE TRIGGER trigger_membership_type_change
BEFORE UPDATE ON MembershipTypes
FOR EACH ROW
WHEN (OLD.price IS DISTINCT FROM NEW.price)
EXECUTE FUNCTION log_membership_type_change();

-- Trigger to validate email format in UserAuthentication
CREATE OR REPLACE FUNCTION validate_email_format()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.email NOT LIKE '%@%.%' THEN
        RAISE EXCEPTION 'Invalid email format for %', NEW.email;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_validate_email
BEFORE INSERT OR UPDATE ON UserAuthentication
FOR EACH ROW
EXECUTE FUNCTION validate_email_format();