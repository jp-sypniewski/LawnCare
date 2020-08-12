import datetime

import sqlalchemy as sa

from lawn_care.data.modelbase import SqlAlchemyBase


class QuoteRequest(SqlAlchemyBase):
    __tablename__ = 'quote_requests'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    username = sa.Column(sa.String)
    dttm_requested = sa.Column(sa.DateTime)
    contact_phone = sa.Column(sa.String)
    contact_email = sa.Column(sa.String)
    completed = sa.Column(sa.Boolean)
