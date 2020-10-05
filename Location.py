from ExceptionWeather import Exception_Location_LonValue, \
    Exception_Location_LatValue


class Location(object):
    def __init__(self, name, country, lon=None, lat=None):
        self._name = name
        self._country = country
        if lon is None:
            self._lon = "longitude is not provide"
        else:
            self._lon = float(lon)
            if self._lon < -180.0 or self._lon > 180.0:
                raise Exception_Location_LonValue
        if lat is None:
            self._lat = "latitude is not provide"
        else:
            self._lat = float(lat)
            if self._lat < -180.0 or self._lat > 180.0:
                raise Exception_Location_LatValue

    def get_name(self):

        """
        Returns the toponym of the city
        :returns: the Unicode toponym
        """
        return self._name

    def get_country(self):

        """
        Returns the toponym of the country
        :returns: the Unicode toponym
        """
        return self._country

    def get_lon(self):
        """
        Returns the longitude of the location
        :returns: the float longitude
        """
        return self._lon

    def get_lat(self):
        """
        Returns the latitude of the location
        :returns: the float latitude
        """
        return self._lat

    def get_cord(self):
        """
        Returns the dictionary of the location
        :returns: the dict of latitude & longitude
        """
        coordinates = {'lon': self._lon, 'lat': self._lat}
        return coordinates

