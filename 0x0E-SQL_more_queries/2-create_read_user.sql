--- A script that creates a database
CREATE IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
CREATE IF NOT EXISTS DATABASE 'hbtn_0d_2';
GRANT SELECT ON 'hbtn_0d_2' TO 'user_0d_2'@'localhost';
