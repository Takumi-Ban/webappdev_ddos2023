from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import declarative_base

dbname = 'memo'
DB = f'sqlite:///{dbname}.sqlite?charset=utf8mb4'

Engine = create_engine(
    DB,
    echo=False
)
Base = declarative_base()

# create session
session = scoped_session(
    sessionmaker(
        autocommit = False,
	    autoflush = False,
	    bind = Engine
    )
)

# use model
Base = declarative_base()
Base.query = session.query_property()