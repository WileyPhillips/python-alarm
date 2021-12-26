from tkinter import *

bgColor = "#BEC2CB"

root = Tk()
root.geometry("1920x1080")
root.configure(bg=bgColor)

alarmList = []


def set_screen():
    global gui, hours_entry, minutes_entry, am_pm_entry, amPm, alarms, alarmList
    amPm = "am"
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
    global amPm
    if amPm == "am":
        amPm = "pm"
        gui[4].configure(text=amPm)
    else:
        amPm = "am"
        gui[4].configure(text=amPm)


def add_alarm():
    global amPm
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
        new_alarm = "{}:{}{}".format(gui[2].get(), gui[3].get(), amPm)
        if successful_alarm:
            insert_alarm(new_alarm)
            alarms[0].configure(text=new_alarm)


def insert_alarm(alarm):
    global alarmList
    if len(alarmList) == 0:
        alarmList.append(alarm)
        index = 0
    else:
        alarmList.append(alarm)
        index = 0
        alarms.insert(index, Label(root, text=alarm))
    alarms[index].configure(text=alarm)
    for i in range(len(alarmList[index:])):
        alarms[index+i].grid(row=2, column=index+i)

root.title("Alarm")
set_screen()

root.mainloop()
