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

Main = tk.Tk() #Creates the main tkinter window
Main.geometry("1000x600")
Main.configure(bg="#878787") #Resize the window and colour it grey
Main.title("Reminder App") #Give a title


ReminderCanvas = tk.Canvas(Main) #Create a canvas

RemiderScrollBar = tk.Scrollbar(Main) #Scrrollbar creation
RemiderScrollBar.config(command=ReminderCanvas.yview) #Set scrollbar control to canvas yview
ReminderCanvas.config(yscrollcommand=RemiderScrollBar.set,bg="#4F4F4F",width=700,highlightthickness=0) #If the canvas is scrolled by something else, set the scrollbar to match.
                                                                                                        #Also sets the width and colour
RemiderScrollBar.pack(side="right",fill="y")
ReminderCanvas.pack(side=("right"),fill="both",padx=15,pady=15) #packs the tkinter widgets so they display

ReminderFrameList = tk.Frame(ReminderCanvas) #Creates the main frame that acts as the container for the other reminder frames
ReminderWindow = ReminderCanvas.create_window((0,0),window=ReminderFrameList, anchor="nw") #places the frame into the canvas
ReminderFrameList.bind("<Configure>", lambda event: ReminderCanvas.configure(scrollregion=ReminderCanvas.bbox("all"))) #Sets the scrollable area of the canvas to match the bounding box of the reminders
ReminderCanvas.bind("<Configure>", lambda event: ReminderCanvas.itemconfigure(ReminderWindow,width=event.width)) #Resize ReminderFrameList to be the same size as the canvas
ReminderCanvas.bind_all("<MouseWheel>", lambda event: ReminderCanvas.yview_scroll(-int(event.delta/120),"units")) #Binds the mousewheel to canvas scrolling
ReminderFrameList.configure(bg="#4F4F4F") #Change the colour of the frame

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
    def Edit(self, On_update=None): #Method that opens an editor, takes argument On_update, defults to None if nothing given
        Editor = tk.Toplevel(self.Main) #makes a tk toplevel
        Editor.title("Edit")
        Editor.geometry("300x200") #shrink the editor and give it a title
      
        ChangedTitle = tk.Entry(Editor) #makes an entry widget
        ChangedTitle.insert(0,self.Title) #Inserts the current value into the entry

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


        ChangedTitle.pack() #Displays the entrys
        ChangedDescription.pack()
        ChangedCategories.pack()
        ChangedDueDate.pack()
        ChangedPriority.pack()
        ChangedAttachments.pack() #DONT FORGET TO CHANGE THE LAYOUT OF THESE TO REFLECT THE REMINDERS ON THE LIST

        def Save(): #Save function to write the inputted data to their corresponding attributes
            self.Title = ChangedTitle.get()
            self.Description = ChangedDescription.get()
            self.Categories = ChangedCategories.get() #MAKE SURE TO LIMIT TO EXISTING CATEGORIES
            self.DueDate = ChangedDueDate.get()
            self.Priority = ChangedPriority.get() #CHANGE TO LIMIT TO SPECIFIC PRIORITIES (LOW MEDIUM HIGH)
            self.Attachments = ChangedAttachments.get() #NEEDS TO BE CHANGED TO SUPPORT ATTACHMENTS

            if On_update: #calls the inputted on_update function
                On_update()

            Editor.destroy() #closes the editor

        def Cancel(): #2nd function, opposite of saved
            Editor.destroy() #closes the editor, no attribute is changed

        

        SaveBtn = tk.Button(Editor,command=Save,text="Save",width=20) #Buttons created for saving and canceling the edit
        CancelBtn = tk.Button(Editor,command=Cancel,text="Cancel",width=20) #bound to the previous 2 functions

        SaveBtn.place(relx=1.0,rely=1.0,anchor="se") #places buttons at the bottom of editor
        CancelBtn.place(relx=0.0,rely=1,anchor="sw")
        Editor.wait_window() #waits until editor is closed then proceeds

