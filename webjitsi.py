#opens a secure jitsi call with a given address
#cameron hill - python 3

import webbrowser
import secrets

tagon = "INVALID URL"
startstring = "https://meet.jit.si/"
url = "https://meet.jit.si/INVALID_URL_TRY_AGAIN"

#import this file into your python file with: import webjitsi.py
def newURL(doctorString):
    global startstring
    global tagon
    global url
    addnumber = secrets.randbelow(10000)
    numbercode = str(addnumber)
    tagon = doctorString.replace(" ","_") + numbercode
    url = startstring + tagon
    return url
    
def dumpURL():
    file = open("urlcommunicator.txt","w")
    file.write(url)
    file.close()

def getURL():
    global url
    file = open("urlcommunicator.txt", "r")
    contents = file.read()
    url = contents

def openURL(url):
    webbrowser.open(url, new=1, autoraise=False)

def getCurrentURL():
    global url
    return url

# these were testing lines
# newURL("helpme")
# dumpURL()
# newURL("thisishell")
# getURL()
# print(getCurrentURL())
# openURL(getCurrentURL())