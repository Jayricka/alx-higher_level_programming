#!/usr/bin/python3
"""Lists all State objects with letter 'a' from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        states_with_a = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id)
        for state in states_with_a:
            print(f"{state.id}: {state.name}")
        session.close()
