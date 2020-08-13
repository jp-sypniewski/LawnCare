from typing import List, Optional

from lawn_care.data import db_session
from lawn_care.data.quote_requests import QuoteRequest


def get_all_quote_requests() -> List[QuoteRequest]:
    session = db_session.create_session()

    quote_requests = session.query(QuoteRequest).all()

    return quote_requests


def add_quote_request(requester_name: str,
                      dttm_requested: str,
                      contact_phone: str,
                      contact_email: str,
                      preference_contact: str
                      ) -> Optional[QuoteRequest]:
    new_quote = QuoteRequest()
    new_quote.requester_name = requester_name
    new_quote.dttm_requested = dttm_requested
    new_quote.contact_phone = contact_phone
    new_quote.contact_email = contact_email
    new_quote.preference_contact = preference_contact

    new_quote.completed = False

    session = db_session.create_session()

    session.add(new_quote)
    session.commit()

    return None


def update_quote_request(input: QuoteRequest) -> QuoteRequest:
    # TODO add body for updating the input

    return input
