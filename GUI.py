import tkinter
from tkinter import *
import main as mm
import people as pp
import timeRange as tm
from PIL import ImageTk, Image

window = Tk()

window.title("Welcome Scheduler By Navid A. Ehyaee")

window.geometry('350x350')
frame = Frame(window, width=100, height=100)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)


lbl = Label(window, text="Please Enter the start and end of your budy schedules\n in this format: HH:MM, HH.MM")


lbl.grid(column=175, row=0)

txt = Entry(window,width=20)

txt.grid(column=175, row=2)

list = []
global i
i= 1

def clicked():
    global i
    res = f"Please Enter the start and end of your budy schedules\n in this format: HH:MM, HH:MM\nAdded {i} Schedule(s)"

    lbl.configure(text= res)
    list.append(txt.get())
    i +=1
    txt.delete(0,tkinter.END) # erase after use

btn = Button(window, text="Add Busy Time", command=clicked)


def clicked2():
    print(list)
    if len(list) == 0 or list[0] == '':
        list.clear()
        list.append("24:00, 24:00")
    p = pp.People("")

    for i in list:

        p.add_busy_intervals(tm.TimeRange(str(i).split(',')[0],str(i).split(',')[1][1:]))

    res = mm.main()
    res = "Please Enter the start and end of your budy schedules\n in this format: HH:MM, HH.MM\n" + res
    lbl.configure(text= res)


btn2 = Button(window, text="results", command=clicked2)


btn.grid(column=175, row=3)
btn2.grid(column=175, row=4)


window.mainloop()
