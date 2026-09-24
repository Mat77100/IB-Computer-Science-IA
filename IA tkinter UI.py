#main tkinter UI
import tkinter as tk

Main = tk.Tk("Reminder App")
Main.geometry("1000x600")
Main.configure(bg="dark grey")
Main.title("Reminder App")


ReminderCanvas = tk.Canvas(Main)

RemiderScrollBar = tk.Scrollbar(Main)
RemiderScrollBar.config(command=ReminderCanvas.yview,troughcolor="black",bg="light grey")
ReminderCanvas.config(yscrollcommand=RemiderScrollBar.set,bg="grey",width=700,highlightthickness=0)

RemiderScrollBar.pack(side="right",fill="y")
ReminderCanvas.pack(side=("right"),fill="both",padx=15,pady=15)

ReminderFrameList = tk.Frame(ReminderCanvas)
ReminderWindow = ReminderCanvas.create_window((0,0),window=ReminderFrameList, anchor="nw")
ReminderFrameList.bind("<Configure>", lambda event: ReminderCanvas.configure(scrollregion=ReminderCanvas.bbox("all")))
ReminderCanvas.bind("<Configure>", lambda event: ReminderCanvas.itemconfigure(ReminderWindow,width=event.width))
ReminderCanvas.bind_all("<MouseWheel>", lambda event: ReminderCanvas.yview_scroll(-int(event.delta/120),"units"))
ReminderFrameList.configure(bg="Grey")

def TEST():
    testReminder = tk.Frame(ReminderFrameList,bg="blue",height=100)
    testRemindertext = tk.Label(testReminder, text="HELLO WORLD")
    testRemindertext.pack()
    testReminder.pack(fill="x",padx=10,pady=10,)
    testReminder.pack_propagate(False)

AddNewReminderTest = tk.Button(Main,command=TEST,text="New Reminder TEST")
AddNewReminderTest.pack(side="bottom",anchor="w",padx=10,pady=10)

Main.mainloop()