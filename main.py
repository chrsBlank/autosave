import tkinter.messagebox
import tkinter
from pynput.keyboard import Key, Controller
import time

root = tkinter.Tk()
root.wm_attributes("-topmost", 1)
root.withdraw()

keyboard = Controller()
settings = open("settings.config", "r")
settings = settings.read()
settings = settings.split("\n")
list = []
for i in settings:
    list.append(i.split(":"))
timetowaits = int(list[0][1])
timetowait = timetowaits * 60
eyestrain = list[2][1]
water = list[3][1]
language = list[1][1]

if eyestrain == 1:
    tn = time.time()
    t202020 = time.time()
else:
    t202020 = 0

if water == 1:
    wt = time.time()
    tw = time.time()
else:
    tw = 0

t4p = time.time()

def Save():
    print("saving")
    keyboard.press(Key.ctrl)
    keyboard.press("s")
    keyboard.release(Key.ctrl)
    keyboard.release("s")

stop = False

while stop == False:
    time.sleep(30)
    if tw != 0:
        if time.time() - tw > 1800:
            if "en" in language:
                tkinter.messagebox.showinfo(message="You have been working for 30 minutes, drink some water")
            elif "gr" in language:
                tkinter.messagebox.showinfo(message="Έχετε δουλέψει για 30 λεπτά, πιείτε λίγο νερό")
            tw = time.time()
    if t202020 != 0:
        print('enabled eyestrain')
        t202020 = time.time()
        if t202020 - tn > 1050:
            if "en" in language:
                tkinter.messagebox.showinfo(message="You have been working for 20 minutes, take a break of 20 seconds and look at something 20 meters away")
            elif "gr" in language:
                tkinter.messagebox.showinfo(message="Έχετε δουλέψει για 20 λεπτά, πάρτε ένα διάλειμμα 20 δευτερολέπτων και κοιτάξτε κάτι 20 μετρα μακριά")
            tn = time.time()
    timetowait = timetowaits * 60
    if time.time() - t4p > timetowait:
        if "en" in language:
            answer = tkinter.messagebox.askyesnocancel(message="Do you want to save?\n if you want to change settings, open the setting.config file")
        elif "gr" in language:
            answer = tkinter.messagebox.askyesnocancel(message="Θέλετε να αποθηκεύσετε; \n αν θέλετε να αλλάξετε τις ρυθμίσεις, ανοίξτε το αρχείο setting.config")
        else:
            answer = tkinter.messagebox.askyesnocancel(message="Θέλετε να αποθηκεύσετε; \n αν θέλετε να αλλάξετε τις ρυθμίσεις, ανοίξτε το αρχείο setting.config")
        if answer == True:
            Save()
        elif answer == False:
            pass
        elif answer == None:
            stop = True
        else:
            print("error: problem with the popup")
        t4p = time.time()