import datetime

import sqlalchemy as sa

from lawn_care.data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, unique=True)
    hashed_password = sa.Column(sa.String, unique=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
