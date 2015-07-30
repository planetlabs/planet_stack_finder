# Author: matt0 (matt@planet.com)
# Description: performs various functions related to distances on Earth

import math

EARTH_RADIUS = 6378.1   # km
DEGREES_TO_RADIANS = math.pi / 180.0
RADIANS_TO_DEGREES = 180.0 / math.pi


def arc_length_to_latitude(km):
    '''
    Calculate the latitude delta from a distance in km
    Latitude is measured in degrees.
    Earth is assumed to be perfectly spherical.
    '''
    # Given a distance north, return the change in latitude.
    return (km / EARTH_RADIUS) * RADIANS_TO_DEGREES


def change_in_longitude(latitude, km):
    '''
    Given a latitude and a distance west, return the change in longitude.
    '''
    # Find the radius of a circle around the earth at given latitude.
    radius = EARTH_RADIUS * math.cos(latitude * DEGREES_TO_RADIANS)
    return (km / radius) * RADIANS_TO_DEGREES
