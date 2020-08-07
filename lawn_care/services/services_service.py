from typing import List


def get_all_services() -> List[dict]:
    services = [
        {'name': 'mow lawn', 'category': 'lawn care'},
        {'name': 'fertilize', 'category': 'lawn care'},
        {'name': 'flea and tick control', 'category': 'weed/pest control'},
        {'name': 'shrub watering', 'category': 'landscaping'},
    ]
    return services
