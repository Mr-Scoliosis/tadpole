from tkinter import *
class Task:
    def __init__(self, name, description, deadline, Canvas, lilypadAbove):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.canvas = Canvas
        self.status = 0
        self.lilypadAbove = lilypadAbove
        #send task data to task database

    def view(self, column):
        # creates the labels for a task
        self.column = column
        self.nameLabel = Label(self.lilypadAbove.taskframe, text="Name: " + self.name, wraplength=100)
        self.nameLabel.grid(row=1, column=self.column, padx=10, pady=0, sticky="w")
        if self.status == 1:
            self.nameLabel.configure(bg="#FFA500")
        elif self.status == 2:
            self.nameLabel.configure(bg="#00ff00")
        self.nameLabel1 = Label(self.lilypadAbove.taskframe,  text="Description: " + self.description, wraplength=100)
        self.nameLabel1.grid(row=2, column=self.column, padx=10, pady=0, sticky="w")
        self.nameLabel2 = Label(self.lilypadAbove.taskframe, text="Deadline Date: " + self.deadline, wraplength=100)
        self.nameLabel2.grid(row=3, column=self.column, padx=10, pady=0, sticky="w")
        
        self.Status_Button = Button(self.lilypadAbove.taskframe, text="Change Status", command=self.updateStatus)
        self.Status_Button.grid(row=4, column=self.column, padx=10, pady=0, sticky="w")

    def updateStatus(self):
        ### send data to database
        if self.status == 0:
            self.nameLabel.configure(bg="#FFA500")
            self.status = 1
        elif self.status == 1:
            self.nameLabel.configure(bg="#00ff00")
            self.status = 2


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
        #adds a task to the tasks list
        self.tasks.append(tasktoadd)

    def create(self):
        # create a task based on the name in the textbox
        button = Task(self.textbox.get("1.0", "end-1c"), self.textbox1.get("1.0", "end-1c"), self.textbox2.get("1.0", "end-1c"), self.canvas, self.pondAbove.currentlilypad)
        self.textbox.destroy() # these 2 delete the textbox and create new project buttons
        self.createpro.destroy() # they are then recreated wh showProjects() is ran
        ### send data to database
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
        if self.pondAbove.projectAbove.Above.creation != False:
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
    def __init__(self, name, canvas, projectAbove):
        self.lilypads = []
        self.name = name
        self.projectAbove = projectAbove
        self.currentlilypad = None
        self.lilypadframe = Frame(root)
        self.lilypadframe.place(relx = 0, rely = 0.2, anchor = "nw", width=1000)
        self.lilypadframe.configure(bg="#eeeaaa")
        self.canvas = canvas

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
            self.lilypadframe.configure(bg="#eeeaaa")
            for pond in self.projectAbove.ponds:
                for lilypad in pond.lilypads:
                    lilypad.taskframe.destroy()
                    lilypad.taskframe = Frame(root)
                    lilypad.taskframe.place(relx = 0, rely = 0.3, anchor = "nw", width=1000)
                    lilypad.taskframe.configure(bg="#00aaaa")
                pond.lilypadframe.destroy()
                pond.lilypadframe = Frame(root)
                pond.lilypadframe.place(relx = 0, rely = 0.2, anchor = "nw", width=1000)
                pond.lilypadframe.configure(bg="#eeeaaa")

        self.projectAbove.currentPond = self
        i = 0
        while i < len(self.lilypads):
            self.lilypads[i].displayAll(i)
            i += 1
        if self.projectAbove.Above.creation != False:
                self.textbox = Text(self.lilypadframe, height=1, width=15)
                self.textbox.grid(row=1,column=len(self.lilypads)+1, padx=10, pady=10, sticky="w")
                self.createpro = Button(self.lilypadframe, text="Create New LilyPad", command=self.create)
                self.createpro.grid(row=1,column=len(self.lilypads)+2, padx=10, pady=10, sticky="w")

    def create(self):
        # create a pond based on the name in the textbox
        button = LilyPad(self.textbox.get("1.0", "end-1c"), self.canvas, self.projectAbove.currentPond)
        self.textbox.destroy() # these 2 delete the textbox and create new project buttons
        self.createpro.destroy() # they are then recreated wh showProjects() is ran
        ### send data to database
        self.lilypads.append(button)
        self.view()


