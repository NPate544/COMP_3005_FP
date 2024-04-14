-- test_price_change_trigger.sql
-- Purpose: Update the membership type price and verify audit logging

BEGIN;

-- Attempt to update the price
UPDATE MembershipTypes SET price = 35.00 WHERE type_id = 1;

-- Query the audit table to verify that the change has been logged
SELECT * FROM MembershipTypeAudit;

