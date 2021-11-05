from tkinter import *
class Task:
    def __init__(self, name, description, deadline, Canvas, lilypadAbove):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.canvas = Canvas
        self.lilypadAbove = lilypadAbove
        #send task data to task database

    def view(self, column):
        # creates the labels for a task
        self.column = column
        self.nameLabel = Label(self.lilypadAbove.taskframe, text="Name: " + self.name )
        self.nameLabel.grid(row=1, column=self.column, padx=10, pady=0, sticky="w")
        self.nameLabel = Label(self.lilypadAbove.taskframe,  text="Description: " + self.description)
        self.nameLabel.grid(row=2, column=self.column, padx=10, pady=0, sticky="w")
        self.nameLabel = Label(self.lilypadAbove.taskframe, text="Deadline Date: " + self.deadline)
        self.nameLabel.grid(row=3, column=self.column, padx=10, pady=0, sticky="w")
        ### this should probably have a button to change the current state of this task ###


class LilyPad:
    def __init__(self, name, Canvas, pondAbove):
        self.tasks = []
        self.name = name
        self.pondAbove = pondAbove
        self.canvas = Canvas
        self.taskframe = Frame(root)
        self.taskframe.place(relx = 0, rely = 0.3, anchor = "nw", width=1000)
        self.taskframe.configure(bg="#00aaaa")
        # self.button = Button(self.canvas, text="add a lilypad", command=self.create_new)
        # self.button.grid(row=1, column=2, padx=10, pady=10, sticky="w")

    def addTask(self, tasktoadd):
        #adds a task to the tasks list
        self.tasks.append(tasktoadd)

    def create_new(self):
        # this will be for creating a new lilypad using a textbox
        #upload new data to lilypad db
        return

    def view(self):
        if self.pondAbove.currentlilypad != None:
            self.pondAbove.currentlilypad.taskframe.destroy()
            self.pondAbove.taskframe = Frame(root)
            self.pondAbove.taskframe.place(relx = 0, rely = 0.2, anchor = "nw", width=1000)
            self.pondAbove.taskframe.configure(bg="#00aaaa")
            for lilypad in self.pondAbove.lilypads:
                lilypad.taskframe.destroy()
                lilypad.taskframe = Frame(root)
                lilypad.taskframe.place(relx = 0, rely = 0.3, anchor = "nw", width=1000)
                lilypad.taskframe.configure(bg="#00aaaa")

        self.pondAbove.currentlilypad = self
        i = 0
        while i < len(self.tasks):
            self.tasks[i].view(i)
            i += 1

    def displayAll(self, column):
        self.button = Button(self.pondAbove.lilypadframe, text=self.name, command=self.view)
        self.button.grid(row=1, column=column, padx=10, pady=10, sticky="w")

class Pond:
    def __init__(self, name, canvas, projectAbove):
        self.lilypads = []
        self.name = name
        self.projectAbove = projectAbove
        self.currentlilypad = None
        self.lilypadframe = Frame(root)
        self.lilypadframe.place(relx = 0, rely = 0.2, anchor = "nw", width=1000)
        self.lilypadframe.configure(bg="#fff700")
        self.canvas = canvas

        # self.textbox = Text(self.frame, height=1, width=15)
        # self.textbox.grid(row=1,column=1, padx=10, pady=10, sticky="w")
        # # self.textbox.focus_set()
        # self.createpro = Button(self.frame, text="Create New LilyPad", command=self.create_new)
        # self.createpro.grid(row=1, column=2, padx=10, pady=10, sticky="w")        
        
    # def create_new(self):
    #     self.text = self.textbox.get("1.0", END)
    #     self.button = Button(self.frame, text=self.text)
        
    #     self.button.configure(command=self.show_lilypads())
    #     self.textbox.delete("1.0", END)
    #     self.button.grid(row=1,column=len(self.lilypads)+1, padx=10, pady=10, sticky="w")

    #     self.lilypads.append(self.button)
    #     self.textbox.grid(column=len(self.lilypads)+1)
    #     self.createpro.grid(column=len(self.lilypads)+2)
        #send pond data to ponda database
        # return
    def addLilyPad(self, LilyPadtoadd):
        self.lilypads.append(LilyPadtoadd)

    def displayAll(self, column):
        self.button = Button(self.projectAbove.pondframe, text=self.name, command=self.view)
        self.button.grid(row=1,column=column, padx=10, pady=10, sticky="w")
        # i = 0
        # while i < len(self.lilypads):
        #     self.lilypads[i].displayAll(i)
        #     i += 1

    def view(self):
        if self.projectAbove.currentPond != None:
            self.projectAbove.currentPond.lilypadframe.destroy()
            self.lilypadframe = Frame(root)
            self.lilypadframe.place(relx = 0, rely = 0.2, anchor = "nw", width=1000)
            self.lilypadframe.configure(bg="#fff700")
            for pond in self.projectAbove.ponds:
                for lilypad in pond.lilypads:
                    lilypad.taskframe.destroy()
                    lilypad.taskframe = Frame(root)
                    lilypad.taskframe.place(relx = 0, rely = 0.3, anchor = "nw", width=1000)
                    lilypad.taskframe.configure(bg="#00aaaa")

        self.projectAbove.currentPond = self
        i = 0
        while i < len(self.lilypads):
            self.lilypads[i].displayAll(i)
            i += 1

    def show_lilypads(self):
        # selected_project.focus_set()
        # selected_project.configure(bg="#1aed84", relief=SUNKEN)
        #focus on this project and display all ponds involved
        # pond_frame = Frame(root)
        # pond_frame.place(relx=0.0, rely=0.1, anchor="nw", width=1100)
        # pond_frame.configure(bg="#00aaaa")
        for i in self.lilypads:
            print(list(self.lilypads))
        
        # Pond("new", pond_frame, self.canvas)


