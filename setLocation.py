from Location import Location
from ExceptionWeather import Exception_Location_LatValue, Exception_Location_LonValue
import sys


def setLocation(name, country, lon, lat):
    """

    :param name: the name of the chooses city
    :param country: the name of the chooses country
    :param lon: Longitude value of the location
    :param lat: Latitude value of the location
    :return: reference to the class Location object
    """
    try:
        ob = Location(name, country, lon, lat)

    except Exception_Location_LatValue:
        print("ERROR in class Location: Latitude value must be between -180 and 180")
        print('--------------------------------------------------------------------')
        sys.exit()

    except Exception_Location_LonValue:
        print("ERROR in class Location: Longitude value must be between -180 and 180")
        print('----------------------------------------------------------------------')
        sys.exit()

    return ob
