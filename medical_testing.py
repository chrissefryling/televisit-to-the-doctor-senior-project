#testing medical functions
#chrisse fryling - python3 

import json

#this class & py file is ONLY medical testing functions + menu testing
# class medicalTesting:

#checks thermometer connection
def temperature(temp):
	if temp != None and temp < 200 and temp > 0: #an acceptablish range of temperatures
		print("Thermometer working correctly.")
	else:
		print("Thermometer not working.")
		
#checks weight scale 
def weight(lbs):
	if lbs != None and lbs > -1 and 700 > lbs: #we dont weight shame in this household
		print("Scale working correctly.")
	else:
		print("Scale not working.")
	
#checks blood pressure
def pressure(blood):
	if blood != None and blood > 0 and blood < 300: #if your blood pressure is over 210 is doctor time
		print("Blood pressure working correctly.")
	else:
		print("Blood pressure not working.")

#checks height 
def height(ft):
	if ft != None and ft > 0 and ft < 10: # anything over 10 feet is ridiculous 
		print("Height information working correctly.")
	else:
		print("Height information not working.")
		
#checks pulse
def pulse(pul):
	if pul != None and pul > 0 and pul < 200: # anything over 200 is me during exams
		print("Pulse information working correctly.")
	else:
		print("Pulse information not working.")
		
#checks audio / video
#cameron please do this uwu implement to your specific function 
#fun fact: there's no specific function that tests well here! whoops.

#checks RANIA connectivity
#if we aren't connected online to rania, set trueConnection to false. this will call the bundled JSON file for testing instead.
def raniaOnline(trueConnection=True):
	#THE CORRECT JSON STRING THOUGH IS BELOW:
	jsoncheck = {
		"Type code": "00000007",
		"Identifier code": "00",
		"Tag": "InitializeA",
		"Data": None
	}
	jsonCheckFile = json.dumps(jsoncheck)

	#INSERT CODE TO SEND THIS FILE TO RANIA HERE
	#FOR NOW THOUGH...
	raniarecieved = None

	if trueConnection == False:
		file = open('raniaallgood.json','r')
		reciept = json.load(file)
	elif raniarecieved == None:
		print('Rania offline.')
		return
	else:
		reciept = json.loads(raniarecieved)

	#Depending on what the actual return JSON looks like, I may have to edit this.
	if(reciept['Response'] == '00'):
    		print('Rania online.')
	else:
    		print('Rania offline.')