'''
def TEST():
    testReminder = tk.Frame(ReminderFrameList,bg="blue",height=100)
    testRemindertext = tk.Label(testReminder, text="HELLO WORLD")
    testRemindertext.pack()
    testReminder.pack(fill="x",padx=10,pady=10,)
    testReminder.pack_propagate(False)
    tk.Button(testReminder,command=testReminder.destroy).pack()
'''

ReminderObjReferences = [] #List containing all reminder objects references
#Create reminder function, creates reminders. 8 arguments; 6 are data related to the reminder, such as the title, the other 2 are for the program (Open_editor, ReminderObj)
def CreateReminder(Title, Description, Categories, DueDate, Priority, Attachments, Open_editor, ReminderObj): #for reminderObj, feed in old one if needed, otherwise feed False
    if not ReminderObj: #If it isn't a previously made object that still exists, useful as the search feature only removes the frame, not the reference
        ReminderObj = Reminder(Main,Title,Description,Categories,DueDate,Priority,Attachments) #creates a new object
    if Open_editor: #Open_editor is a bool value, opens the editor when reminder is created, used when pressing the New reminder button.
        ReminderObj.Edit() #calles edit method
    NewReminder = tk.Frame(ReminderFrameList,bg="white",height=100) #creates the reminder frame
    NewReminder.config(bg="#A6A6A6") #Reminder frame colour
    Text = tk.Label(NewReminder,text=ReminderObj.Title,bg="#6B6B6B",fg="#FFFFFF",font=("",25,"bold"),wraplength=300, justify="left") #Labels that contain all of the displayed data
    Description = tk.Label(NewReminder,text=ReminderObj.Description,bg="#6B6B6B",fg="#FFFFFF",font=("",10,"bold")) #2 labels are formatted, rest are not (lack of time)
    Categories = tk.Label(NewReminder,text=ReminderObj.Categories)
    DueDate = tk.Label(NewReminder,text=ReminderObj.DueDate)
    Priority = tk.Label(NewReminder,text=ReminderObj.Priority)
    Attachments = tk.Label(NewReminder,text=ReminderObj.Attachments)

    Text.pack(anchor="w", padx=5,pady=5) #displays the lables, with 2 formatted properly
    Description.pack(anchor="w", padx=5)
    Categories.pack()
    DueDate.pack()
    Priority.pack()
    Attachments.pack()
#Functions needed for the 2 buttons on the frame
    def UpdateReminder(): #Updates the labels to display the current object data
        Text.config(text=ReminderObj.Title)
        Description.config(text=ReminderObj.Description)
        Categories.config(text=ReminderObj.Categories)
        DueDate.config(text=ReminderObj.DueDate)
        Priority.config(text=ReminderObj.Priority)
        Attachments.config(text=ReminderObj.Attachments)

    def DeleteReminder(): #Deletes the reminder frame and object.
        if ReminderObj.DeleteConfirm != 1: #for confirmation, delete must be pressed 3 times
            ReminderObj.DeleteConfirm -= 1
            DelBtn.config(text=f"Delete: x{ReminderObj.DeleteConfirm}")
            return
        else:
            ReminderObjReferences.remove(ReminderObj)
            NewReminder.destroy()

    DelBtn = tk.Button(NewReminder,text=f"Delete: x{ReminderObj.DeleteConfirm}",command=DeleteReminder,bg="red") #Creates the buttons
    EditBtn = tk.Button(NewReminder,text="Edit",command=lambda:ReminderObj.Edit(UpdateReminder)) #edit button calls the edit method with update reminders as the arg
    EditBtn.pack() #unformatted
    DelBtn.place(relx=0.961,rely=0.061, anchor="center") #display buttons with correct formatting
    NewReminder.pack(fill="x",padx=10,pady=10) #displays reminder
    if ReminderObj not in ReminderObjReferences: #If the reminder object reference has not already been stored in ReminderObjReferences, add it. 
        ReminderObjReferences.append(ReminderObj)

