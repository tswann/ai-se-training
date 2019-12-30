from ex_01_clean2 import Location, LocationService

def test_higher_rate_location():
    location = Location({'name':'Las Vegas', 'rate':31, 'category': 'ABC'})
    assert location.is_higher_rate()

def test_highest_low_rate_location():
    location = Location({'name':'Las Vegas', 'rate':Location.LOCATION_RATE_THRESHOLD, 'category': 'ABC'})
    assert not location.is_higher_rate()

def test_valid_location_category():
    location = Location({'name':'Las Vegas', 'rate':30, 'category': Location.LOCATION_VALID_CATEGORY})
    assert location.is_valid_category()

def test_invalid_location_category():
    location = Location({'name':'Las Vegas', 'rate':30, 'category': 'BLAH'})
    assert not location.is_valid_category()