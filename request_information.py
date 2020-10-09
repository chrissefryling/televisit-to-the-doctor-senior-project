#File: request_information
# this file / class is functions that STORE input
import json

class infoRequest:

#globals
	temp = 0
	ft = 0
	pul = 0
	lbs = 0
	blood = 0

#database stores everything as None when no current input
# when num is 1 the database is FILE INPUT when num is 0 database is initialized to None and it's user input
	def database_init(self,num):
		if num == 1:
			#ill add to this soon
			self.temp = 0
		if num == 0:
			self.temp = 0
			self.ft = 0
			self.pul = 0
			self.lbs = 0
			self.blood = 0
		else:
			print("Error. Something went wrong with database initialization.")

	def temperature_input(self,temp_new):
		self.temp = temp_new
	
	def height_input(self,ft_new):
		self.ft = ft_new
		
	def pressure_input(self,blood_new):
		self.blood = blood_new
		
	def weight_input(self,lbs_new):
		self.lbs = lbs_new
		
	def pulse(self,pul_new):
		self.pul = pul_new

	#RANIA communication methods
	#rainaBroadcast does one of two things: it either creates a json file that's then returned, or it saves that json file to a file
	#saving it to a file is optional; include the dumpfile parameter to do this
	#choosing a filename is also optional; include a filename parameter to do this
	#in an ideal world i'll fill in the else statement to actually communicate with rania, but i don't have the URLs of their API right now
	def raniaBroadcast(self, dumpfile=False, filename='send.json'):
		broadcast = {
			"Type code": "00000007",
			"Identifier code": "00",
			"Tag": "publish",
			"Data": {"temp": self.temp, "ft": self.ft, "blood": self.blood, "lbs": self.lbs, "pul": self.pul}
		}
		if dumpfile == True:
			file = open(filename, 'w')
			json.dump(broadcast, file)
			return filename
		else:
			sentdata = json.dumps(broadcast)
			return sentdata

	#raniaRecieving takes a recieved JSON from the Raina system and puts it in the information field
	#to be frank I couldn't remember if we needed this
	#use the optional parameters to set this function to actually call on a filename instead of an internally recieved json file
	def raniaRecieving(self, recievedJson, usefile=False, filename='send.json'):
		if usefile == True:
			file = open(filename, 'r')
			data = json.load(file)
		else:
    			data = json.loads(recievedJson)
		
		items = data['Data']
		self.temp = items['temp']
		self.ft = items['ft']
		self.blood = items['blood']
		self.lbs = items['lbs']
		self.pul = items['pul']

    		
	
# comment these in to test additions to the JSON handling functions
# cow = infoRequest()
# cow.temperature_input(20)
# cow.height_input(15)
# cow.pressure_input(66)
# cow.weight_input(400)
# cow.pulse(95)
# cow.raniaBroadcast(True)
# cow.raniaRecieving(None, True)
# print(cow.temp)
# print(cow.ft)
# print(cow.blood)
# print(cow.lbs)
# print(cow.pul)			