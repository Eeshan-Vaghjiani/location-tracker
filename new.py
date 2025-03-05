import phonenumbers
from phonenumbers import geocoder
from test import number
import folium

key = "2f92da82d2164970a0b250df0098414f"

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,"en")
print (number_location)


from phonenumbers import carrier 
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder =OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
 