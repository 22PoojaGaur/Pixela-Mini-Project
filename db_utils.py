from sqlalchemy import Column, DateTime, PrimaryKeyConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user" # table name 'user' store in database

    user_id = Column(Integer, primary_key = True)
    user_name = Column(String(32))
    user_secret = Column(String(16))


class Habit(Base):
    __tablename__ = "habit"

    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    graph_name = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint(user_id, graph_name, name="habit_pk"),
    )


class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key = True)
    graph_id = Column(Integer, ForeignKey("habit.habit_pk"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    value = Column(DateTime)


def setup():
    engine = create_engine("sqlite:///habit_tracker.db", echo=True, future=True)

    #print (f'debug {Base.metadata.tables}')

    Base.metadata.create_all(engine)

