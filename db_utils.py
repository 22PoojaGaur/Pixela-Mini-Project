from sqlalchemy import Column, DateTime, PrimaryKeyConstraint, engine, select
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


class User(Base):
    __tablename__ = "user" # table name 'user' store in database

    user_id = Column(Integer, primary_key = True)
    user_name = Column(String(32), unique=True)
    user_secret = Column(String(16))


class Habit(Base):
    __tablename__ = "habit"

    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    graph_name = Column(String, nullable=False)
    graph_id = Column(String, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint(user_id, graph_name, name="habit_pk"),
    )


class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key = True)
    graph_id = Column(Integer, ForeignKey("habit.graph_id"), nullable=False)
    value = Column(DateTime)


def setup():
    engine = create_engine("sqlite:///habit_tracker.db", echo=True, future=True)

    #print (f'debug {Base.metadata.tables}')
    Base.metadata.create_all(engine)

def get_engine():
    return create_engine("sqlite:///habit_tracker.db", echo=True, future=True)


def get_token(user_name):

    session = Session(bind=get_engine())
    stmt = select(User).where(User.user_name == user_name)

    result = session.scalars(stmt)

    if not result:
        raise RuntimeError

    # result.first() returns (<User>, )
    return result.first().user_secret  # result.first() result.all() result.scalars()


def get_user_id(user_name):
    session = Session(bind=get_engine())
    stmt = select(User).where(User.user_name == user_name)

    result = session.scalars(stmt)

    if not result:
        raise RuntimeError

    return result.first().user_id


def get_graph_id(user_name, graph_name):
    session = Session(bind=get_engine())

    stmt = (
        select(Habit)
            .join(User, Habit.user_id == User.user_id)
            .where(Habit.graph_name == graph_name)
            .where(User.user_name == user_name)
    )

    result = session.scalars(stmt)

    if not result:
        raise RuntimeError

    return result.first().graph_id


def create_user_db(user_name, user_secret):
    try:
        with Session(get_engine()) as session:
            user = User(
                user_name=user_name,
                user_secret=user_secret

            )
            session.add(user)
            session.commit()
    except:
        print (f"Failed to create user with name -> {user_name}")
        raise RuntimeError


def create_habit_for_user_db(user_id, graph_name, graph_id):
    try:
        with Session(get_engine()) as session:
            habit = Habit(
                user_id=user_id,
                graph_name=graph_name,
                graph_id=graph_id

            )
            session.add(habit)
            session.commit()
    except:
        print(f"Failed to create habit graph with name -> {graph_name}")
        raise RuntimeError


def create_record_db(graph_id, date):
    from datetime import datetime

    try:
        with Session(get_engine()) as session:
            record = Record(
                graph_id=graph_id,
                value=datetime.strptime(date, '%Y%m%d'),

            )
            session.add(record)
            session.commit()
    except:
        print(f"Failed to record entry for habit in graph")
        raise RuntimeError


def get_user_habits(user_name):

    session = Session(bind=get_engine())
    stmt = (
        select(Habit.graph_name)
        .join(User, User.user_id == Habit.user_id)
        .where(User.user_name == user_name)
    )

    result = session.scalars(stmt)

    if not result:
        raise RuntimeError

    return result.all()
