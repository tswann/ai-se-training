from dataclasses import dataclass
import datetime
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

class LocationService:

    GOOD_RESULT = 'Do some cool processing'
    BAD_RESULT = 'Something less cool'

    def __init__(self, locations):
        self.locations = locations

    def _get_higher_rate_locations(self):
        return (location for location in self.locations if location.is_higher_rate)

    def get_location_coolness_results(self):
        for location in self._get_higher_rate_locations():
            logging.debug(location)
            yield self.GOOD_RESULT if location.is_valid_category else self.BAD_RESULT


@dataclass
class Location:
    name: str
    rate: int
    category: str

    LOCATION_RATE_THRESHOLD = 30
    LOCATION_VALID_CATEGORY = 'GHT'

    @property
    def is_higher_rate(self):
        return self.rate > self.LOCATION_RATE_THRESHOLD

    @property
    def is_valid_category(self):
        return self.category == self.LOCATION_VALID_CATEGORY

    def __repr__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

def run():
    current_date = datetime.date.today().strftime("%y-%m-%d")
    locations = (Location('Austin', 31, 'AGH'), 
                Location('New York', 27, 'GHT'), 
                Location('Las Vegas', 56, 'GHT'))
    
    service = LocationService(locations)
    results = service.get_location_coolness_results()
    output_results(results)
    #output_results_2(results)
    #output_results_2("someothing")
    #output_results_2(1)
    logging.info('Process completed on ' + current_date)


def output_results(results: iter):
    logging.info([result for result in results])

def output_results_2(results):
    if hasattr(results, '__iter__'):
        print([result for result in results])
    else:
        print(results)

if __name__ == '__main__':
    run()