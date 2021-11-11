from tkinter import *
import pymysql as db
# import time

    # connection = db.connect(
    #     host='cs1.ucc.ie',
    #     user='ld8',
    #     password='soodi',
    #     database='cs2208_ld8')
    # cursor = connection.cursor(db.cursors.DictCursor)

    # connection.commit()
    # cursor.close()
    # connection.close()




def downloadProjects(self):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    
    cursor.execute("""SELECT * FROM Projects""")
    Projects = []
    for row in cursor.fetchall():
        id = row['ID']
        leader = row['Leader']
        name = row['Name']
        Projects.append(Project(id, leader, name, self.frame, self.can, self.root))
    
    connection.commit()
    cursor.close()
    connection.close()

    return Projects

def get_project_by_id(main, project_id):
    for i in main.Projects:
        if i.id == project_id:
            return i

def get_pond_by_id(self, pond_id):
    for i in self.ponds:
        if i.id == pond_id:
            return i

def get_lilypad_by_id(self, lilypad_id):
    for i in self.lilypads:
        if i.id == lilypad_id:
            return i


def downloadTeams(project):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)

    cursor.execute("""SELECT * FROM Teams""")
    for row in cursor.fetchall():
        id = row['ID']
        name = row['Name']
        project_above = project
        project_above.addMembers(member(id, name, project.canvas, project_above))
    connection.commit()
    cursor.close()
    connection.close()


def downloadPonds(project):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    ponds = []
    cursor.execute("""SELECT * FROM Ponds p WHERE p.Project_ID = %i""" % project.id)
    for row in cursor.fetchall():
        id = row['ID']
        name = row['Name']
        project_above = project
        ponds.append(Pond(id, name, project.canvas, project_above))
    connection.commit()
    cursor.close()
    connection.close()
    return ponds


def downloadLilypads(pond):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    lilypads = []
    cursor.execute("""SELECT * FROM Lilypads l WHERE l.Pond_ID = %i""" % pond.id)
    for row in cursor.fetchall():
        id = row['ID']
        name = row['Name']
        pond_above = pond
        lilypads.append(LilyPad(id, name, pond.canvas, pond_above))
    connection.commit()
    cursor.close()
    connection.close()
    return lilypads


def downloadTasks(lilypad):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    tasks = []
    cursor.execute("""SELECT * FROM Tasks t WHERE t.Lilypad_ID = %i""" % lilypad.id)
    #the descrpt variable is written this way as description is a keyword in
    #python, and this was the cleanest alternative
    for row in cursor.fetchall():
        id = row['ID']
        name = row['Name']
        descrpt = row["Dscrpt"]
        deadline = row["Deadline"]
        status = row["Status"]
        lilypad_above = lilypad
        tasks.append(Task(id, name, descrpt, deadline, status, lilypad_above.canvas, lilypad_above))
    connection.commit()
    cursor.close()
    connection.close()
    return tasks

def insertProject(leaderName, projectName):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""INSERT INTO Projects(Leader, Name) Values(%s, %s)""", (leaderName, projectName))
    cursor.execute("""SELECT MAX(ID) FROM Projects""")
    for row in cursor.fetchall():
        id = row["MAX(ID)"]
    connection.commit()
    cursor.close()
    connection.close()
    return id

def insertPond(pondName, projectID):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""INSERT INTO Ponds(Name, Project_ID) Values(%s, %s)""", (pondName, projectID))
    cursor.execute("""SELECT MAX(ID) FROM Ponds""")
    for row in cursor.fetchall():
        id = row["MAX(ID)"]
    connection.commit()
    cursor.close()
    connection.close()
    return id

