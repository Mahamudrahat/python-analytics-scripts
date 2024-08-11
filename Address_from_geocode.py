from geopy.geocoders import Nominatim


text_file = open("geocode.txt", "r")
lines = text_file.read().split('\n')
#print (lines)
text_file.close()
list_size = len(lines)
print (str(list_size))


for i in range(list_size):
	sub_lines=lines[i].split(',')
	lat=sub_lines[0]
	lon=sub_lines[1]
	geolocator = Nominatim(user_agent="specify_your_app_name_here")
	location = geolocator.reverse("{}, {}".format(lat, lon))
	print(location.address)