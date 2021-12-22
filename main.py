from tkinter import *

bgColor = "#BEC2CB"

root = Tk()
root.geometry("1920x1080")
root.configure(bg=bgColor)


def set_screen():
    global gui, text_entry, am_pm
    text_entry = StringVar()
    text_entry.set("N/A")
    alarms = [
        Label(root, text="       ")
    ]
    gui = [
        Label(root, text="Next Alarm"),
        Label(root, textvariable=text_entry),
        Entry(root),
        Entry(root),
        Label(root, text="am"),
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
    if gui[4].text == "am":
        gui[4].configure(text="pm")
    else:
        gui[4].configure(text="am")


root.title("Alarm")
set_screen()

root.mainloop()
