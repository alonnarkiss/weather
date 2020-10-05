import requests
from ExceptionWeather import Exception_Weather_requests,\
                          Exception_Weather_CityOrCountryName


class Weather(object):
    def __init__(self, name, country, cord):
        self._key = "b0893a7415e38deec3b8dacac8829cfb"
        # check if have coordinates input,
        # if have coordinates input init the url address by the coordinates
        # otherwise init the url by city and country.
        if type(cord) is dict:
            self._lat = cord["lat"]
            self._lon = cord["lon"]
            self._url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric" \
                .format(self._lat, self._lon, self._key)
        else:
            self._city = name
            self._country = country
            self._url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric'.format(self._city,
                                                                                                               self._country,
                                                                                                               self._key)
        try:
            get = requests.get(self._url)
        except requests.exceptions.ConnectionError as e:
            raise Exception_Weather_requests("Unable to connect", e)

        dic1 = get.json()
        # Check if have incorrect input by city/country name
        if dic1["cod"] != "404":
            self._temp = dic1['main']['temp']
            self._humidity = dic1['main']['humidity']
        else:
            # print(dic1["cod"])
            raise Exception_Weather_CityOrCountryName

    def get_temperature(self):
        """
        Returns the temperature of the location
        :returns: temperature
        """
        return self._temp

    def get_humidity(self):
        """
        Returns the humidity of the location
        :returns: humidity
        """
        return self._humidity
