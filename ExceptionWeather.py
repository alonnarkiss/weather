import sys


class Error(Exception):
    pass


class Exception_Location_LonValue(Error):
    """
    Error class that represents longitude of the location.

    """
    pass


class Exception_Location_LatValue(Error):
    """
    Error class that represents latitude of the location.

    """
    pass


class Exception_Weather_CityOrCountryName(Error):
    """
     Error class that represents incorrect city or country

    """
    pass


class Exception_Weather_requests(IOError):
    """
    Generic exception for Weather.py file like timeout conditions, connection etc.

    """
    def __init__(self, msg, original_exception):
        super(Exception_Weather_requests, self).__init__(msg + (": %s" % original_exception))
        self.original_exception = original_exception
        print(msg + (": %s" % original_exception))
        sys.exit()
