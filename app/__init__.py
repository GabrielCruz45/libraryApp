# This special file turns the app directory into a Python package. 
# It contains the application factory function. 
# This function is responsible for creating the Flask app instance, 
# initializing extensions like SQLAlchemy, and 
# registering our different sets of routes (Blueprints).



from flask import Flask
from sqlalchemy import create_engine, text

app = Flask(__name__)
app.secret_key = 'fdd3d8e6681c52408787e5a560261e061084d36d988786e016e6640ff9e73e18'

## create database file, connect to execute methods?
engine = create_engine('sqlite:///mydatabase.db', echo=True)
conn = engine.connect()
conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str, age int)"))
## to actually commit ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ SQL queries
conn.commit()


@app.route("/")
def hello_world():
    return "<p> Hello, world. <p>"