class Project:
    def __init__(self, name, frame, canvas):
        self.ponds = []
        self.frame = frame
        self.pondframe = Frame(root)
        self.members = []
        self.pondframe.place(relx = 0, rely = 0.1, anchor = "nw", width=1000)
        self.pondframe.configure(bg="#006400")
        self.canvas = canvas
        self.name = name
        self.Above = TadpoleUI
        self.currentPond = None

    def addMembers(self, membering):
        self.members.append(membering)

    def create(self):
        # create a pond based on the name in the textbox
        new_Project = self.textbox.get("1.0", "end-1c")
        button = Pond(new_Project, self.canvas, self.Above.currentProject)
        self.textbox.destroy() # these 2 delete the textbox and create new project buttons
        self.createpro.destroy() # they are then recreated wh showProjects() is ran
        ### send data to database
        self.ponds.append(button)
        self.view()

    def addPond(self, pondtoadd):
        self.ponds.append(pondtoadd)

    def displayAll(self, column):
        self.button = Button(self.frame, text=self.name, command=self.view)
        self.button.grid(row=1,column=column, padx=10, pady=10, sticky="w")

    def view(self):
        if self.Above.currentProject != None:
            #removing previously displayed ponds, lilypads, and tasks
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
                    pond.lilypadframe.configure(bg="#eeeaaa")
                project.pondframe.destroy()
                project.pondframe = Frame(root)
                project.pondframe.place(relx = 0, rely = 0.1, anchor = "nw", width=1000)
                project.pondframe.configure(bg="#006400")
            self.Above.memberFrame.destroy()
            self.Above.memberFrame = Frame(root)
            self.Above.memberFrame.place(relx=0.72, rely=0, anchor="nw", width=400, height=700)
            self.Above.memberFrame.configure(bg="#00918a")

        self.Above.currentProject = self
            
        i = 0
        while i < len(self.ponds):
            self.ponds[i].displayAll(i)
            i += 1
        if self.Above.creation != False:
            self.textbox = Text(self.pondframe, height=1, width=15)
            self.textbox.grid(row=1,column=len(self.ponds)+1, padx=10, pady=10, sticky="w")
            self.createpro = Button(self.pondframe, text="Create New Pond", command=self.create)
            self.createpro.grid(row=1,column=len(self.ponds)+2, padx=10, pady=10, sticky="w")
        
        if self.Above.creation != False:
            self.random = Button(self.Above.memberFrame, text="Generate Invite Code", command=self.randomNumber)
            self.random.grid(row=0,column=1, padx=10, pady=10, sticky="w")
        counter = 0
        while counter < len(self.members):
            self.members[counter].display(counter+1, self.Above.memberFrame)
            counter += 1 

        
    def randomNumber(self):
        return


class member():
    def __init__(self, name, projects):
        self.name = name
        self.projects = projects
        self.Above = TadpoleUI

    def display(self, row, frame):
        self.label = Label(frame, text=self.name)
        self.label.grid(row=row, column=1, padx=10, pady=10, sticky="w")
        
class TadPole():
    def __init__(self, root):
        self.root = root
        self.Projects = []
        self.currentProject = None
        self.textbox = None
        self.createpro = None
        self.creation = False
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
        self.creation = True
        self.frame.place(relx=0, rely=0, anchor="nw")
        self.memberFrame = Frame(root)
        self.memberFrame.place(relx=0.72, rely=0, anchor="nw", width=400, height=700)
        self.memberFrame.configure(bg="#00918a")

        ##these are to demonstrate downloading the projects from a database
        self.download()
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
        if self.creation != False:
            self.textbox = Text(self.frame, height=1, width=15)
            self.textbox.grid(row=1,column=len(self.Projects)+1, padx=10, pady=10, sticky="w")
            self.createpro = Button(self.frame, text="create new project", command=self.create)
            self.createpro.grid(row=1,column=len(self.Projects)+2, padx=10, pady=10, sticky="w")
        else:
            self.codeBox = Text(self.memberFrame, height=1, width=15)
            self.codeBox.grid(row=0,column=1, padx=10, pady=10, sticky="w")
            self.random = Button(self.memberFrame, text="Join Project", command=self.joinProject)
            self.random.grid(row=0,column=2, padx=10, pady=10, sticky="w")

    def joinProject(self):
        return

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
        self.memberFrame = Frame(root)
        self.memberFrame.place(relx=0.72, rely=0, anchor="nw", width=400, height=700)
        self.memberFrame.configure(bg="#00918a")
        self.download()
        self.showProjects()
        

    def download(self):
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
        testMember = member("Jimmy", [])
        testMember2 = member("Johnny", [])
        TestProject.addMembers(testMember)
        TestProject.addMembers(testMember2)
        
        testMember3 = member("Luke", [])
        testMember4 = member("Andrew", [])
        TestProject2.addMembers(testMember3)
        TestProject2.addMembers(testMember4)

        self.Projects.append(TestProject)
        self.Projects.append(TestProject2)
        

root = Tk()
TadpoleUI = TadPole(root)
root.mainloop()



    