class Project:
    def __init__(self, name, frame, canvas):
        self.ponds = []
        self.frame = frame
        self.pondframe = Frame(root)
        self.pondframe.place(relx = 0, rely = 0.1, anchor = "nw", width=1000)
        self.pondframe.configure(bg="#0cf700")
        self.canvas = canvas
        self.name = name
        self.Above = TadpoleUI
        self.currentPond = None

    def create(self):
        # create a pond based on the name in the textbox
        # self.Above.textbox.destroy() # these 2 delete the textbox and create new project buttons
        # self.Above.createpro.destroy() # they are then recreated wh showProjects() is ran
        ### send data to database
        self.Above.showProjects()

    def addPond(self, pondtoadd):
        self.ponds.append(pondtoadd)

    def displayAll(self, column):
        self.button = Button(self.frame, text=self.name, command=self.view)
        self.button.grid(row=1,column=column, padx=10, pady=10, sticky="w")

    def view(self):
        if self.Above.currentProject != None:
            self.Above.currentProject.pondframe.destroy()
            for project in self.Above.Projects:
                for pond in project.ponds:
                    for lilypad in pond.lilypads:
                        lilypad.taskframe.destroy()
                        lilypad.taskframe = Frame(root)
                        lilypad.taskframe.place(relx = 0, rely = 0.3, anchor = "nw", width=1000)
                        lilypad.taskframe.configure(bg="#00aaaa")
                    pond.lilypadframe.destroy()
                    pond.lilypadframe = Frame(root)
                    pond.lilypadframe.place(relx = 0, rely = 0.2, anchor = "nw", width=1000)
                    pond.lilypadframe.configure(bg="#fff700")
                project.pondframe.destroy()
                project.pondframe = Frame(root)
                project.pondframe.place(relx = 0, rely = 0.1, anchor = "nw", width=1000)
                project.pondframe.configure(bg="#0cf700")

        self.Above.currentProject = self
            
        i = 0
        while i < len(self.ponds):
            self.ponds[i].displayAll(i)
            i += 1
        


