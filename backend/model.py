from sqlalchemy import Column, String, Date, DateTime, func, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from configparser import ConfigParser

from pydantic import BaseModel
from datetime import datetime, date

Base = declarative_base()

class UserTable(Base):
    __tablename__ = 'users'
    
    username = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    birthday = Column(Date)
    create_time = Column(DateTime, default=func.now())
    last_login = Column(DateTime, nullable=True)

class User(BaseModel):
    username: str
    password: str | None
    birthday: date | None
    create_time: datetime
    last_login: datetime | None

def sqlalchemy_to_pydantic(user: UserTable) -> User:
    return User(
        username=user.username,
        password=user.password,
        birthday=user.birthday,
        create_time=user.create_time,
        last_login=user.last_login
    )

# Parse database_connection_string in alembic.ini
config = ConfigParser()
config.read('alembic.ini')
db_url = config.get('alembic', 'sqlalchemy.url')

# Perform CRUD for the model

# Create the database engine
engine = create_engine(db_url)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a new user
def create_user(username, password, birthday, last_login=None) -> bool:
    session = Session()
    exist = get_user(username=username)
    if exist: return False
    user = UserTable(username=username, password=password, birthday=birthday, last_login=last_login)
    session.add(user)
    session.commit()
    session.close()
    return True

# Retrieve a user by username
def get_user(username):
    session = Session()
    user = session.query(UserTable).filter_by(username=username).first()
    session.close()
    if not user: return None
    return sqlalchemy_to_pydantic(user)

# Update a user's password
def update_user(username: str, new_password=None, birthday=None, last_login=None):
    session = Session()
    user = session.query(UserTable).filter_by(username=username).first()
    if not user: return False
    if new_password : user.password = new_password
    if birthday : user.birthday = birthday
    if last_login : user.last_login = last_login
    session.commit()
    session.close()
    return True

# Delete a user
def delete_user(username):
    session = Session()
    user = session.query(UserTable).filter_by(username=username).first()
    if not user: return False
    session.delete(user)
    session.commit()
    session.close()
    return True
