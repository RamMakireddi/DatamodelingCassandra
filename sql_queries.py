# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

time_table_create = ("create table if not exists time "
"(start_time bigint primary key, hour int not null, day int not null, week int not null, month int not null, year int not null, weekday int not null);")

user_table_create = ("create table if not exists users "
"(user_id int primary key, first_name varchar not null, last_name varchar not null, gender char not null, level varchar default 'free');")

songplay_table_create = ("create table if not exists songplays "
"(songplay_id SERIAL primary key, start_time bigint references time, user_id int references users, level varchar default 'free', song_id varchar references songs," 
  "artist_id varchar references artists, session_id int check (session_id>=0), location text not null, user_agent text not null,"
  "unique(start_time,user_id,song_id,artist_id)) ;")

song_table_create = ("create table if not exists songs "
"(song_id varchar primary key, title text not null, artist_id varchar not null, year int default 0, duration numeric CONSTRAINT positive_duration CHECK (duration>=0));")

artist_table_create = ("create table if not exists artists "
"(artist_id varchar primary key, name varchar not null , location text, latitude numeric, longitude numeric);")

# INSERT RECORDS



songplay_table_insert = ("insert into songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)"
"values(%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (start_time,user_id,song_id,artist_id) DO UPDATE SET (level,session_id,location,user_agent)=(EXCLUDED.level,EXCLUDED.session_id,EXCLUDED.location,EXCLUDED.user_agent)")

user_table_insert = ("insert into users (user_id, first_name, last_name, gender, level) values(%s,%s,%s,%s,%s) " 
                     " ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level")


song_table_insert = ("insert into songs (song_id, title, artist_id, year, duration) values(%s,%s,%s,%s,%s) "
                    " ON CONFLICT (song_id) DO NOTHING")

artist_table_insert = ("insert into artists (artist_id, name, location, latitude, longitude) values(%s,%s,%s,%s,%s) "
                      " ON CONFLICT (artist_id) DO UPDATE SET (location,latitude,longitude)=(EXCLUDED.location, EXCLUDED.latitude,EXCLUDED.longitude)")


time_table_insert = ("insert into time (start_time, hour, day, week, month, year, weekday) values(%s,%s,%s,%s,%s,%s,%s) "
                      " ON CONFLICT (start_time) DO NOTHING")

# FIND SONGS

song_select = ("select s.song_id, s.artist_id from songs s join artists a on s.artist_id=a.artist_id "
               " where s.title=%s and a.name=%s and s.duration=%s")

# QUERY LISTS

create_table_queries = [time_table_create, user_table_create, song_table_create, artist_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]