import datetime

import sqlalchemy as sa

from lawn_care.data.modelbase import SqlAlchemyBase


class Service(SqlAlchemyBase):
    __tablename__ = 'services'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, unique=True)
    category = sa.Column(sa.String)
    quick_description = sa.Column(sa.String)
    extended_description = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    updated_at = sa.Column(sa.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)