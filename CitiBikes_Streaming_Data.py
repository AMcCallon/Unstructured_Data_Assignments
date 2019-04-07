#Import needed packages
import requests
import time
import ujson
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer


#Create function to turn dictionaries into bytes
def dict_to_bytes(dict):
	str =ujson.dumps(dict)
	binary= ' '.join(format(ord(letter), 'b') for letter in str)

#Create function to run
def citibike_request():
	r=requests.get(request_url)

	#Parse the JSON file
	station_info =ujson.loads(r.content.decode('utf-8'))
	
	#Break up messages into seperate messages
	station_data = (station_info)['data']['stations']
	
	#Assign variables for for loop
	station_len = len(station_data)
	i=0
	
	#While loop
	while i<station_len:
		unique_station_data = station_data[i]
		Dict_as_bytes = dict_to_bytes(unique_station_data)
		p.produce('citibike.station.update.1', Dict_as_bytes)
		i+=1

#Begin Producing messages in kafka
admin = AdminClient({'bootstrap.servers': 'kafka-1:9092'})
admin.create_topics([NewTopic("citibike.station.update.1", num_partitions = 3, replication_factor = 1)])

#Produce a message
p=Producer({'bootstrap.servers': 'kafka-1:9092', 'api.version.request': True})

#Set URL request
request_url = ("https://gbfs.citibikenyc.com/gbfs/en/station_information.json")


	
while True:
	citibike_request()
	p.flush()
	print("Scraping Page")
	print("Sending Message")
	time.sleep(10)
