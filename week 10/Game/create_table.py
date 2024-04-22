import psycopg2
import csv

conn = psycopg2.connect(
  host = 'localhost',
  database = 'postgres',
  user = 'postgres',
  password = '76141Zam'
)

cursor = conn.cursor()
scripts = '''
    create table if not exists snake_users(
      id serial primary key,
      login varchar(20) not null unique,
      password varchar(20) not null,
      score int default 0,
      level int default 0
  );
'''
cursor.execute(scripts)
conn.commit()
print("Created")

"""
drop_table_query = "drop table snake_users;"
cursor.execute(drop_table_query)
conn.commit()"""

conn.close()
