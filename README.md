# Summary of the Project
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

# Tasks
1. Create a star schema optimized for queries on song play analysis. 
2. Create fact and dimension tables for ETL purposes.
3. Build ETL pipeline that automates the workflow of extracting data from json sources and insert them to the database.

# Star Schema design
### Fact Table: 
songplays
- Records: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent.
- Primary Key: songplay_id.
- Foreign Keys: start_time, user_id, song_id, artist_id.

### Dimension Tables:

users
* Records: first_name, last_name, gender, level.
* Primary key: user_id.

songs
* Records: title, artist_id, year, duration.
* Primary key: song_id.

artists
* Records: artist_name, artist_location, artist_latitude, artist_longitude.
* Primary key: artist_id.

time
* Records: hour, day, week, month, year, weekday.
* Primary key: start_time. 

# Data Explanation
* test.ipynb: displays the first few rows of each table to let you check your database.
* create_tables.py: drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
* etl.ipynb: reads and processes a single file from song_data and log_data then loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
* etl.py: reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
* sql_queries.py: contains all sql queries, and is imported into the last three files above.

# Requirements:
1. In order to create locally a database in PostgreSQL you will need to install PostgreSQL(pgAdmin4 for GUI) on your local machine. 
2. The ETL.py code is designed based on Python3 with pandas, Numpy and psycopg2 libraries, therfore make sure you have them before you run the code.
3. In order to iterate over files in python you will need os and glob modules (if they don't come with the default Python3 libraries).
4. Download the data repository and all source code on your local machine

# How to run:
1. Make sure that you have all requirements to make the code executable.
2. Run the following command on the terminal to create the database and tables 
    "python create_tables.py".
3. Run ETL source code to extract and inserts the data from json files to tables
    "python etl.py".
4. Tables can be checked in "test.ipynb" to look at the tables

    