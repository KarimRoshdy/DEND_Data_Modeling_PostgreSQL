# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
songplay_id SERIAL NOT NULL,
start_time TIMESTAMP NOT NULL REFERENCES time(start_time),
user_id  INT NOT NULL REFERENCES users(user_id),
level VARCHAR(40),
song_id VARCHAR(100) REFERENCES songs(song_id),
artist_id VARCHAR(100) REFERENCES artists(artist_id),
session_id INT NOT NULL,
location VARCHAR(150),
user_agent VARCHAR(250),
PRIMARY KEY (songplay_id))
""")


user_table_create = ("""CREATE TABLE IF NOT EXISTS users(
user_id INT NOT NULL, 
first_name VARCHAR(50), 
last_name VARCHAR(50),
gender VARCHAR(10), 
level VARCHAR(50),
PRIMARY KEY (user_id))
""")

song_table_create = ("""CREATE TABLE  IF NOT EXISTS songs(
song_id VARCHAR(100)NOT NULL ,
title VARCHAR(200),
artist_id VARCHAR(100) NOT NULL,
year INT,
duration DOUBLE PRECISION,
PRIMARY KEY (song_id))
""")

artist_table_create = ("""CREATE TABLE artists(
artist_id VARCHAR(100) NOT NULL ,
artist_name VARCHAR(255),
artist_location VARCHAR(255),
artist_latitude DOUBLE PRECISION,
artist_longitude DOUBLE PRECISION,
PRIMARY KEY (artist_id))
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
start_time TIMESTAMP NOT NULL,
hour INT,
day INT,
week INT, 
month INT, 
year INT,
weekday INT,
PRIMARY KEY (start_time))
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id,
                                                                location, user_agent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                                                               """)


user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name,gender, level)  VALUES(%s,%s,%s,%s,%s) 
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level """)

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES(%s,%s,%s,%s,%s)
ON CONFLICT (song_id)  DO NOTHING""")

artist_table_insert = ("""INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) VALUES(%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO NOTHING""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day ,week, month, year, weekday) VALUES(%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (start_time) DO NOTHING""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id FROM songs s JOIN artists a ON s.artist_id = a.artist_id 
WHERE s.title = %s 
AND a.artist_name = %s 
AND s.duration = %s """)


# QUERY LISTS

create_table_queries = [ time_table_create, user_table_create, song_table_create, artist_table_create,songplay_table_create]
drop_table_queries = [time_table_drop, user_table_drop, song_table_drop, artist_table_drop, songplay_table_drop]