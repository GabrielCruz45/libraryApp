from sqlalchemy import create_engine, MetaData, Column, Table, Integer, String, Float, insert, ForeignKey, func

engine = create_engine('sqlite:///mySec_database.db', echo=True)

meta = MetaData()

# a cool thing about SQLAlchemy is that you can use other sql flavors (posgres) with the same python code
people = Table(
    "people", # first parameter is name of table
    meta, # second parameter is the metadata object
    Column('id', Integer, primary_key=True), # then columns
    Column('name', String, nullable=False),
    Column('age', Integer)
)

meta.create_all(engine)

conn = engine.connect()

insert_statement = people.insert().values(name='univerze', age=420420420)
result = conn.execute(insert_statement)
conn.commit()

# you can also use insert()
insert_statement_two = insert(people).values(name='earthh', age=6969)
result = conn.execute(insert_statement_two)
conn.commit()

# both statements are equivalent
select_statement = people.select().where(people.c.age > 30)
result = conn.execute(select_statement)

update_statement = people.update().where(people.c.name == 'gabz').values(age=69)
result = conn.execute(update_statement)
conn.commit() # importante!!!!!!!

# use .in_() to search for more than one value
delete_statement = people.delete().where(people.c.name.in_(['gandalf', 'earthh', 'univerze', 'nice bro']))
result = conn.execute(delete_statement)
conn.commit()

# for row in result.fetchall():
#     print(row)



# create relations between tables
things = Table(
    "things",
    meta,
    Column('id', Integer, primary_key=True),
    Column('description', String, nullable=False),
    Column('value', Float),
    Column('owner', Integer, ForeignKey('people.id'))
)

meta.create_all(engine) # important!!! runs the CREATE keyword to create the table on the .db file

# insert_people = people.insert().values([
#     {'name' : 'xim', 'age' : 33},
#     {'name' : 'jeren', 'age' : 33},
#     {'name' : 'gatx', 'age' : 41},
#     {'name' : 'siney', 'age' : 35},
#     {'name' : 'mami', 'age' : 61},
#     {'name' : 'personaQueMeCaeMal', 'age' : 42168}
# ])


# insert_things = things.insert().values([
#     {'owner': 1, 'description' : 'MacBook Pro', 'value' : 1999.99},
#     {'owner': 1, 'description' : 'Epiphone Sheraton II', 'value' : 299.99},
#     {'owner': 2, 'description' : 'PC', 'value' : 699.99},
#     {'owner': 3, 'description' : 'Guitarra', 'value' : 299.99},
#     {'owner': 4, 'description' : 'Sartenes', 'value' : 599.99},
#     {'owner': 5, 'description' : 'Batería', 'value' : 1499.99},
#     {'owner': 6, 'description' : 'Casa', 'value' : 199999.99},
#     {'owner': 7, 'description' : 'CR-V', 'value' : 39999.99}
# ])

# conn.execute(insert_people)
# conn.commit()

# conn.execute(insert_things)
# conn.commit()


# for joining tables and figuring out which people own what
# if you were to add .outerjoin(...) (instead of .join(...))
# join_statement = people.outerjoin(things, people.c.id == things.c.owner) # joins the 2 tables based on id and owner columns 
join_statement = people.join(things, people.c.id == things.c.owner) # joins the 2 tables based on id and owner columns

# a partir del joint statement crear el select statement escogiendo los... 
# ************************************************tengo que check esta lógica pq es de SQL no de SQLAlchemy****************************************************************************
select_statement = people.select().with_only_columns(people.c.name, things.c.description).select_from(join_statement) 

result = conn.execute(select_statement)

for row in result.fetchall():
    print(row)



# we can aggregate
# the aggregation is as follows: everywhere where x is a value on said column "join/aggregate" 
# the other columns with other data. you should make a rule for this part

# with this aggregation we are adding the value of the all the things owned by each owner
group_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.value)).group_by(things.c.owner).having(func.sum(things.c.value) > 2000)
result = conn.execute(group_by_statement)

for row in result.fetchall():
    print(row)