class TadPole():
    def __init__(self, root):
        self.root = root
        self.Projects = []
        self.currentProject = None
        self.textbox = None
        self.createpro = None

        self.can = Canvas(root, width=1000, height=700)
        self.can.configure(bg="#0cf7e0")
        self.can.pack()

        self.Textlines = Label(root, text="Made by Team 8", relief=SUNKEN)
        self.Textlines.pack()

        self.frame = Frame(root)
        self.frame.place(relx = 0.5, rely = 0.5, anchor = "center")
        self.frame.configure(bg="#0cf7e0")

        self.User1 = Button(self.frame, text="Leader", command=self.leader)
        self.User1.grid(row=1,column=1, padx=10, pady=10)

        self.User2 = Button(self.frame, text="Member", command=self.member)
        self.User2.grid(row=1,column=2, padx=10, pady=10)
        

    def leader(self):
        self.User1.destroy()
        self.User2.destroy()
        self.frame.place(relx=0, rely=0, anchor="nw")
        ##these are to demonstrate downloading the projects from a database
        self.testing()
        self.showProjects()
        
        # self.Projects.append(Project(self.frame, self.can))

    def showProjects(self):
        i = 0
        while i < len(self.Projects):
            self.Projects[i].displayAll(i)
            i += 1
    
        self.textbox = Text(self.frame, height=1, width=15)
        self.textbox.grid(row=1,column=len(self.Projects)+1, padx=10, pady=10, sticky="w")
        self.createpro = Button(self.frame, text="create new project", command=self.create)
        self.createpro.grid(row=1,column=len(self.Projects)+2, padx=10, pady=10, sticky="w")

    def create(self):
        # create a pond based on the name in the textbox
        button = Project(self.textbox.get("1.0", "end-1c"), self.frame, self.can)
        self.textbox.destroy() # these 2 delete the textbox and create new project buttons
        self.createpro.destroy() # they are then recreated wh showProjects() is ran
        ### send data to database
        self.Projects.append(button)
        self.showProjects()

    def member(self):
        #this definitely doesnt work
        self.User1.destroy()
        self.User2.destroy()
        self.frame.place(relx=0, rely=0, anchor="nw")
        self.testing()
        self.showProjects()
        

    def testing(self):
        # return
        #these are to demonstrate downloading the projects from a database
        TestProject = Project("Project", self.frame, self.can)
        TestPond = Pond("Pond", self.can, TestProject)
        TestLilyPad = LilyPad("LilyPad", self.can, TestPond)
        TestLilyPad3 = LilyPad("LilyPad3", self.can, TestPond)
        TestTask = Task("Task name", "description of the things the task should accomplish", "01/01/2001", self.can, TestLilyPad)
        TestTask4 = Task("Task name", "description of the things the task should accomplish", "01/01/2001", self.can, TestLilyPad)
        TestTask5 = Task("Task name", "description of the things the task should accomplish", "01/01/2001", self.can, TestLilyPad)
        TestPond2 = Pond("Pond2", self.can, TestProject)
        
        TestLilyPad2 = LilyPad("LilyPad2", self.can, TestPond2)
        TestLilyPad4 = LilyPad("LilyPad4", self.can, TestPond2)
        TestTask2 = Task("Replace the other task please", "description of the things the task should accomplish", "01/01/2001", self.can, TestLilyPad3)
        TestTask3 = Task("This is very cool", "description of the things the task should accomplish", "01/01/2001", self.can, TestLilyPad3)

        
        TestProject2 = Project("Project2", self.frame, self.can)
        TestPond10 = Pond("this is the second test", self.can, TestProject2)
        
        TestLilyPad10 = LilyPad("test part 2 lilypad boogaloo", self.can, TestPond10)
        TestLilyPad11 = LilyPad("3 lilypad boogaloo", self.can, TestPond10)
        TestTask10 = Task("other task please", "description of the things the task should accomplish", "01/01/2001", self.can, TestLilyPad10)
        TestTask11 = Task("This is very cool", "description of the things the task should accomplish", "01/01/2001", self.can, TestLilyPad11)
        TestLilyPad10.addTask(TestTask10)
        TestLilyPad11.addTask(TestTask11)
        TestPond10.addLilyPad(TestLilyPad10)
        TestPond10.addLilyPad(TestLilyPad11)
        TestProject2.addPond(TestPond10)
        TestLilyPad.addTask(TestTask)
        TestLilyPad.addTask(TestTask4)
        TestLilyPad.addTask(TestTask5)
        TestLilyPad3.addTask(TestTask2)
        TestLilyPad3.addTask(TestTask3)
        TestPond.addLilyPad(TestLilyPad)
        TestPond.addLilyPad(TestLilyPad3)
        TestPond2.addLilyPad(TestLilyPad2)
        TestPond2.addLilyPad(TestLilyPad4)
        TestProject.addPond(TestPond)
        TestProject.addPond(TestPond2)
        self.Projects.append(TestProject)
        self.Projects.append(TestProject2)

global Focused

root = Tk()
TadpoleUI = TadPole(root)
root.mainloop()



    