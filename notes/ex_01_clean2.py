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
        return (location for location in self.locations if location.is_higher_rate())

    def get_location_coolness_results(self):
        for location in self._get_higher_rate_locations():
            logging.debug(location)
            yield self.GOOD_RESULT if location.is_valid_category() else self.BAD_RESULT


class Location:
    LOCATION_RATE_THRESHOLD = 30
    LOCATION_VALID_CATEGORY = 'GHT'

    def __init__(self, config):
        self.name = config['name']
        self.rate = config['rate']
        self.category = config['category']

    def is_higher_rate(self):
        return self.rate > self.LOCATION_RATE_THRESHOLD

    def is_valid_category(self):
        return self.category == self.LOCATION_VALID_CATEGORY

    def __repr__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

def run():
    current_date = datetime.date.today().strftime("%y-%m-%d")
    locations = (Location({'name':'Austin', 'rate':31, 'category':'AGH'}), 
                Location({'name':'New York', 'rate':27, 'category':'GHT'}), 
                Location({'name':'Las Vegas', 'rate':56, 'category':'GHT'}))
    
    service = LocationService(locations)
    results = service.get_location_coolness_results()
    logging.info([result for result in results])
    logging.info('Process completed on ' + current_date)


if __name__ == '__main__':
    run()