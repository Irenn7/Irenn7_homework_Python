from sqlalchemy import create_engine

connection_string = 'postgresql://postgres:RoyaL@localhost:5432/postgres'

engine = create_engine(connection_string)
