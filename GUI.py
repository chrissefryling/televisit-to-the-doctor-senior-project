import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
from os import path
import webjitsi as ji
import request_information as req

data = req.infoRequest()

root = tk.Tk()
root.title("RANIA TeleVisit to the Doctor")

#there will be no resizing of this window
root.resizable(0, 0)

canvas = tk.Canvas(root, height=750, width=1200, bg="#002855")
canvas.pack()

#all login screen information needed to create login screen
userlabel = tk.Label(root, text='Username', bg='#002855', fg='#EAAA00')
userlabel.config(font=('helvetica', 16))

userEntry = tk.Entry(root, width=25, font=('helvetica', 18))
passEntry = tk.Entry(root, show='*', width=25, font=('helvetica', 18))

passlabel = tk.Label(root, text='Password', bg='#002855', fg='#EAAA00')
passlabel.config(font=('helvetica', 16))

login_title = tk.Label(root, text='RANIA TeleVisit to the Doctor',
                       bg='#002855', fg='#EAAA00', font=('arial', 36))

current_doctor_un = None
is_data_uploaded = False

#function called when user pushes "Login" button
def checkLogin():
    username = userEntry.get()
    password = passEntry.get()

    if username == "doctor" and password == "password":
        global current_doctor_un
        print("Successfully logging in")
        current_doctor_un = "doctor"
        doctor_interface()

    elif username == "patient" and password == "password":
        global is_data_uploaded
        current_doctor_un = None
        if tk.messagebox.askyesno("Televisit", "Would you like to use the last medical data you recorded?"):
            if path.exists("raniaData.json"):
                data.raniaRecieving(None, True, "raniaData.json")
                is_data_uploaded = True
            else:
                tk.messagebox.showwarning("Televisit", "No such data found, using default.")

        print("Success")
        patient_interface()

    else:
        fail = tk.Label(root, text='The username or password entered is incorrect',
                    bg='#002855', fg='red')
        fail.config(font=('helvetica', 18))
        canvas.create_window(600, 300, window=fail)

def createAccount():
    canvas.delete("all")
        
login = tk.Button(root, text="Login", padx=50, pady=10, fg="white",
                     bg="#EAAA00", font=('arial', 18), command=checkLogin)

signup = tk.Button(root, text="Sign Up", padx=50, pady=10, fg="white",
                     bg="#EAAA00", font=('arial', 18), command=createAccount)

#all doctor interface information needed to create doctor's interface
call_initiated = tk.Label(root, text='', font = ('arial', 26),
                                            bg='#002855', fg='#EAAA00')

#all patient interface information


#function that is called when the start call button is clicked
def startCall():
    global current_doctor_un
    canvas.create_window(600, 100, window = call_initiated)
    if current_doctor_un == None:

        hasmadecall = path.exists("urlcommunicator.txt")

        if hasmadecall == True:
            ji.getURL()
            URL = ji.getCurrentURL()
            ji.openURL(URL)
            call_initiated['text'] = "Calling..."
        else:
            call_initiated['text'] = "Wait for your doctor to set up the call, then try again."

    else:
        ji.newURL(current_doctor_un)
        ji.dumpURL()
        ji.openURL(ji.getCurrentURL())
        call_initiated['text'] = "Calling..."

    root.attributes("-topmost", True)
    canvas.create_window(600, 100, window = call_initiated)
 

def help_func():
    print("Help function loading now...")
    help_txt = tk.Tk()
    help_txt.title("Help")

    help_canvas = tk.Canvas(help_txt, height=500, width=1100, bg="#002855")
    help_canvas.pack()

    sign_up = tk.Label(help_txt, text='Press Sign Up button to create a new account.\n', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))

    log_in = tk.Label(help_txt, text='Press Login button to log into your account.\n', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))

    start_c = tk.Label(help_txt, text='Press Start Call button to begin a call with your doctor.\n', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))

    end_c = tk.Label(help_txt, text='Press End Call button to end call.\n', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))

    send_d = tk.Label(help_txt, text='Press Upload Saved Data button to send medical information to your doctor.\n', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))
                         
    record_d = tk.Label(help_txt, text='Press Record Medical Data button to record your information.\n', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))
                         
    log_o = tk.Label(help_txt, text='Press Log Out to log out of your account.\n', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))
    

    help_canvas.create_window(550, 50, window = sign_up)
    help_canvas.create_window(550, 125, window = log_in)
    help_canvas.create_window(550, 200, window = start_c)
    help_canvas.create_window(550, 275, window = end_c)
    help_canvas.create_window(550, 350, window = send_d)
    help_canvas.create_window(550, 425, window = record_d)
    help_canvas.create_window(550, 495, window = log_o)


temperature = "N/A"
pressure = "N/A"
pulse = "N/A"
weight = "N/A"
height = "N/A"

