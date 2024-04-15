#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, State, City
import sys

def create_state_city(username, password, database_name):
    # Create engine to connect to the database
    engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@localhost:3306/{database_name}")

    # Create all defined tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State "California" with City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add State and City to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 100-relationship_states_cities.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    create_state_city(username, password, database_name)
