from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#  Executing the instruction from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# Create a class-based for the "Countries" table
class Country(base):
    __tablename__ = "Country"
    Id = Column(Integer, primary_key=True)
    name = Column(String)
    cap_city = Column(String)
    population = Column(Integer)
    gdp_in_usd_T = Column(Float)


# Instead of connecting to the databae directly, we will ask a session
# Create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# Opens an actual session by calling the session () subclass defined above
session = Session()

# Creating the database using declarative_base subclass
base.metadata.create_all(db)


# # Creating records for country table
# united_states = Country(
#     name="United States",
#     cap_city="Washington D.C.",
#     population=331449281,
#     gdp_in_usd_T=22.67
# )

# japan = Country(
#     name="Japan",
#     cap_city="Tokyo",
#     population=126050804,
#     gdp_in_usd_T=5.15
# )

# germany = Country(
#     name="Germany",
#     cap_city="Berlin",
#     population=83149300,
#     gdp_in_usd_T=4.24
# )

# brazil = Country(
#     name="Brazil",
#     cap_city="Brasilia",
#     population=214132099,
#     gdp_in_usd_T=2.48
# )

# egypt = Country(
#     name="Egypt",
#     cap_city="Cairo",
#     population=104124440,
#     gdp_in_usd_T=0.33
# )

# malaysia = Country(
#     name="Malaysia",
#     cap_city="Kuala Lampur",
#     population=32776194,
#     gdp_in_usd_T=333.24
# )


# add each instance of our programmers to our session
# session.add(united_states)
# session.add(japan)
# session.add(germany)
# session.add(brazil)
# session.add(egypt)
# session.add(malaysia)

# commit our session to the database
# session.commit()

# Deleting a single record

dcountry = input("Enter the name of the country you want to delete: ")

country = session.query(Country).filter_by(name=dcountry).first()
# defensive programing
if country is not None:
    print("Country Found! it is", country.name)
    confirmation = input("Are you sure, you want to delete it? y/n ")
    if confirmation.lower() == "y":
        session.delete(country)
        session.commit()
        print("Country just now deleted")
    else: 
        print("Country not deleted")
else:
    print("No country fond")


# query the database to find all countries
countries = session.query(Country)
for country in countries:
    print(
        country.Id,
        country.name,
        country.cap_city,
        country.population,
        country.gdp_in_usd_T,
        sep=" | "
        )


