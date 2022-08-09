-- A script that creates table called first_table in the current database in the MySQL server.
-- The database name will be passed as an argument of the mysql command
-- The script should not fail if the table first_table already exists.
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	NAME VARCHAR(256)
);
