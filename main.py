from tkinter import *

bgColor = "#BEC2CB"

root = Tk()
root.geometry("1920x1080")
root.configure(bg=bgColor)


def set_screen():
    global gui, text_entry, am_pm_entry, amPm
    amPm = "am"
    text_entry = StringVar()
    text_entry.set("N/A")
    am_pm_entry = StringVar()
    am_pm_entry.set(amPm)
    alarms = [
        Label(root, text="       ")
    ]
    gui = [
        Label(root, text="Next Alarm"),
        Label(root, textvariable=text_entry),
        Entry(root),
        Entry(root),
        Label(root, textvariable=am_pm_entry),
        Button(root, text="^"),
        Button(root, text="v"),
        Button(root, text="^"),
        Button(root, text="v"),
        Button(root, text="^", command=time_of_day)
    ]
    gui[0].grid(row=0, column=2)
    gui[1].grid(row=1, column=2)
    gui[2].grid(row=4, column=1)
    gui[3].grid(row=4, column=2)
    gui[4].grid(row=4, column=3)
    gui[5].grid(row=3, column=1)
    gui[6].grid(row=5, column=1)
    gui[7].grid(row=3, column=2)
    gui[8].grid(row=5, column=2)
    gui[9].grid(row=3, column=3)
    alarms[0].grid(row=2, column=0)


# ERROR need to get label text
def time_of_day():
    global amPm
    if amPm == "am":
        amPm = "pm"
        am_pm_entry.set(amPm)
    else:
        amPm = "am"
        am_pm_entry.set(amPm)


root.title("Alarm")
set_screen()

root.mainloop()