def SaveReminders(): #Saves reminders to a file
    with open("ReminderEntries.txt","w") as ReminderEntries: #Opens file in write mode
        for reminder in ReminderObjReferences: #Iterate through every reminder, printing all their attributes on new lines
                ReminderEntries.write(reminder.Title +"\n") #\n appends each to a new line
                ReminderEntries.write(reminder.Description +"\n")
                ReminderEntries.write(reminder.Categories +"\n")
                ReminderEntries.write(reminder.DueDate +"\n")
                ReminderEntries.write(reminder.Priority +"\n")
                ReminderEntries.write(reminder.Attachments +"\n") #fix later, possible remove it
    Main.destroy() #Closes the main tkinter window, stopping the program


AddNewReminderTest = tk.Button(Main,command=lambda:CreateReminder("Reminder","","TESTING","01/01/27","low","N/A",True,False),text="New Reminder") #New reminder button, correctly formatted
AddNewReminderTest.pack(side="bottom",anchor="w",padx=10,pady=10) #display the button

Main.protocol("WM_DELETE_WINDOW", SaveReminders) #Rebinds the X button that usually closes the window, rebound to save function

#Readds saved reminders
try:
    with open("ReminderEntries.txt","r") as SavedReminders: #opens file, read mode
        Entries = SavedReminders.readlines() #stores every line in the file
        if Entries: #check to see if there are reminders
            for i in range(0, len(Entries),6): #extracts lines in lists of 6
                ReminderData = Entries[i:i+6] #each list is used to create a reminder
                CreateReminder(ReminderData[0].strip(),ReminderData[1].strip(),ReminderData[2].strip(),ReminderData[3].strip(),ReminderData[4].strip(),ReminderData[5].strip(),False,False)

except:
    pass #prevents errors from stopping the program if no file is found


#reminder sorting
SearchLabel = tk.Label(Main,text="Search: ",bg="#878787") #Label
SearchBar = tk.Entry(Main) #Entry, takes user input
SearchWithDescription = tk.BooleanVar(value=False) #tkinter boolian variable



def Filter_with_search(SearchWithDescription): #Searches all reminders and displays matching ones
    if SearchBar.get() == "": #if the search bar is empty:
        for Frames in ReminderFrameList.winfo_children(): #Clear all frames
                Frames.destroy()
        for Reminder in ReminderObjReferences: #Add every reminder in ReminderObjReference
            CreateReminder(None,None,None,None,None,None,False,Reminder) #Creates reminder
        return
        

    Results = [] #List for matching results

    for ReminderObj in ReminderObjReferences: #Iterate through every reminder:
        if SearchBar.get().lower() in ReminderObj.Title.lower(): #If the inputted string is found within the reminders title (With lower() function):
            Results.append(ReminderObj) #add it to the results list
        if SearchWithDescription.get() and (SearchBar.get().lower() in ReminderObj.Description.lower()): #if the search select is True AND inputted string is found within the description:
            Results.append(ReminderObj) #add to results

    for Frames in ReminderFrameList.winfo_children(): #Removes every frame
        Frames.destroy()

    for NewReminder in Results: #Creates new reminder frames using only object references from Results
        CreateReminder(None,None,None,None,None,None,False,NewReminder)

SearchWithDescriptionButton = tk.Checkbutton(Main,text="Search description as well",onvalue=True,offvalue=False,variable=SearchWithDescription,bg="#878787",command=lambda:Filter_with_search(SearchWithDescription))
#Creates a checkbox button that changes SearchWithDescription between True and False, calls Filter_with_search when pressed

SearchBar.bind("<KeyRelease>", lambda event: Filter_with_search(SearchWithDescription)) #Calls Filter_with_search whenever a keyboard key is relesed


SearchLabel.place(relx=0.02,rely=0.22) #displays the label, entry, and checkbox with correct formatting
SearchBar.place(relx=0.02,rely=0.25)
SearchWithDescriptionButton.place(relx=0.02,rely=0.30)

Main.mainloop() #begins the main tkinter running loop
