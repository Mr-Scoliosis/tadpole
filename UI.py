from tkinter import *
import pymysql as db
import backend
# from UI import download



class Task:
    def __init__(self, id, name, description, deadline, status, Canvas, lilypadAbove):
        self.id = id
        self.name = name
        self.description = description
        self.deadline = deadline
        self.deadline = status
        self.canvas = Canvas
        self.lilypadAbove = lilypadAbove
        # send task data to task database

    def view(self, column):
        # creates the labels for a task
        self.column = column
        self.nameLabel = Label(self.lilypadAbove.taskframe, text="Name: " + self.name )
        self.nameLabel.grid(row=1, column=self.column, padx=10, pady=0, sticky="w")
        self.nameLabel1 = Label(self.lilypadAbove.taskframe,  text="Description: " + self.description)
        self.nameLabel1.grid(row=2, column=self.column, padx=10, pady=0, sticky="w")
        self.nameLabel2 = Label(self.lilypadAbove.taskframe, text="Deadline Date: " + self.deadline)
        self.nameLabel2.grid(row=3, column=self.column, padx=10, pady=0, sticky="w")

        self.Status = Label(self.lilypadAbove.taskframe, text="Status: ")
        self.Status.grid(row=4, column=self.column, padx=10, pady=0, sticky="w")
        self.Status_Button = Button(self.lilypadAbove.taskframe, text="Change Status", command=self.updateStatus)
        # this should probably have a button to change the current state of this task

    def updateStatus(self):
        return


class LilyPad:
    def __init__(self, name, Canvas, pondAbove):
        self.tasks = []
        self.name = name
        self.pondAbove = pondAbove
        self.canvas = Canvas
        self.taskframe = Frame(root)
        self.taskframe.place(relx = 0, rely = 0.3, anchor = "nw", width=1000)
        self.taskframe.configure(bg="#00aaaa")

    def addTask(self, tasktoadd):
        # adds a task to the tasks list
        self.tasks.append(tasktoadd)

    def create(self):
        # create a task based on the name in the textbox
        button = Task(self.textbox.get("1.0", "end-1c"), self.textbox1.get("1.0", "end-1c"), self.textbox2.get("1.0", "end-1c"), self.canvas, self.pondAbove.currentlilypad)
        self.textbox.destroy() # these 2 delete the textbox and create new project buttons
        self.createpro.destroy() # they are then recreated wh showProjects() is ran
        # send data to database
        self.tasks.append(button)
        self.view()

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

        self.textbox = Text(self.taskframe, height=1, width=15)
        self.textbox.grid(row=1,column=len(self.tasks)+1, padx=10, pady=10, sticky="w")
        self.textbox1 = Text(self.taskframe, height=1, width=15)
        self.textbox1.grid(row=2,column=len(self.tasks)+1, padx=10, pady=10, sticky="w")
        self.textbox2 = Text(self.taskframe, height=1, width=15)
        self.textbox2.grid(row=3,column=len(self.tasks)+1, padx=10, pady=10, sticky="w")
        self.createpro = Button(self.taskframe, text="Create New Task", command=self.create)
        self.createpro.grid(row=1,column=len(self.tasks)+2, padx=10, pady=10, sticky="w")

    def displayAll(self, column):
        self.button = Button(self.pondAbove.lilypadframe, text=self.name, command=self.view)
        self.button.grid(row=1, column=column, padx=10, pady=10, sticky="w")

class Pond:
    def __init__(self, id, name, canvas, projectAbove):
        self.lilypads = []
        self.name = name
        self.projectAbove = projectAbove
        self.currentlilypad = None
        self.lilypadframe = Frame(root)
        self.lilypadframe.place(relx = 0, rely = 0.2, anchor = "nw", width=1000)
        self.lilypadframe.configure(bg="#fff700")
        self.canvas = canvas
        self.id = id

    def addLilyPad(self, LilyPadtoadd):
        self.lilypads.append(LilyPadtoadd)

    def displayAll(self, column):
        self.button = Button(self.projectAbove.pondframe, text=self.name, command=self.view)
        self.button.grid(row=1,column=column, padx=10, pady=10, sticky="w")

    def view(self):
        if self.projectAbove.currentPond != None:
            # removing previously displayed tasks
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
                pond.lilypadframe.destroy()
                pond.lilypadframe = Frame(root)
                pond.lilypadframe.place(relx = 0, rely = 0.2, anchor = "nw", width=1000)
                pond.lilypadframe.configure(bg="#fff700")

        self.projectAbove.currentPond = self
        i = 0
        while i < len(self.lilypads):
            self.lilypads[i].displayAll(i)
            i += 1

        self.textbox = Text(self.lilypadframe, height=1, width=15)
        self.textbox.grid(row=1,column=len(self.lilypads)+1, padx=10, pady=10, sticky="w")
        self.createpro = Button(self.lilypadframe, text="Create New LilyPad", command=self.create)
        self.createpro.grid(row=1,column=len(self.lilypads)+2, padx=10, pady=10, sticky="w")

    def create(self):
        # create a lilypad based on the name in the textbox
        button = LilyPad(self.textbox.get("1.0", "end-1c"), self.canvas, self.projectAbove.currentPond)
        self.textbox.destroy() # these 2 delete the textbox and create new project buttons
        self.createpro.destroy() # they are then recreated wh showProjects() is ran
        # send data to database
        self.lilypads.append(button)
        self.view()


