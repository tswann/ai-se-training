import datetime
from collections import namedtuple

Location = namedtuple('Location', ['name', 'rate', 'category'])

LOCATION_RATE_THRESHOLD = 30
LOCATION_VALID_CATEGORY = 'GHT'

def process_locations(locations):
    for location in locations:
        if is_rate_threshold_exceeded(location):
            if is_valid_category(location.category):
                print('Do some cool processing')
            else:
                print('This processing is less cool')
        else:
            print('Need to handle this scenario explicitly?')

def is_rate_threshold_exceeded(location):
    return location.rate > LOCATION_RATE_THRESHOLD

def is_valid_category(category):
    return category == LOCATION_VALID_CATEGORY

def run():
    current_date = datetime.date.today().strftime("%y-%m-%d")
    locations = (Location(name='Austin', rate=31, category='AGH'), 
                Location(name='New York', rate=27, category='GHT'), 
                Location(name='Las Vegas', rate=56, category='GHT'))
    
    process_locations(locations)
    print('Process completed on ' + current_date)


if __name__ == '__main__':
    run()
