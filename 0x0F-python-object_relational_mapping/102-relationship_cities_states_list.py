from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, State, City
import sys

def list_cities_states(username, password, database_name):
    # Create engine to connect to the database
    engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@localhost:3306/{database_name}")

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and access their associated State objects using the state relationship
    cities = session.query(City).order_by(City.id).all()

    # Iterate over each City and display its id, name, and associated State name
    for city in cities:
        state_name = city.state.name
        print(f"{city.id}: {city.name} -> {state_name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 102-relationship_cities_states_list.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_cities_states(username, password, database_name)