def save(tempEntry, bloodEntry, pulseEntry, weightEntry, heightEntry, fromWindow=True):
    if fromWindow:
        print("Saving entered medical info...")
        temperature = tempEntry.get()
        pressure = bloodEntry.get()
        pulse = pulseEntry.get()
        weight = weightEntry.get()
        height = heightEntry.get()
    else:
        temperature = tempEntry
        pressure = bloodEntry
        pulse = pulseEntry
        weight = weightEntry
        height = heightEntry

    data.height_input(height)
    data.weight_input(weight)
    data.pressure_input(pressure)
    data.pulse(pulse)
    data.temperature_input(temperature)

    showTemp = tk.Label(root, text="Temperature: " + str(temperature) + " degrees",
                        bg='#002855', fg='#EAAA00', font = ('arial', 20))
    showBlood = tk.Label(root, text="Blood Pressure: "+str(pressure), bg='#002855',
                        fg='#EAAA00', font = ('arial', 20))
    showPulse = tk.Label(root, text="Pulse: " + str(pulse) + " bpm", bg='#002855',
                        fg='#EAAA00', font = ('arial', 20))
    showWeight = tk.Label(root, text="Weight: " + str(weight) + " lbs", bg='#002855',
                        fg='#EAAA00', font = ('arial', 20))
    showHeight = tk.Label(root, text="Height: " + str(height) + " feet", bg='#002855',
                          fg='#EAAA00', font = ('arial', 20))
    
    canvas.create_window(350, 400, window = showTemp)
    canvas.create_window(350, 450, window = showBlood)
    canvas.create_window(350, 500, window = showPulse)
    canvas.create_window(350, 550, window = showWeight)
    canvas.create_window(350, 600, window = showHeight)

def record():
    print("Recording medical data now...")
    record_root = tk.Tk()
    record_root.title("Record New Measurements & Enter Them Here:")

    record_canvas = tk.Canvas(record_root, height=375, width=600, bg="#002855")
    record_canvas.pack()

    templabel = tk.Label(record_root, text='Enter Temperature (F)', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))
    tempEntry = tk.Entry(record_root, width=5, font=('helvetica', 20))

    bloodlabel = tk.Label(record_root, text='Enter Blood Pressure', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))
    bloodEntry = tk.Entry(record_root, width=5, font=('helvetica', 20))

    pulselabel = tk.Label(record_root, text='Enter Pulse (bpm)', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))
    pulseEntry = tk.Entry(record_root, width=5, font=('helvetica', 20))

    weightlabel = tk.Label(record_root, text='Enter Current Weight in lbs', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))
    weightEntry = tk.Entry(record_root, width=5, font=('helvetica', 20))

    heightlabel = tk.Label(record_root, text='Enter Height in Feet', bg='#002855', fg='#EAAA00',
                         font = ('arial', 20))
    heightEntry = tk.Entry(record_root, width=5, font=('helvetica', 20))

    record_canvas.create_window(200, 50, window = templabel)
    record_canvas.create_window(500, 50, window = tempEntry)

    record_canvas.create_window(200, 100, window = bloodlabel)
    record_canvas.create_window(500, 100, window = bloodEntry)

    record_canvas.create_window(200, 150, window = pulselabel)
    record_canvas.create_window(500, 150, window = pulseEntry)

    record_canvas.create_window(200, 200, window = weightlabel)
    record_canvas.create_window(500, 200, window = weightEntry)

    record_canvas.create_window(200, 250, window = heightlabel)
    record_canvas.create_window(500, 250, window = heightEntry)

    save_data = tk.Button(record_root, text="Save Data", padx = 35, pady=8,
                             fg="white", bg="#EAAA00", font=('arial', 20),
                             command = lambda:[save(tempEntry, bloodEntry, pulseEntry,
                                                    weightEntry, heightEntry),
                                               record_root.destroy()])
    record_canvas.create_window(300, 325, window = save_data)


def upload():
    print("Uploading data to doctor...")
    #put function for actually uploading the data here
    data.raniaBroadcast(True)

    uploadedLabel = tk.Label(root, text='Successfully uploaded data to doctor',
                             bg='#002855', fg='#EAAA00', font = ('arial', 24))

    canvas.create_window(850, 500, window = uploadedLabel)

#function that is called when logout is clicked
def wrapup():
    if path.exists("urlcommunicator.txt"):
        os.remove("urlcommunicator.txt")
    if path.exists("send.json"):
        os.remove("send.json")
    if current_doctor_un is None:
        if tk.messagebox.askyesno("Televisit", "Would you like to send your last recorded medical data to the Rania system?"):
            data.raniaBroadcast(True, "raniaData.json")


