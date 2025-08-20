from datetime import date
import psycopg2
import config


connection = psycopg2.connect(
    host=config.HOST,
    port=config.PORT,
    user=config.USER,
    password=config.PASSWORD,
    dbname=config.DBNAME
)

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS tasks;")

cursor.execute("""
    CREATE TABLE tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(128) NOT NULL,
        description TEXT,
        due_date DATE NOT NULL,
        create_at DATE NOT NULL
    );
""")

due_date = date(year=2025, month=8, day=21)
today = date.today()

cursor.execute("""
    INSERT INTO tasks (title, description, due_date, create_at)
    VALUES (%s, %s, %s, %s)
""", ['Yugurish', 'ertalab 3.5 km yugurishim kerak', due_date, today])

cursor.execute("""
    INSERT INTO tasks (title, description, due_date, create_at)
    VALUES (%s, %s, %s, %s)
""", ['Dars qilish', 'ertalab 2 soat dars qilishim kerak', due_date, today])


cursor.execute("SELECT * FROM tasks;")
rows = cursor.fetchall()

for row in rows:
    id, title, desc, due_date, created_at = row
    print(id, title, due_date)

cursor.close()

connection.commit()
connection.close()

