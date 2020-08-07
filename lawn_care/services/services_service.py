from typing import List


def get_all_services() -> List[dict]:
    services = [
        {'name': 'mow lawn', 'class': 'lawn care'},
        {'name': 'fertilize', 'class': 'lawn care'},
        {'name': 'flea and tick control', 'class': 'weed/pest control'},
        {'name': 'shrub watering', 'class': 'landscaping'},
    ]
    return services
