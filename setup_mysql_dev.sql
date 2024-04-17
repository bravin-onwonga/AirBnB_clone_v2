-- creates database if it doesn't exists
-- creates a new user with all priviledges to new db
-- grants select priviledge on perfomance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_Pwd#20';

GRANT ALL PRIVILEGES
ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

GRANT SELECT
ON performance_schema.*
TO 'hbnb_dev'@'localhost';
