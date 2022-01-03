from tkinter import *
from datetime import datetime
from playsound import playsound

bgColor = "#BEC2CB"

root = Tk()
root.geometry("1920x1080")
root.configure(bg=bgColor)

alarmList = []

# TODO make first alarm go to next alarm
# TODO Make next alarm go off when time
# TODO Add "X"
# TODO Find a way to have a while loop checking for the time while the root main loop runs

def get_time():
    return datetime.now().strftime("%H:%M") if str(datetime.now().strftime("%H:%M"))[0] != "0" \
        else str(datetime.now().strftime("%H:%M"))[1:]



def set_screen():
    global gui, hours_entry, minutes_entry, meridiam_entry, meridiam, alarms, alarmList
    meridiam = "am"
    hours_entry = StringVar()
    hours_entry.set("")
    minutes_entry = StringVar()
    minutes_entry.set("")
    alarms = [
        Label(root, text="       ")
    ]
    gui = [
        Label(root, text="Next Alarm"),
        Label(root, text="N/A"),
        Entry(root, textvariable=hours_entry, width=3),
        Entry(root, textvariable=minutes_entry, width=3),
        Label(root, text="am"),
        Button(root, text="^", command=time_of_day),
        Button(root, text="Submit", command=add_alarm)
    ]
    gui[0].grid(row=0, column=2)
    gui[1].grid(row=1, column=2)
    gui[2].grid(row=4, column=1)
    gui[3].grid(row=4, column=2)
    gui[4].grid(row=4, column=3)
    gui[5].grid(row=3, column=3)
    gui[6].grid(row=4, column=4)
    alarms[0].grid(row=2, column=0)


def time_of_day():
    global meridiam
    if meridiam == "am":
        meridiam = "pm"
        gui[4].configure(text=meridiam)
    else:
        meridiam = "am"
        gui[4].configure(text=meridiam)


def add_alarm():
    global meridiam
    successful_alarm = True
    if len(alarmList) != 28:
        try:
            hours = int(gui[2].get())
            if hours > 12:
                hours = "12"
                hours_entry.set(hours)
            else:
                hours = str(hours)
        except:
            successful_alarm = False
            hours_entry.set("")
        try:
            minutes = int(gui[3].get())
            if minutes > 59:
                minutes = "59"
                minutes_entry.set(minutes)
            elif minutes < 10:
                minutes = "0" + str(minutes)
            else:
                minutes = str(minutes)
        except:
            successful_alarm = False
            minutes_entry.set("")
        new_alarm = "{}:{}{}".format(hours, minutes, meridiam)
        if successful_alarm and military_time(new_alarm) != get_time() and new_alarm not in alarmList:
            print("through to insert_alarm")
            insert_alarm(new_alarm)


def insert_alarm(alarm):
    global alarmList
    inserted = False
    if len(alarmList) == 0:
        print("first alarm")
        alarmList.append(alarm)
        index = 0
        alarms[index].configure(text=alarm)
    else:
        index = -1
        for i in range(len(alarmList)):
            current_time = military_time(alarmList[i])
            new_time = military_time(alarm)
            time_to_current = time_dif(current_time)
            time_to_new = time_dif(new_time)
            if time_to_current > time_to_new:
                inserted = True
                index = i
                alarmList.insert(index, alarm)
                alarms.insert(index, Label(root, text=alarm))
                break
        if index == -1:
            alarmList.append(alarm)
            alarms.append(Label(root, text=alarm))
            alarms[len(alarmList) - 1].grid(row=2, column=len(alarmList) -1)
    if inserted:
        for i in range(len(alarmList[index:])):
            alarms[index].configure(text=alarm)
            alarms[index+i].grid(row=2, column=index+i)


# ex makes 2:00pm to 14:00
# used for figuring out alarm order in connection to current time
def military_time(time):
    index = time.find(":")
    if time[-2:] == "pm":
        military_hour = int(time[:index]) + 12
    else:
        military_hour = int(time[:index])
    if military_hour == 12 or military_hour == 24:
        military_hour -= 12
    return str(military_hour) + time[index:-2]


def time_dif(alarm):
    current_hour = int(str(get_time())[:str(get_time()).find(":")])
    alarm_hour = int(str(alarm)[:str(alarm).find(":")])
    current_min = int(str(get_time())[str(get_time()).find(":")+1:])
    alarm_min = int(str(alarm)[str(alarm).find(":")+1:])
    hour_dif = alarm_hour - current_hour
    min_dif = alarm_min - current_min
    if min_dif < 0:
        min_dif += 60
        hour_dif -= 1
    if hour_dif < 0:
        hour_dif += 24
    return min_dif + (hour_dif * 60)


def alarm_goes_off():
    playsound('touchdownraiders.mp3')


root.title("Alarm")
set_screen()

root.mainloop()