def insertLilyPad(lilypadName, pondID):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""INSERT INTO Lilypads(Name, Pond_ID) Values(%s, %s)""", (lilypadName, pondID))
    cursor.execute("""SELECT MAX(ID) FROM Lilypads""")
    for row in cursor.fetchall():
        id = row["MAX(ID)"]
    connection.commit()
    cursor.close()
    connection.close()
    return id

def insertTask(taskName, taskDescription, taskDeadline, pondID):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""INSERT INTO Tasks(Name, Dscrpt, Deadline, Status, Lilypad_ID) Values(%s, %s, %s, %s, %s)""", (taskName, taskDescription, taskDeadline, 0, pondID))
    cursor.execute("""SELECT MAX(ID) FROM Tasks""")
    for row in cursor.fetchall():
        id = row["MAX(ID)"]
    connection.commit()
    cursor.close()
    connection.close()
    return id

def updateTaskStatus(taskID, Status):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""Update Tasks SET Status = %s WHERE ID = %s""", (Status, taskID))
    connection.commit()
    cursor.close()
    connection.close()



class Task:
    def __init__(self, id, name, description, deadline, status, Canvas, lilypadAbove):
        self.id = id
        self.name = name
        self.description = description
        self.deadline = deadline
        self.canvas = Canvas
        self.status = status
        self.lilypadAbove = lilypadAbove#

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

        self.nameLabel2 = Label(self.lilypadAbove.taskframe, text="Deadline Date: " + str(self.deadline), wraplength=100)
        self.nameLabel2.grid(row=3, column=self.column, padx=10, pady=0, sticky="w")
        
        self.Status_Button = Button(self.lilypadAbove.taskframe, text="Change Status", command=self.updateStatus)
        self.Status_Button.grid(row=4, column=self.column, padx=10, pady=0, sticky="w")

    def updateStatus(self):
        ### send data to database
        if self.status == 0:
            self.nameLabel.configure(bg="#FFA500")
            updateTaskStatus(self.id, 1)
            self.status = 1
        elif self.status == 1:
            self.nameLabel.configure(bg="#00ff00")
            updateTaskStatus(self.id, 2)
            self.status = 2



class LilyPad:
    def __init__(self, id, name, Canvas, pondAbove):
        self.tasks = []
        self.id = id
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
        taskName = self.textbox.get("1.0", "end-1c")
        taskDescription = self.textbox1.get("1.0", "end-1c")
        taskDeadline = self.textbox2.get("1.0", "end-1c")
        id = insertTask(taskName, taskDescription, taskDeadline, self.id)
        button = Task(id, taskName, taskDescription, taskDeadline, 0, self.canvas, self.pondAbove.currentlilypad)
        self.textbox.destroy() # these 2 delete the textbox and create new project buttons
        self.createpro.destroy() # they are then recreated when showProjects() is ran
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
                lilypad.button.configure(bg="#ffffff")
                lilypad.taskframe.destroy()
                lilypad.taskframe = Frame(root)
                lilypad.taskframe.place(relx = 0, rely = 0.3, anchor = "nw", width=1000)
                lilypad.taskframe.configure(bg="#00aaaa")

        self.pondAbove.currentlilypad = self
        self.pondAbove.currentlilypad.button.configure(bg="#ccccaa")
        
        self.tasks = downloadTasks(self)
        i = 0
        while i < len(self.tasks):
            self.tasks[i].view(i)
            i += 1

        if self.pondAbove.projectAbove.Above.creation != False:
            self.textbox = Text(self.taskframe, height=1, width=15)
            self.textbox.grid(row=1,column=len(self.tasks)+1, padx=10, pady=10, sticky="w")
            self.textbox1 = Text(self.taskframe, height=3, width=15)
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
        self.lilypadframe.configure(bg="#eeeaaa")
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
            self.lilypadframe.configure(bg="#eeeaaa")
            for pond in self.projectAbove.ponds:
                for lilypad in pond.lilypads:
                    lilypad.taskframe.destroy()
                    lilypad.taskframe = Frame(root)
                    lilypad.taskframe.place(relx = 0, rely = 0.3, anchor = "nw", width=1000)
                    lilypad.taskframe.configure(bg="#00aaaa")
                pond.button.configure(bg="#ffffff")
                pond.lilypadframe.destroy()
                pond.lilypadframe = Frame(root)
                pond.lilypadframe.place(relx = 0, rely = 0.2, anchor = "nw", width=1000)
                pond.lilypadframe.configure(bg="#eeeaaa")

        self.projectAbove.currentPond = self
        self.projectAbove.currentPond.button.configure(bg="#aaccaa")
        self.lilypads = downloadLilypads(self)
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
        # create a lilypad based on the name in the textbox
        newLilyPadName = self.textbox.get("1.0", "end-1c")
        #send info to database
        id = insertLilyPad(newLilyPadName, self.id)
        lilyPadButton = LilyPad(id, newLilyPadName, self.canvas, self.projectAbove.currentPond)
        self.textbox.destroy() # these 2 delete the textbox and create new project buttons
        self.createpro.destroy() # they are then recreated wh showProjects() is ran
        self.lilypads.append(lilyPadButton)
        self.view()


class Project:
    def __init__(self, id, leader, name, frame, canvas, root):
        self.ponds = []
        self.frame = frame
        self.root = root
        self.pondframe = Frame(self.root)
        self.members = []
        self.pondframe.place(relx = 0, rely = 0.1, anchor = "nw", width=1000)
        self.pondframe.configure(bg="#006400")
        self.canvas = canvas
        self.name = name
        self.Above = TadpoleUI
        self.currentPond = None
        self.leader = leader
        self.id = id

    def addMembers(self, membering):
        self.members.append(membering)

    def create(self):
        # create a pond based on the name in the textbox
        newPondName = self.textbox.get("1.0", "end-1c")
        id = insertPond(newPondName, self.id)
        pondButton = Pond(id, newPondName, self.canvas, self.Above.currentProject)
        self.textbox.destroy() # these 2 delete the textbox and create new project buttons
        self.createpro.destroy() # they are then recreated wh showProjects() is ran
        # send data to database
        self.ponds.append(pondButton)
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
                    pond.lilypadframe.configure(bg="#eeeaaa")
                project.pondframe.destroy()
                project.pondframe = Frame(root)
                project.pondframe.place(relx = 0, rely = 0.1, anchor = "nw", width=1000)
                project.pondframe.configure(bg="#006400")
                project.button.configure(bg="#ffffff")
            self.Above.memberFrame.destroy()
            self.Above.memberFrame = Frame(root)
            self.Above.memberFrame.place(relx=0.72, rely=0, anchor="nw", width=400, height=700)
            self.Above.memberFrame.configure(bg="#00918a")

        self.Above.currentProject = self
        self.Above.currentProject.button.configure(bg="#aaaacc")

        self.ponds = downloadPonds(self)
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
        self.username = "guy"
        self.frame.place(relx=0, rely=0, anchor="nw")
        self.memberFrame = Frame(root)
        self.memberFrame.place(relx=0.72, rely=0, anchor="nw", width=400, height=700)
        self.memberFrame.configure(bg="#00918a")

        ##these are to demonstrate downloading the projects from a database
        self.Projects = downloadProjects(self)
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
        projectName = self.textbox.get("1.0", "end-1c")
        id = insertProject(self.username, projectName)
        projectButton = Project(id, self.username, projectName, self.frame, self.can, root)
        
        self.textbox.destroy() # these 2 delete the textbox and create new project buttons
        self.createpro.destroy() # they are then recreated wh showProjects() is ran
        # send data to database
        self.Projects.append(projectButton)
        self.showProjects()

    def member(self):
        # this definitely doesnt work
        self.User1.destroy()
        self.User2.destroy()
        self.frame.place(relx=0, rely=0, anchor="nw")
        self.username = "Luke"

        self.memberFrame = Frame(root)
        self.memberFrame.place(relx=0.72, rely=0, anchor="nw", width=400, height=700)
        self.memberFrame.configure(bg="#00918a")
        self.Projects = downloadProjects(self)
        self.showProjects()
        

root = Tk()
TadpoleUI = TadPole(root)
root.mainloop()


