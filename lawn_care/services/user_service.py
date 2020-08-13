from typing import Optional

from lawn_care.data import db_session
from lawn_care.data.users import User


def find_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()
    return session.query(User).filter(User.email == email).first()


def create_user(username: str,
                password: str,
                email: str,
                first_name: str,
                last_name: str
                ):
    new_user = User()
    new_user.username = username
    new_user.hashed_password = password
    new_user.email = email
    new_user.first_name = first_name
    new_user.last_name = last_name

    session = db_session.create_session()
    try:
        session.add(new_user)
        session.commit()
    finally:
        session.close()

    return new_user
