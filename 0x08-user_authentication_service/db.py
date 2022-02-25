#!/usr/bin/env python3
"""DB class module"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base, User


class DB:
    """Docstring for DB class"""
    def __init__(self):
        """Initialize a DB object"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Create a session"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save user to the database"""
        session = self._session
        user = User(email=email, hashed_password=hashed_password)

        session.add(user)

        session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """
           Returns the first row found in the users table as filtered
           by the method’s input arguments
        """
        session = self._session

        return session.query(User).filter_by(**kwargs).one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update the user attributes from kwargs"""
        user = self.find_user_by(id=user_id)

        for k, v in kwargs.items():
            if not hasattr(user, k):
                raise ValueError
            setattr(user, k, v)

        self._session.commit()
        return None
