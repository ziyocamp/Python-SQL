from sqlalchemy import (
    create_engine, URL, text,
    Table, Column, String, INTEGER, BOOLEAN,
    MetaData,
    insert, select,
)
from config import HOST, PORT, USER, PASSWORD, DBNAME


url_object = URL.create(
    "postgresql+psycopg2",
    username=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DBNAME,
)

engine = create_engine(url_object)

meta = MetaData()
users = Table(
    'users',
    meta,
    Column('id', INTEGER(), primary_key=True),
    Column('first_name', String(length=64), nullable=False),
    Column('last_name', String(length=64)),
    Column('is_male', BOOLEAN()),
)
meta.create_all(engine)

with engine.connect() as conn:
    stmt = insert(users).values(first_name="Ali")
    conn.execute(stmt)
    conn.commit()

with engine.connect() as conn:
    stmt = select(users)
    
    result = conn.execute(stmt)
    for row in result:
        print(row)

