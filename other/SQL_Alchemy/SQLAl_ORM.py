from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# This is the starting point. It creates an "engine" that knows how to talk to a specific database. 
# In this case, it's set up to connect to a file named myOtherdatabase.db using SQLite, which is a simple, 
# file-based database.
engine = create_engine("sqlite:///myOtherdatabase.db", echo=True)

# Base = declarative_base(): This creates a base class that our table-mapping classes will inherit from. 
# It’s the magic that links our Python classes to the database tables.
Base = declarative_base




# class Person(Base): & class Thing(Base):: These are Python classes, but they're special. 
# They act as blueprints for our database tables. Person maps to a people table, and Thing 
# maps to a things table.
class Person(Base): # singular
    __tablename__ = 'people' # plural
    id = Column(Integer, primary_key=True) # primary_key=True: This marks the id column as the unique identifier for each row. Every person will have a unique ID.
    name = Column(String, nullable=False) # nullable=False: This means the name column must have a value; it can't be empty.
    age = Column(Integer)

    # things = relationship('Thing', ...): This gives each Person object a things attribute, 
    # which will be a list of all the Thing objects they own.
    things = relationship('Thing', back_populates='person')
    # "Back-populating" means that when you link two database objects together on one side of a relationship, 
    # SQLAlchemy will automatically update the other side of that relationship for you. 
    # It keeps your Python objects in sync.

class Thing(Base):
    # __tablename__ = 'things': This explicitly names the table in the database. 
    # It's good practice to use plural table names.
    __tablename__ = 'things'
    # Column(...): Each Column represents a column in the database table.
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float)
    # ForeignKey('people.id'): This is crucial for relationships. 
    # It creates a link by telling the owner column in the things table that it must contain an id 
    # that exists in the people table. This ensures every "thing" has a valid owner.
    owner = Column(Integer, ForeignKey('people.id'))

    # relationship(...): This is the Python side of the connection. 
    # It creates a powerful link between the Person and Thing objects.

    # person = relationship('Person', ...): 
    # This gives each Thing object a person attribute, 
    # which will be the Person object who owns it.
    person = relationship('Person', back_populates='things')
    # back_populates='...': This tells the two relationships how to stay in sync. 
    # When you assign a Person to a Thing, the Thing automatically gets added to that 
    # Person's list of things, and vice versa.


# This line takes all the blueprints (classes inheriting from Base) and 
# tells the engine to actually create those tables in the myOtherdatabase.db file 
# if they don't already exist.
Base.metadata.create_all(engine)


# sessionmaker: You can think of this as creating a factory for generating conversations (sessions) with the database.
Session = sessionmaker(bind=engine)
# session = Session(): This starts a new conversation. 
# A session is like a temporary workspace or scratchpad where you can load, add, and change your Python objects 
# before saving them to the database.
session = Session()

# new_person = Person(...): We create a new Person object just like any other Python object.
new_person_one = Person(name='Sam', age=80)
new_person_two = Person(name='Sonny', age=70)


# We place this new object into our "workspace" (the session). The object is now "staged" to be saved.
# session.add(new_person_one) to add just the first person
session.add_all([
    new_person_one,
    new_person_two
])
# use .add_all([]) to add more than one!

# session.commit(): This is the final step. It takes all the changes you've made in the session 
# (in this case, adding Sam) and permanently saves them to the database. 
# If you forget to commit, your changes will be lost when the program ends.
session.commit()