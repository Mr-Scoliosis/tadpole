from tkinter import *
class Task:
    def __init__(self, name, description, deadline, frame, Canvas):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.frame = frame
        self.canvas = Canvas
        #send task data to task database

    def displayAll(self, column):
        self.column = column
        self.button = Button(self.frame, text=self.name, command=self.view)
        self.button.grid(row=4, column=self.column, padx=10, pady=10, sticky="w")

    def view(self):
        return

class LilyPad:
    def __init__(self, name, frame, Canvas):
        self.tasks = []
        self.name = name
        self.frame = frame
        self.canvas = Canvas
        # self.button = Button(self.canvas, text="add a lilypad", command=self.create_new)
        # self.button.grid(row=1, column=2, padx=10, pady=10, sticky="w")

    def addTask(self, tasktoadd):
        self.tasks.append(tasktoadd)

    def create_new(self):
        #upload new data to lilypad db
        return

    def view(self):
        return

    def displayAll(self, column):
        self.button = Button(self.frame, text=self.name, command=self.view)
        self.button.grid(row=3,column=column, padx=10, pady=10, sticky="w")
        i = 0
        while i < len(self.tasks):
            self.tasks[i].displayAll(i)
            i += 1

class Pond:
    def __init__(self, name, frame, canvas):
        self.lilypads = []
        self.name = name
        self.frame = frame
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
        self.button = Button(self.frame, text=self.name, command=self.view)
        self.button.grid(row=2,column=column, padx=10, pady=10, sticky="w")
        i = 0
        while i < len(self.lilypads):
            self.lilypads[i].displayAll(i)
            i += 1

    def view(self):
        return

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
    def __init__(self, name, frame, canvas, column):
        self.ponds = []
        self.frame = frame
        self.canvas = canvas
        self.name = name
        self.column = column
        # self.frame.place(relx=0, rely=0, anchor="nw")
        # self.textbox = Text(self.frame, height=1, width=15)
        # self.textbox.grid(row=len(self.ponds)+1,column=1, padx=10, pady=10, sticky="w")
        # self.textbox.focus_set()
        # self.createpro = Button(self.frame, text="create new project", command=self.create)
        # self.createpro.grid(row=len(self.ponds)+1,column=2, padx=10, pady=10, sticky="w")

    # def create(self):
        #create a pond based on the name in the textbox
        # self.button = Button(self.frame, text=self.textbox.get("1.0", END))
        
        # self.button.configure(command=self.show_Ponds())
        # self.textbox.delete("1.0", END)
        # self.button.grid(row=1,column=len(self.ponds)+1, padx=10, pady=10, sticky="w")
        #send data to database
        #     
        # self.ponds.append(self.button)
        # self.textbox.grid(column=len(self.ponds)+1)
        # self.createpro.grid(column=len(self.ponds)+2)

    def addPond(self, pondtoadd):
        self.ponds.append(pondtoadd)

    def displayAll(self, column):
        self.button = Button(self.frame, text=self.name, command=self.view)
        self.button.grid(row=1,column=self.column, padx=10, pady=10, sticky="w")
        i = 0
        while i < len(self.ponds):
            self.ponds[i].displayAll(i)
            i += 1

    def view(self):
        return

    def show_Ponds(self):
        return
        #focus on this project and display all ponds involved
        # pond_frame = Frame(root)
        # pond_frame.place(relx=0.0, rely=0.1, anchor="nw", width=1100)
        # pond_frame.configure(bg="#00aaaa")
        # for i in self.Projects:
        #     i.configure(bg="#ffffff")
        # Focused = self
        # Focused.button.configure(bg="#1aed84", relief=SUNKEN)
        
        # self.ponds.append(Pond("new", pond_frame, self.canvas))
        # print(self.ponds)
        #add a generate random code thing for team invites


class TadPole():
    def __init__(self, root):
        self.root = root
        self.Projects = []

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
        TestTask = Task("Task", "description", "deadline", self.frame, self.can)
        TestLilyPad = LilyPad("LilyPad", self.frame, self.can)
        TestPond = Pond("Pond", self.frame, self.can)
        TestProject = Project("Project", self.frame, self.can, len(self.Projects))
        TestLilyPad.addTask(TestTask)
        TestPond.addLilyPad(TestLilyPad)
        TestProject.addPond(TestPond)
        self.Projects.append(TestProject)
        self.showProjects()
        
        # self.Projects.append(Project(self.frame, self.can))

    def showProjects(self):
        i = 0
        while i < len(self.Projects):
            self.Projects[i].displayAll(i+1)
            i += 1

    def member(self):
        #this definitely doesnt work
        self.User1.destroy()
        self.User2.destroy()
        self.frame.place(relx=0, rely=0, anchor="nw")
        self.Label1 = Label(self.frame, text="This is what the Team Member sees")
        self.Label1.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        # self.Label2 = Label(self.frame, text="I am still a God")
        # self.Label2.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        # self.add_new = Button(self.frame, text="+", command=self.create)
        # self.add_new.grid(row=3,column=1, padx=10, pady=10, sticky="w")


global Focused

root = Tk()
TadpoleUI = TadPole(root)
root.mainloop()



    