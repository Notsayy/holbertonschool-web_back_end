#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the User object."""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find the first user matching the given keyword arguments."""
        valid_columns = {c.key for c in User.__table__.columns}
        for key in kwargs:
            if key not in valid_columns:
                raise InvalidRequestError(
                    f"'{key}' is not a valid column of User"
                )

        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound("No user found matching the given criteria")
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes and commit changes to the database.

        Args:
            user_id: the ID of the user to update
            **kwargs: user attributes to update

        Returns:
            None

        Raises:
            ValueError: if a key does not correspond to a User attribute
        """
        user = self.find_user_by(id=user_id)

        valid_columns = {c.key for c in User.__table__.columns}
        for key, value in kwargs.items():
            if key not in valid_columns:
                raise ValueError(f"'{key}' is not a valid attribute of User")
            setattr(user, key, value)

        self._session.commit()
