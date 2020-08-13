from typing import Optional

from passlib.handlers.sha2_crypt import sha512_crypt as crypto

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
    new_user.hashed_password = hash_text(password)
    new_user.email = email
    new_user.first_name = first_name
    new_user.last_name = last_name

    new_user.account_type = 'user'

    session = db_session.create_session()
    try:
        session.add(new_user)
        session.commit()
    finally:
        session.close()

    return new_user


def hash_text(text: str) -> str:
    hashed_text = crypto.encrypt(text, rounds=152701)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return crypto.verify(plain_text, hashed_text)


def login_user(email, password) -> Optional[User]:
    session = db_session.create_session()

    user = session.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_hash(user.hashed_password, password):
        return None

    return user


def find_user_by_id(user_id: int) -> Optional[User]:
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    return user
