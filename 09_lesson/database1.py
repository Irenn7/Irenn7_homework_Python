from sqlalchemy import create_engine

db_connection_string = 'postgresql://postgres:RoyaL@localhost:5432/postgres'
db = create_engine(db_connection_string)
engine = db




