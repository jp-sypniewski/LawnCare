from typing import List

from lawn_care.data import db_session
from lawn_care.data.services import Service


def get_all_services() -> List[dict]:
    services = [
        {'name': 'mow lawn', 'category': 'lawn care'},
        {'name': 'fertilize', 'category': 'lawn care'},
        {'name': 'flea and tick control', 'category': 'weed/pest control'},
        {'name': 'shrub watering', 'category': 'landscaping'},
    ]
    return services


def get_db_services() -> List[Service]:
    session = db_session.create_session()

    services = session.query(Service).all()

    return services
