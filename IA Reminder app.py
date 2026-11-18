#main tkinter UI
import tkinter as tk


#COLOUR PALETTE HEX CODE(dark --> light):
"#141414"
"#4F4F4F"
"#878787"
"#A6A6A6"
"#D1D1D1"

'''

FIX UR FORMATTING MATE
mainly:
edit window needs info on what each entry is for (title, description, etc.)
the formatting of the reminder data on the frame,
thats all i can think of for now
oh and fix bugs (obv)

known bugs:
u can open multiple edit windows
closing the edit window when making a new reminder adds it anyway


'''

Main = tk.Tk()
Main.geometry("1000x600")
Main.configure(bg="#878787")
Main.title("Reminder App")


ReminderCanvas = tk.Canvas(Main)

RemiderScrollBar = tk.Scrollbar(Main)
RemiderScrollBar.config(command=ReminderCanvas.yview,troughcolor="black",bg="light grey")
ReminderCanvas.config(yscrollcommand=RemiderScrollBar.set,bg="#4F4F4F",width=700,highlightthickness=0)

RemiderScrollBar.pack(side="right",fill="y")
ReminderCanvas.pack(side=("right"),fill="both",padx=15,pady=15)

ReminderFrameList = tk.Frame(ReminderCanvas)
ReminderWindow = ReminderCanvas.create_window((0,0),window=ReminderFrameList, anchor="nw")
ReminderFrameList.bind("<Configure>", lambda event: ReminderCanvas.configure(scrollregion=ReminderCanvas.bbox("all")))
ReminderCanvas.bind("<Configure>", lambda event: ReminderCanvas.itemconfigure(ReminderWindow,width=event.width))
ReminderCanvas.bind_all("<MouseWheel>", lambda event: ReminderCanvas.yview_scroll(-int(event.delta/120),"units"))
ReminderFrameList.configure(bg="#4F4F4F")

class Reminder():
    def __init__(self,Tk,Title,Description,Categories,DueDate,Priority,Attachments):
        self.Main = Tk
        self.Title = Title
        self.Description = Description
        self.Categories = Categories
        self.DueDate = DueDate
        self.Priority = Priority
        self.Attachments = Attachments
        self.DeleteConfirm = 3
    def Edit(self, On_update=None):
        Editor = tk.Toplevel(self.Main)
        Editor.title("Edit")
        Editor.geometry("300x200")
        ChangedTitle = tk.Entry(Editor)
        ChangedTitle.insert(0,self.Title)

        ChangedDescription = tk.Entry(Editor)
        ChangedDescription.insert(0,self.Description)

        ChangedCategories = tk.Entry(Editor)
        ChangedCategories.insert(0,self.Categories)

        ChangedDueDate = tk.Entry(Editor)
        ChangedDueDate.insert(0,self.DueDate)

        ChangedPriority = tk.Entry(Editor)
        ChangedPriority.insert(0,self.Priority)

        ChangedAttachments = tk.Entry(Editor)
        ChangedAttachments.insert(0,self.Attachments)


        ChangedTitle.pack()
        ChangedDescription.pack()
        ChangedCategories.pack()
        ChangedDueDate.pack()
        ChangedPriority.pack()
        ChangedAttachments.pack() #DONT FORGET TO CHANGE THE LAYOUT OF THESE TO REFLECT THE REMINDERS ON THE LIST

        def Save():
            self.Title = ChangedTitle.get()
            self.Description = ChangedDescription.get()
            self.Categories = ChangedCategories.get() #MAKE SURE TO LIMIT TO EXISTING CATEGORIES
            self.DueDate = ChangedDueDate.get()
            self.Priority = ChangedPriority.get() #CHANGE TO LIMIT TO SPECIFIC PRIORITYS (LOW MEDIUM HIGH)
            self.Attachments = ChangedAttachments.get() #NEEDS TO BE CHANGED TO SUPPORT ATTACHMENTS

            if On_update:
                On_update()

            Editor.destroy()

        def Cancel():
            Editor.destroy()

        

        SaveBtn = tk.Button(Editor,command=Save,text="Save",width=20)
        CancelBtn = tk.Button(Editor,command=Cancel,text="Cancel",width=20)

        SaveBtn.place(relx=1.0,rely=1.0,anchor="se")
        CancelBtn.place(relx=0.0,rely=1,anchor="sw")
        Editor.wait_window()

'''
def TEST():
    testReminder = tk.Frame(ReminderFrameList,bg="blue",height=100)
    testRemindertext = tk.Label(testReminder, text="HELLO WORLD")
    testRemindertext.pack()
    testReminder.pack(fill="x",padx=10,pady=10,)
    testReminder.pack_propagate(False)
    tk.Button(testReminder,command=testReminder.destroy).pack()
'''

ReminderObjReferences = []

'''
BIG ISSUE: Basically, creating a reminder opens the edit window, but pressing cancle still creates it
'''

