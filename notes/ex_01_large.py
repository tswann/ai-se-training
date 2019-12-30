import datetime
import os

class LocationService:

    GOOD_RESULT = 'Do some cool processing'
    BAD_RESULT = 'Something less cool'

    def __init__(self, locations):
        self.locations = locations

    @profile
    def _get_higher_rate_locations(self):
        return (location for location in self.locations if location.is_higher_rate())

    @profile
    def get_location_coolness_results(self):
        for location in self._get_higher_rate_locations():
            yield self.GOOD_RESULT if location.is_valid_category() else self.BAD_RESULT


class Location:
    LOCATION_RATE_THRESHOLD = 30
    LOCATION_VALID_CATEGORY = 'GHT'

    def __init__(self, config):
        self.name = config['name']
        self.rate = config['rate']
        self.category = config['category']
        self.data = config['data']

    def is_higher_rate(self):
        return self.rate > self.LOCATION_RATE_THRESHOLD

    def is_valid_category(self):
        return self.category == self.LOCATION_VALID_CATEGORY

    def __repr__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

def get_big_chunk():
    return bytearray(os.urandom(1000000))

@profile
def run():
    current_date = datetime.date.today().strftime("%y-%m-%d")
    locations = (Location({'name':'Austin', 'rate':31, 'category':'AGH', 'data': get_big_chunk() }), 
                Location({'name':'New York', 'rate':27, 'category':'GHT', 'data': get_big_chunk() }), 
                Location({'name':'Las Vegas', 'rate':56, 'category':'GHT', 'data': get_big_chunk() }),
                Location({'name':'Austin', 'rate':31, 'category':'AGH', 'data': get_big_chunk() }), 
                Location({'name':'New York', 'rate':27, 'category':'GHT', 'data': get_big_chunk() }), 
                Location({'name':'Las Vegas', 'rate':56, 'category':'GHT', 'data': get_big_chunk() }),
                Location({'name':'Austin', 'rate':31, 'category':'AGH', 'data': get_big_chunk() }), 
                Location({'name':'New York', 'rate':27, 'category':'GHT', 'data': get_big_chunk() }), 
                Location({'name':'Las Vegas', 'rate':56, 'category':'GHT', 'data': get_big_chunk() }),
                Location({'name':'Austin', 'rate':31, 'category':'AGH', 'data': get_big_chunk() }), 
                Location({'name':'New York', 'rate':27, 'category':'GHT', 'data': get_big_chunk() }), 
                Location({'name':'Las Vegas', 'rate':56, 'category':'GHT', 'data': get_big_chunk() }),
                Location({'name':'Austin', 'rate':31, 'category':'AGH', 'data': get_big_chunk() }), 
                Location({'name':'New York', 'rate':27, 'category':'GHT', 'data': get_big_chunk() }), 
                Location({'name':'Las Vegas', 'rate':56, 'category':'GHT', 'data': get_big_chunk() }))
    
    service = LocationService(locations)
    results = service.get_location_coolness_results()
    print([result for result in results])
    print('Process completed on ' + current_date)


if __name__ == '__main__':
    run()