class Project:
    def __init__(self, id, leader, name, frame, canvas, root):
        self.ponds = []
        self.frame = frame
        self.root = root
        self.pondframe = Frame(self.root)
        self.members = []
        self.pondframe.place(relx = 0, rely = 0.1, anchor = "nw", width=1000)
        self.pondframe.configure(bg="#0cf700")
        self.canvas = canvas
        self.name = name
        self.Above = TadpoleUI
        self.currentPond = None
        self.leader = leader
        self.id = id
        print(self.id)

    def add_to_members(self, membering):
        self.members.append(membering)

    def showMembers(self, row):
        self.label = Label(self.frame, text=self.name)
        self.label.grid(row=row,column=1, padx=10, pady=10, sticky="w")

    def create(self):
        # create a pond based on the name in the textbox
        new_Project = self.textbox.get("1.0", "end-1c")
        button = Pond(new_Project, self.canvas, self.Above.currentProject)
        self.textbox.destroy() # these 2 delete the textbox and create new project buttons
        self.createpro.destroy() # they are then recreated wh showProjects() is ran
        # send data to database
        self.ponds.append(button)
        self.view()

    def addPond(self, pondtoadd):
        self.ponds.append(pondtoadd)

    def displayAll(self, column):
        self.button = Button(self.frame, text=self.name, command=self.view)
        self.button.grid(row=1,column=column, padx=10, pady=10, sticky="w")

    def view(self):
        if self.Above.currentProject != None:
            # removing previously displayed ponds, lilypads, and tasks
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

        self.Above.memberFrame.destroy()
        self.Above.memberFrame = Frame(root)
        self.Above.memberFrame.place(relx=0.72, rely=0, anchor="nw", width=400, height=700)
        self.Above.memberFrame.configure(bg="#00918a")

        self.textbox = Text(self.pondframe, height=1, width=15)
        self.textbox.grid(row=1,column=len(self.ponds)+1, padx=10, pady=10, sticky="w")
        self.createpro = Button(self.pondframe, text="Create New Pond", command=self.create)
        self.createpro.grid(row=1,column=len(self.ponds)+2, padx=10, pady=10, sticky="w")
        counter = 0
        while counter < len(self.members):
            self.members[counter].display(counter)
            counter += 1

class member():
    def __init__(self, name, projects, frame):
        self.name = name
        self.projects = projects
        self.frame = frame
        self.Above = TadpoleUI

    def display(self, row):
        self.label = Label(self.frame, text=self.name)
        self.label.grid(row=row,column=1, padx=10, pady=10, sticky="w")

class TadPole():
    def __init__(self, root):
        self.root = root
        self.Projects = []
        self.currentProject = None
        self.textbox = None
        self.createpro = None
        self.can = Canvas(root, width=1400, height=700)
        self.can.configure(bg="#0cf7e0")
        self.root.title("Simple Frog")
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
        self.memberFrame = Frame(root)
        self.memberFrame.place(relx=0.72, rely=0, anchor="nw", width=400, height=700)
        self.memberFrame.configure(bg="#00918a")

<<<<<<< Updated upstream
        # these are to demonstrate downloading the projects from a database
        self.download()
=======
        ##these are to demonstrate downloading the projects from a database
        self.Projects = backend.downloadProjects(self)
>>>>>>> Stashed changes
        self.showProjects()

    def showMembers(self):
        counter = 0
        while counter < len(self.members):
            self.members[counter].display(counter)
            counter += 1

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
        # send data to database
        self.Projects.append(button)
        self.showProjects()

    def member(self):
        # this definitely doesnt work
        self.User1.destroy()
        self.User2.destroy()
        self.frame.place(relx=0, rely=0, anchor="nw")
        self.Projects = backend.downloadProjects()
        self.showProjects()

if __name__ =="__main__":
    root = Tk()
    TadpoleUI = TadPole(root)
    root.mainloop()
