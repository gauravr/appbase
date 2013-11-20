import datetime

from sqlalchemy import create_engine, MetaData, Column, Integer, DateTime, BOOLEAN
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

import settings

# configure Session class with desired options
# later, we create the engine
engine = create_engine(settings.DB_URL, convert_unicode=True, echo=True, pool_size=30)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

metadata = MetaData()
engine.pool._use_threadlocal = True


def connect():
    return Session()


def Column_created():
    return Column('created', DateTime, default=datetime.datetime.now)


def Column_id():
    return Column('id', Integer, primary_key=True)


def Column_active():
    return Column('active', BOOLEAN, default=True)


def tr_start(tls):
    pass

def tr_complete(tls):
    Session.commit()
    Session.remove()


def tr_abort(tls):
    Session.rollback()
