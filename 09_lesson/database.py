from sqlalchemy import create_engine

connection_string = 'postgresql://postgres:mypassword@localhost:5432/postgres'

engine = create_engine(connection_string)

