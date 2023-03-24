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

session = scoped_session(
    sessionmaker(
        autocommit = False,
	    autoflush = False,
	    bind = Engine
    )
)

Base = declarative_base()
Base.query = session.query_property()