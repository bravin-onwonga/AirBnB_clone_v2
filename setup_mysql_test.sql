-- creates database(hbnb_test_db) if it doesn't exists
-- creates a new user with all priviledges to the new db
-- grants select priviledge on perfomance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';

GRANT SELECT
ON performance_schema.*
TO 'hbnb_test'@'localhost';
