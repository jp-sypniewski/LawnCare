import datetime

import sqlalchemy as sa

from lawn_care.data.modelbase import SqlAlchemyBase


class QuoteRequest(SqlAlchemyBase):
    __tablename__ = 'quote_requests'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
    requester_name = sa.Column(sa.String)
    dttm_requested = sa.Column(sa.DateTime)
    contact_phone = sa.Column(sa.String, nullable=True)
    contact_email = sa.Column(sa.String, nullable=True)
    preference_contact = sa.Column(sa.String)
    completed = sa.Column(sa.Boolean)
