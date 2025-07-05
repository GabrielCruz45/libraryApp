from sqlalchemy import create_engine, text

## create database file, connect to execute methods?
engine = create_engine('sqlite:///mydatabase.db', echo=True)
conn = engine.connect()
conn.execute(text("CREATE TABLE IF NOT EXISTS people (name TEXT, age INTEGER);"))
## to actually commit ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ SQL queries
conn.commit()

from sqlalchemy.orm import Session

session = Session(engine)
session.execute(text("INSERT INTO people (name, age) VALUES ('Gabz', 31);"))
session.commit()


# SQLAlchemy core first

# SQLAlchemy ORM