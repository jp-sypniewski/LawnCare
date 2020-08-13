from typing import List, Optional

from lawn_care.data import db_session
from lawn_care.data.quote_requests import QuoteRequest


def get_all_quote_requests() -> List[QuoteRequest]:
    session = db_session.create_session()

    quote_requests = session.query(QuoteRequest).all()

    return quote_requests


def add_quote_request(requester_name: str,
                      dttm_requested,
                      contact_phone: str,
                      contact_email: str,
                      preference_contact: str
                      ) -> Optional[QuoteRequest]:
    # TODO stuff to add the quote request...

    # TODO wondering what the input should look like here
    # TODO do we use object as param or dict with traits?

    return input


def update_quote_request(input: QuoteRequest) -> QuoteRequest:
    # TODO add body for updating the input

    return input