def CreateReminder(Title, Description, Categories, DueDate, Priority, Attachments, Open_editor, ReminderObj): #for reminderObj, feed in old one if needed, otherwise feed False
    if not ReminderObj:
        ReminderObj = Reminder(Main,Title,Description,Categories,DueDate,Priority,Attachments) 
    if Open_editor:
        ReminderObj.Edit()
    NewReminder = tk.Frame(ReminderFrameList,bg="white",height=100)
    NewReminder.config(bg="#A6A6A6")
    Text = tk.Label(NewReminder,text=ReminderObj.Title,bg="#6B6B6B",fg="#FFFFFF",font=("",25,"bold"),wraplength=300, justify="left")
    Description = tk.Label(NewReminder,text=ReminderObj.Description,bg="#6B6B6B",fg="#FFFFFF",font=("",10,"bold"))
    Categories = tk.Label(NewReminder,text=ReminderObj.Categories)
    DueDate = tk.Label(NewReminder,text=ReminderObj.DueDate)
    Priority = tk.Label(NewReminder,text=ReminderObj.Priority)
    Attachments = tk.Label(NewReminder,text=ReminderObj.Attachments)

    Text.pack(anchor="w", padx=5,pady=5)
    Description.pack(anchor="w", padx=5)
    Categories.pack()
    DueDate.pack()
    Priority.pack()
    Attachments.pack()

    def UpdateReminder():
        Text.config(text=ReminderObj.Title)
        Description.config(text=ReminderObj.Description)
        Categories.config(text=ReminderObj.Categories)
        DueDate.config(text=ReminderObj.DueDate)
        Priority.config(text=ReminderObj.Priority)
        Attachments.config(text=ReminderObj.Attachments)

    def DeleteReminder():
        if ReminderObj.DeleteConfirm != 1:
            ReminderObj.DeleteConfirm -= 1
            DelBtn.config(text=f"Delete: x{ReminderObj.DeleteConfirm}")
            return
        else:
            ReminderObjReferences.remove(ReminderObj)
            NewReminder.destroy()

    DelBtn = tk.Button(NewReminder,text=f"Delete: x{ReminderObj.DeleteConfirm}",command=DeleteReminder,bg="red")
    EditBtn = tk.Button(NewReminder,text="Edit",command=lambda:ReminderObj.Edit(UpdateReminder)) #DISABLE WHEN EDIT WINDOW IS OPEN
    EditBtn.pack()
    DelBtn.place(relx=0.961,rely=0.061, anchor="center")
    NewReminder.pack(fill="x",padx=10,pady=10)
    if ReminderObj not in ReminderObjReferences:
        ReminderObjReferences.append(ReminderObj) #This rat bastard caused me a few issus, first it alawys duplicated reminders when using a search, then it would straight up remove them, fixed now

def SaveReminders():
    with open("ReminderEntries.txt","w") as ReminderEntries:
        for reminder in ReminderObjReferences: #possibly dont need thr **NEXT** as you know what each line is. altho u might want to keep just as like a chekck wheterh the next line hasa reminder
                #ReminderEntries.write("**NEXT**\n") #MAKE SURE TO STOP USER FROM INPUTTING THIS IN ANY FEILD, JUST IN CASE. THIS IS TO CLASSIFY WHEN THE NEXT REMINDER IS
                ReminderEntries.write(reminder.Title +"\n") #\n appends each to a new line
                ReminderEntries.write(reminder.Description +"\n")
                ReminderEntries.write(reminder.Categories +"\n")
                ReminderEntries.write(reminder.DueDate +"\n")
                ReminderEntries.write(reminder.Priority +"\n")
                ReminderEntries.write(reminder.Attachments +"\n") #fix later, possible remove it
    Main.destroy() #This is so that it actually closes


AddNewReminderTest = tk.Button(Main,command=lambda:CreateReminder("Reminder","","TESTING","01/01/27","low","N/A",True,False),text="New Reminder")
AddNewReminderTest.pack(side="bottom",anchor="w",padx=10,pady=10)

Main.protocol("WM_DELETE_WINDOW", SaveReminders) #Rebinds the x button that usally closes the window, rebinded to save fundtion

#Readd saved reminders
try:
    with open("ReminderEntries.txt","r") as SavedReminders:
        Entries = SavedReminders.readlines() #stores every line in the file
        if Entries: #check to see if there are reminders
            for i in range(0, len(Entries),6):
                ReminderData = Entries[i:i+6]
                CreateReminder(ReminderData[0].strip(),ReminderData[1].strip(),ReminderData[2].strip(),ReminderData[3].strip(),ReminderData[4].strip(),ReminderData[5].strip(),False,False)

except:
    pass #just to prevent an error when the file isnt there, like if the program has not ran for the first time


#REMINDER SORTING, YAYYYYYYYYY
SearchLabel = tk.Label(Main,text="Search: ",bg="#878787")
SearchBar = tk.Entry(Main)
SearchSelect = tk.BooleanVar(value=False) #check box only changes tkinter variables



def Filter_with_search(SearchSelect): 
    if SearchBar.get() == "":
        for Frames in ReminderFrameList.winfo_children(): #is this ineffecient, probably, does it work, eh
                Frames.destroy()
        for Reminder in ReminderObjReferences:
            CreateReminder(None,None,None,None,None,None,False,Reminder)
        return
        

    Results = []

    for ReminderObj in ReminderObjReferences:
        if SearchBar.get().lower() in ReminderObj.Title.lower():
            Results.append(ReminderObj)
        if SearchSelect.get() and (SearchBar.get().lower() in ReminderObj.Description.lower()):
            Results.append(ReminderObj)

    for Frames in ReminderFrameList.winfo_children():
        Frames.destroy()

    for NewReminder in Results:
        CreateReminder(None,None,None,None,None,None,False,NewReminder)

SearchWithDescription = tk.Checkbutton(Main,text="Search description as well",onvalue=True,offvalue=False,variable=SearchSelect,bg="#878787",command=lambda:Filter_with_search(SearchSelect))

SearchBar.bind("<KeyRelease>", lambda event: Filter_with_search(SearchSelect))


SearchLabel.place(relx=0.02,rely=0.22)
SearchBar.place(relx=0.02,rely=0.25)
SearchWithDescription.place(relx=0.02,rely=0.30)

Main.mainloop()