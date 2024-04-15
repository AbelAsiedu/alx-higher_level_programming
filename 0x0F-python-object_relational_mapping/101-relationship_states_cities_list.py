#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, State, City
import sys

def list_states_cities(username, password, database_name):
    # Create engine to connect to the database
    engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@localhost:3306/{database_name}")

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and corresponding City objects using the cities relationship
    states = session.query(State).order_by(State.id).all()

    # Iterate over each State and its associated City objects
    for state in states:
        print(f"{state.id}: {state.name}")
        cities = sorted(state.cities, key=lambda city: city.id)  # Sort cities by id
        for city in cities:
            print(f"    {city.id}: {city.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 101-relationship_states_cities_list.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states_cities(username, password, database_name)
