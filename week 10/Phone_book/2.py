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
    create table if not exists phone_book(
      id serial primary key,
      name varchar(20) not null,
      phone int not null unique
  );
'''
cursor.execute(scripts)
conn.commit()

"""drop_table_query = "drop table phone_book;"
cursor.execute(drop_table_query)
conn.commit()"""

with open('phone_book.csv', 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name, phone = row 
        insert_query = "INSERT INTO phone_book (name, phone) VALUES (%s, %s);"
        cursor.execute(insert_query, (name, phone))
        conn.commit()

cursor.close()
conn.close()