def view_patient_info():
    print("Retrieving patient info...")
    if path.exists("send.json"):
        data.raniaRecieving(None, True)
        temperature = data.temp
        pressure = data.blood
        pulse = data.pul
        weight = data.lbs
        height = data.ft

        showTemp = tk.Label(root, text="Temperature: " + str(temperature) + " degrees",
                            bg='#002855', fg='#EAAA00', font = ('arial', 20))
        showBlood = tk.Label(root, text="Blood Pressure: "+str(pressure), bg='#002855',
                            fg='#EAAA00', font = ('arial', 20))
        showPulse = tk.Label(root, text="Pulse: " + str(pulse) + " bpm", bg='#002855',
                            fg='#EAAA00', font = ('arial', 20))
        showWeight = tk.Label(root, text="Weight: " + str(weight) + " lbs", bg='#002855',
                            fg='#EAAA00', font = ('arial', 20))
        showHeight = tk.Label(root, text="Height: " + str(height) + " feet", bg='#002855',
                            fg='#EAAA00', font = ('arial', 20))
        
        canvas.create_window(350, 400, window = showTemp)
        canvas.create_window(350, 450, window = showBlood)
        canvas.create_window(350, 500, window = showPulse)
        canvas.create_window(350, 550, window = showWeight)
        canvas.create_window(350, 600, window = showHeight)

    else:
        retrievingLabel = tk.Label(root, text="No patient data found.\nPlease wait for the patient to send data.",
                            bg='#002855', fg='#EAAA00', font = ('arial', 20))

        canvas.create_window(350, 400, window = retrievingLabel)



def notes():
    notes_root = tk.Tk()
    notes_root.title("Notes")

    if path.exists("notes.txt"):
        with open("notes.txt","r+") as f:
            saved_notes = f.read().rstrip()
    else:
        saved_notes = ""

    def closing_notes(saved_notes):
        if saved_notes == text.get(1.0, tk.END):
            notes_root.destroy()
        elif 'yes' == messagebox.askquestion("Exit Notes", "Do you want to save your notes before exiting?"):
            saved_notes = text.get(1.0, tk.END)
            with open("notes.txt", "w+") as f:
                f.write(saved_notes)
            notes_root.destroy()
        else:
            notes_root.destroy()
            
    notes_root.protocol("WM_DELETE_WINDOW", lambda:[closing_notes(saved_notes)])

    text = tk.Text(notes_root, height = 40, width = 80)
    text.pack()

    text.insert(tk.END, saved_notes)

def doctor_interface():
    canvas.delete("all")

    startcall_button = tk.Button(root, text="Start Call", padx = 50, pady=10,
                             fg="white", bg="green", font=('arial', 24),
                             command = startCall)
    logout = tk.Button(root, text="Log Out", padx = 40, pady=8,
                             fg="white", bg="#EAAA00", font=('arial', 16),
                             command = lambda:[(wrapup(), login_screen())])
    help_button = tk.Button(root, text = "Help", padx = 40, pady=8,
                            fg="white", bg="#EAAA00", font=('arial', 16),
                             command = help_func)
    viewinfo_button = tk.Button(root, text="View Patient Info", padx = 50, pady=10,
                             fg="white", bg="#EAAA00", font=('arial', 26),
                             command = view_patient_info)
    write_notes = tk.Button(root, text = "View/Edit Notes",
                            padx = 20, pady=8, fg="white", bg="#EAAA00",
                            font=('arial', 26), command = notes)

    canvas.create_window(600, 175, window = startcall_button)
    canvas.create_window(150, 50, window = logout)
    canvas.create_window(1050, 50, window = help_button)
    canvas.create_window(350, 300, window = viewinfo_button)
    canvas.create_window(850, 300, window = write_notes)

def login_screen():
    canvas.delete("all")

    userEntry.delete(0, 100)
    passEntry.delete(0, 100)
    
    canvas.create_window(600, 370, window=userlabel)
    canvas.create_window(600, 475, window=passlabel)

    canvas.create_window(600, 410, window=userEntry)
    canvas.create_window(600, 515, window=passEntry)

    canvas.create_window(700, 600, window=login)
    canvas.create_window(500, 600, window=signup)

    canvas.create_window(600, 175, window = login_title)
    

def patient_interface():
    canvas.delete("all")

    startcall_button = tk.Button(root, text="Start Call", padx = 50, pady=10,
                             fg="white", bg="green", font=('arial', 24),
                             command = startCall) 
    logout = tk.Button(root, text="Log Out", padx = 40, pady=8,
                             fg="white", bg="#EAAA00", font=('arial', 16),
                             command = lambda:[(wrapup(), login_screen())])
    help_button = tk.Button(root, text = "Help", padx = 40, pady=8,
                            fg="white", bg="#EAAA00", font=('arial', 16),
                             command = help_func)
    record_data = tk.Button(root, text = "Record Medical Data", padx = 20,
                            pady=8, fg="white", bg="#EAAA00", font=('arial', 26),
                             command = record)
    upload_data = tk.Button(root, text = "Upload Saved Data",
                            padx = 20, pady=8, fg="white", bg="#EAAA00",
                            font=('arial', 26), command = upload)

    if is_data_uploaded:
        save(data.temp, data.blood, data.pul, data.lbs, data.ft, False)

    canvas.create_window(600, 175, window = startcall_button)
    canvas.create_window(150, 50, window = logout)
    canvas.create_window(1050, 50, window = help_button)
    canvas.create_window(350, 300, window = record_data)
    canvas.create_window(850, 300, window = upload_data)

    
login_screen()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        wrapup()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
