from sqlalchemy import(
    create_engine, Column, Integer, String
)

# we're not going to create tables, but instead, we'll be creating Python classes.
# These Python classes will subclass the declarative_base, meaning that
# any class we're making will extend from the main class within the ORM.
    
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql://postgres:<pass>@localhost/chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead connecting directly to the db we will ask for a sessio
# create a new instnce of the session maker, then point to our session (the db)
Session = sessionmaker(db)
# open the actual session by calling the Session() subclass defined above
session = Session()

# create the database using declarative_base subclass
base.metadata.create_all(db)

#-----------------------------------------CREATE
# create records on the "Programmer" table
ada_lovelace = Programmer(    
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(    
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(    
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL Language"
)

margaret_hamilton = Programmer(    
    first_name = "Margaret",
    last_name = "Hamelton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11"
)

margaret_hamilton = Programmer(    
    first_name = "Margaret",
    last_name = "Hamelton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(    
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(    
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British",
    famous_for = "World Wide Web"
)

kat_me = Programmer(    
    first_name = "Kat",
    last_name = "Me",
    gender = "F",
    nationality = "British",
    famous_for = "Lern to code"
)

# add each instance of "programmer" to the session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(kat_me)

# commit the session to the database
# session.commit()


#-----------------------------------------UPDATE
# update a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# commit the session to the database
# session.commit()

# update multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender is not defined")
#     session.commit()



#-----------------------------------------DELETE
## delete a single record
# fname = input('Enter a first name: ')
# lname = input('Enter a last name: ')
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
## defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer is not deleted")
# else:
#     print("No records found")

## delete ALL records (be careful!)
# for programmer in session.query(Programmer):
#     session.delete()
#     session.commit()


# query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
