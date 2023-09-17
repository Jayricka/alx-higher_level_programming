#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = city.state.name
        print("{}: {} -> {}".format(city.id, city.name, state_name))

    session.close()
