#### Connecting to database
\c databasename  --- To connect database

EX: \c test
EX: \c test postgres local host 5432 

#### Expanded Display ON/OFF
\x

#### View the database
\i /path of folder/filename.sql

#### Creating Table
Creating a table named "person" with data like 
"id" which is self incremental and not null,
"first_name" with "VARCHAR(50)" to store upto 50 characters and is not null,
similarly the other fields like "last_name upto 50 characters", "gender upto 7 characters", "email upto 150 caharcters" and "date_of_birth " 

test=# CREATE TABLE person (
test(# id BIGSERIAL NOT NULL PRIMARY KEY,
test(# first_name VARCHAR(50) NOT NULL,
test(# last_name VARCHAR(50) NOT NULL,
test(# gender VARCHAR(7)NOT NULL,
test(# date_of_birth DATE NOT NULL,
test(# email VARCHAR(150) );

#### Insert query (Insert the data with their respective field in the table)
test=# INSERT INTO person (first_name, last_name, gender, date_of_birth, email)
test-# VALUES ('Jake', 'Jones', 'MALE', date '1990-12-13', 'jake@gmail.com');

#### Conditional Query
SELECT * FROM person ----select all from table

SELECT * FROM person ORDER BY country_of_birth; -----select all and ordered by country of birth or any field it contains

SELECT * FROM person ORDER BY country_of_birth DESC; -----select all and ordered by country of birth in "descending order"

SELECT * FROM person ORDER BY country_of_birth ASC; -----select all and ordered by country of birth in "ascending order"

#### DISTINCT
Select the distinct values from table for particular field

SELECT DISTINCT country_of_birth FROM person ORDER BY country_of_birth

#### WHERE,AND
Allows to filter the data on condition and "AND" allows to add more conditions

SELECT * FROM person WHERE gender = 'Female';
SELECT * FROM person WHERE gender = 'Female' AND country_of_birth = 'Poland';
SELECT * FROM person WHERE gender = 'Female' AND (country_of_birth = 'Poland' OR country_of_birth = 'Japan');

#### Comparison
Returns True/ False
SELECT 1=1; 
SELECT 1=2;
SELECT 1<2;
SELECT 1<>2; ---- not equal

#### LIMIT/FETCH,OFFSET
LIMIT ---- Limit the values to be displayed
OFFSET ---- Offset the values, so the values after it displays

SELECT * FROM person LIMIT 10;
SELECT * FROM person OFFSET 5 LIMIT 10;
SELECT * FROM person OFFSET 5 FETCH FIRST 5 ROW ONLY; ---- Fetch first 5 rows only

#### IN
Takes an arrays of values then return the query matching those values

SELECT * FROM person WHERE country_of_birth IN ('Poland','Japan','France'); ---- select person whose country_of_birth is Poland, Japan, France

#### BETWEEN
Select the data between two values

SELECT * FROM person WHERE date_of_birth BETWEEN DATE '2000-01-01' AND '2015-01-01'; ---select date between those two dates 

#### LIKE And ILIKE
LIKE returns output if it contains mentioned string

SELECT * FROM person WHERE email LIKE '%@wikimedia.org'; ---- Gives the email mentioned by address. The "%" refers to any character

SELECT * FROM person WHERE email LIKE '%@google.%';
SELECT * FROM person WHERE email LIKE '_____@%googl'; ---- Match by first (any number) spaces 
SELECT * FROM person WHERE country_of_birth ILIKE '%g'; ---- ILike ignores some pattern like small or large character

#### GROUP BY
It groups based on what column you selected,including count function and at what condition you want to group by

SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth;

#### GROUP BY HAVING
It is like putting a condition on group by and should be placed before order.

SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth HAVING COUNT(*)>5 ORDER BY country_of_birth; -------- Group by having count > 5

#### MAX, MIN, AVERAGE
SELECT MAX(price) FROM car; ----- Gives max price
SELECT MIN(price) FROM car; ----- Gives min price/value 
SELECT AVG(price) FROM car; ----- Gives average price/value
SELECT ROUND(AVG(price)) FROM car; ---- Round the values
SELECT make, model, MIN(PRICE) FROM car GROUP BY make, model ----- Group by make, model with minimum price

#### SUM
Gives sum of values
SELECT SUM(price) FROM car; ---- Sum of all available car prices

#### Basic arithmatic operators
SELECT 10+2 ------ Gives sum
SELECT 10^2 ------ Gives Square

#### ROUND
Rounding the values
SELECT make, model, price, ROUND(price*10,2) FROM car; ------ Rounding upto 2 digits

#### Alias
Rename to the particular column
SELECT make, model, price As original_price, ROUND(price*10,2) As discounted_price FROM car;

#### COALESCE
The COALESCE function accepts an unlimited number of arguments and it returns the first argument that is not null.
SELECT COALESCE(email,'Email not provide') FROM person;

#### NULLIF
It takes 2 values and compare them if they are equal or not. If equal then returns none and if they are unequal then returns 1st value

SELECT 10 / NULLIF(2,9); ----the output is 5 not an error

#### Timestamps And Dates 
SELECT NOW();------ gives present timestamp with date
SELECT NOW()::DATE; ----gives date only
SELECT NOW()::TIME; ----gives time
SELECT NOW() - INTERVAL '1 YEAR' ----- Subtract 1 year from current year

#### Extracting Fields From Timestamp
EXtracting the field from timestamp

SELECT EXTRACT(YEAR FROM NOW());
SELECT EXTRACT(DOW FROM NOW()); ------ Select day of the week

#### Age Function
Gives age as a new column based on the parameters 

SELECT first_name,last_name, gender, country_of_birth, date_of_birth, AGE(NOW(), date_of_birth) AS age FROM person;

#### Primary Key
Primary Key uniquely identifies the record in the table. If you want to add duplicate key you need to alter the table 

ALTER TABLE person DROP CONSTRAINT person_pkey; -----Alter the table and drop the person_key,so that you can add the duplicate row

#### Adding Primary Key
Delete the duplicate rows. Add the person with the details, then add the Primary Key.

DELETE FROM person WHERE id = 1; 
ALTER TABLE person ADD PRIMARY KEY (id);

#### Unique Constrain
Allows unique value for each column. Delete the duplicate one. Then alter table

ALTER TABLE person ADD CONSTRAINT unique_email_address UNIQUE (email); ---- Add unique email address

#### Check Constrains



#### DELETE
Used to delete a whole database or some specific information. So one should be careful while using it.
DELETE FROM person WHERE country_of_birth = 'Pakistan'; ----- Deletes everyone whose country of birth is Pakistan.

#### UPDATE
Allows to update one or multiple column based on where clause otherwise one can update whole data.

UPDATE person SET email = 'gunther@gmail.com' WHERE id = 132;
UPDATE person SET first_name = 'Abraham', last_name = 'Buttowski', email = 'buttowski@gmail.com' WHERE id = 831;

#### ON CONFLICT
Allows you to not update if there is an conflict situation arises or the person you want to update/insert ia already there. In this case it does not displays any error, shows insert 0,0. The id or any thing you are adding after 'on conflict' should be unique.

INSERT INTO person (id, first_name, last_name, email, gender, date_of_birth, country_of_birth) VALUES (113, 'Meryl', 'Harrowell', null, 'Female',DATE '2021-07-06', 'Indonesia') ON CONFLICT (id) DO NOTHING;

#### UPSERT
Allows you to update the fields.

INSERT INTO person (id, first_name, last_name, email, gender, date_of_birth, country_of_birth) VALUES (113, 'Patrizius', 'Hully', 'phullyqn@harvard.edu.uk', 'Male',DATE '2021-11-30', 'Indonesia') ON CONFLICT (id) DO UPDATE SET email=EXCLUDED.email; ---- Here we update phullyqn@harvard.edu to phullyqn@harvard.edu.uk

#### Foreign Keys, Joins and Relationship
Foreign keys are those whose having relationship(references) with other table matches the 'primary key' and 'the field type'.

#### Adding relationship between tables

UPDATE person SET car_id = 2 WHERE id = 1; ------ update car_id in person database Where id is 1.

#### JOIN
Joining Common fields

SELECT * FROM person JOIN car ON person.car_id = car.id ----- Gives intersection

#### left Join
Everything including left part with intersection is provided

SELECT * FROM person LEFT JOIN car ON person.car_id = car.id

#### Deleting Records with Foreign Key
You can not delete directly when there is foreign key Constrain. First you have to delete/update that id. You can not directly delete car.

UPDATE person SET car_id = 13 WHERE id = 9000; ---update the database
DELETE FROM person WHERE id = 9000; --- Delete id remove Foreign Key
DELETE FROM car WHERE id = 13; ------ Delete car

#### Exporting Query Result to CSV
Create a CSV file by using \copy(Query) To 'destination folder\filename.csv' DELIMITER ',' CSV HEADER; 

\copy (SELECT * FROM person LEFT JOIN car ON car.id = person.car_id) TO '/Users/gaura/Desktop/Postgres/result.csv' DELIMITER ',' CSV HEADER;

#### Serial and Sequences
SELECT nextval(person_id_seq'::regclass); ----- Gives next seuence value
ALTER SEQUENCE person_id_seq RESTART WITH 10; ---- Next value would be start with 10

#### Extension
List of available sequences
SELECT * FROM pg_available_extensions;

#### UUID
Guarantees unique identifier when it is generated

CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; ----- Create extension
SELECT uuid_generate_v4(); ----------Invoking

#### UUID As Primary Keys
UPDATE person SET car_uid = 'bd632624-37b1-45b9-9d78-0a6e3208852e' WHERE person_uid = 'a0bd419a-4592-4df3-9544-585e5ae9883a'; ------- updating car_uid

SELECT * FROM person LEFT JOIN car USING (car_uid);------ Can be used when primary key and foreign key are same





