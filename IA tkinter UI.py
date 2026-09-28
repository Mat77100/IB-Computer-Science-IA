#main tkinter UI
import tkinter as tk


#COLOUR PALETTE HEX CODE(dark --> light):
"#141414"
"#4F4F4F"
"#878787"
"#A6A6A6"
"#D1D1D1"


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

def CreateReminder():
    ReminderObj = Reminder(Main,"Reminder","","TESTING","01/01/27","low","N/A") #Might be worth refrencing the reminder obj into a list of sorts in order to make saving easier
    ReminderObj.Edit()
    NewReminder = tk.Frame(ReminderFrameList,bg="white",height=100)
    NewReminder.config(bg="#A6A6A6")
    Text = tk.Label(NewReminder,text=ReminderObj.Title)
    Description = tk.Label(NewReminder,text=ReminderObj.Description)
    Categories = tk.Label(NewReminder,text=ReminderObj.Categories)
    DueDate = tk.Label(NewReminder,text=ReminderObj.DueDate)
    Priority = tk.Label(NewReminder,text=ReminderObj.Priority)
    Attachments = tk.Label(NewReminder,text=ReminderObj.Attachments)

    Text.pack()
    Description.pack()
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
            NewReminder.destroy()

    DelBtn = tk.Button(NewReminder,text=f"Delete: x{ReminderObj.DeleteConfirm}",command=DeleteReminder,bg="red")
    EditBtn = tk.Button(NewReminder,text="Edit",command=lambda:ReminderObj.Edit(UpdateReminder))
    EditBtn.pack()
    DelBtn.pack()
    NewReminder.pack(fill="x",padx=10,pady=10)




AddNewReminderTest = tk.Button(Main,command=CreateReminder,text="New Reminder")
AddNewReminderTest.pack(side="bottom",anchor="w",padx=10,pady=10)

Main.mainloop()