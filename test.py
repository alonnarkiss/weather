from getWeather import getMyWeather
from setLocation import setLocation
import time

# we put in incorrect city in purpose
location_dict = [{'name': "Jerusalem District", 'country': "Israel"}, {'name': "New York", 'country': "USA"},
                 {'name': "Barcelos", 'country': "Spain"}, {'name': "Moskva", 'country': "Russia"},
                 {'name': "Rehovot", 'country': "Israel"}, {'name': "ness ziona", 'country': "Israel"},
                 {'name': "nesziyona", 'country': "Israel"}]


for location in location_dict:
    print('\n')
    print(location['country'] + '-' + location['name'])
    print('=========================')

    location_obj = setLocation(location['name'], location['country'], 0, 0)

    city, country = (location_obj.get_name(), location_obj.get_country())
    temp, him = getMyWeather(city, country)
    time.sleep(2)
