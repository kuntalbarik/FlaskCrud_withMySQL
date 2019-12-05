# FlaskCrud_withMySQL
FlaskCrud_withMySQL,javascript

===================================================================================================================
video tutorial link--https://m.youtube.com/watch?v=Pu9XhFJduEw&list=PL1FgJUcJJ03vLZXbAFESDqGKBrDNgi-LG&index=2&t=0s
===================================================================================================================
MySQL schema

CREATE DATABASE flask_crud_students;
CREATE TABLE student_details (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(100) DEFAULT NULL,
  email_id varchar(100) DEFAULT NULL,
  mobile_no varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
