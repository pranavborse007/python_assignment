# BUILDING DATABASE APPS WITH PostgreSQL and python.


#1 introduction to data 
# what is data = collection of information.
# datum = single piece of information
# Eg. data of a person = name , age , gender , DOB , nationality
# forms = text , numbers , media , etc


#2 introduction to database
# what  is base = in construction of house initially the basement is laid in an organized manner.
# data + base = DATABASE
# organized = tables by means of rows and columns
# can be easily accessed, managed and updated
# main purpose of database = to operate a large amount of information by storing , retriving and managing by
# many databases are available like. 
#1 MySQL
#2 ORACLE
#3 PostregreSQL
#4 MongoDB etc.


#3 introduction to Postregre SQL

# TYPES OF DATABASES:
# 1.HIERARCHICAL DATABASE
# 2.NoSQL DATABASE
# 3.OBJECT ORIENTED DATABASE
# 4.RELATIONAL DATABASE
# 5.NETWORK DATABASE


# 4.RELATIONAL DATABASE
# 4.1 categorised by the set of tables
# 4.2 SQL(structured query language)
# 4.3 acts as the application interference
# 4.4 easier to modify  ---->extending the database
#                       ---->joining the database
                    

# .PostregreSQL
#   object relational database:
#                       -->object oriented database + relational database
#                       -->similar to relational database
#                       -->object oriented database  -->object,classes and inheritance are supported
#   open source
#   Source code is available under PostregreSQL License 
#   Building of commercial apps



#5 creating a database
# 1. \l
# 2. create database demodb;
# postgres=# \l
# 3. postgres=# \c demodb
#  ----> now we connect the database demodb




#6 deleting database 
# 1. create database test;
# 2. demodb=# \l
# 3. demodb=# drop database test;
# 4. demodb=# \l




#7 creating table and adding data
# 1. student=# CREATE TABLE students(name text,number int,age int);
# 2. student=# \d                     note : we get a table/for show table
# 3. student=# INSERT INTO students(name,number,age) VALUES('Sam',12,20); 
#                                             note : we can insert/add any values in table
# 4. student=# INSERT INTO students(name,number,age) VALUES('Sam',12,20); 
#                                              note : we can insert/add new one values in table




#8 retriving data from database and deleting contents in the table

# retriving data from database :

# student=# SELECT * FROM students;                         note:here we can get values of table that we insert
# student=# SELECT name FROM students;                      note:retriving particular values from table
# student=# SELECT * FROM students WHERE number = 12;       note:retriving particular  complete rows that we mention.
 
# deleting contents from the table:
# student=# TRUNCATE TABLE students;                        note:delete complete values from the table and table gets empty.
# student=# \d
# student=# SELECT * FROM students;                         note:it gives empty table





#9 setting up virtualenv
# 1. created a folder of any name(visual studio)
# 2. in that folder (visual studio) create any (test.py) file of python
# 3. now open command prompt 
# 4. in command prompt :cd desktop               note :then enter
# 5. after enter , then: cd visual studio        note:cd (enter folder name) and then enter again
# 6. after enter , then:pip install virtualenv   note:enter    then  virtualenv get install    
# 7. after enter , then:virtualenv env           note:enter   then, virtualenv get setup
#  AFTER YOUR VIRTUALENV GETS INSTALLED AND SETUP COMPLETELY FOR ACTIVATING AND DEACTIVATING 
#  FOLLOWING STEPS ARE FOLLOWED 

# 8. after enter , then:cd env                   note:enter
# 9. after enter , then:cd scripts               note:enter
# 10. after enter , then:activate                 note:enter    then virtualenv gets activated
# 11. for going back to visual studio :cd..
# 12. for going back to visual studio :cd..
# 13. after that to getting output of file of folder that we activate:python test.py
#                                       note:python (file name.py) we get output that have typed in file
# 14. for deactivate virtualenv :deactivate         note:typed deactivate and enter
# for again activate virtualenv type respectivelt:cd env
#                                                :cd scripts
#                                                :activate
# for getting output in visual studio's terminal activte virtualenv
# then select new terminal and typed in terminal :python test.py    note:type :python (file name.py )




#10 installing psycopg2
# for installing psycopg2 acivate first virtualenv and then 
# for again activate virtualenv type respectivelt:cd env
#                                                :cd scripts
#                                                :activate
# and then go to (env) visual studio :cd..
#                       again  :cd..
# 1. for installing psycopg2   :pip install psycopg2==2.9.7




#11 connecting to database
# 1.in test.py = import psycopg2
#              = connect = psycopg2.connect() 




