from ex_01_clean2 import Location, LocationService

def test_higher_rate_location():
    location = Location('Las Vegas', 31, 'ABC')
    assert location.is_higher_rate

def test_highest_low_rate_location():
    location = Location('Las Vegas', Location.LOCATION_RATE_THRESHOLD, 'ABC')
    assert not location.is_higher_rate

def test_valid_location_category():
    location = Location('Las Vegas', 30, Location.LOCATION_VALID_CATEGORY)
    assert location.is_valid_category

def test_invalid_location_category():
    location = Location('Las Vegas', 30, 'BLAH')
    assert not location.is_valid_category