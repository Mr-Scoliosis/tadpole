from tkinter import *
class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        #send task data to task database


class LilyPad:
    def __init__(self, name):
        self.tasks = []
        self.name = name
        self.canvas = Canvas
        self.button = Button(self.canvas, text="add a lilypad", command=self.create_new)
        self.button.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        def create_new(self):
            #upload new data to lilypad db
            return

class Pond:
    def __init__(self, name, frame, canvas):
        self.lilypads = []
        self.pondname = name
        self.frame = frame
        self.canvas = canvas
        self.button = Button(self.frame, text="+", command=self.create_new)
        self.button.grid(row=1, column=2, padx=10, pady=10, sticky="w")        
        
    def create_new(self):
        #send pond data to ponda database
        return


class Project:
    def __init__(self, frame, canvas):
        self.ponds = []
        self.textbox.grid(row=len(self.ponds)+1,column=1, padx=10, pady=10, sticky="w")
        self.createpro.grid(row=len(self.ponds)+1,column=2, padx=10, pady=10, sticky="w")

    def create(self):
        #create a pond based on the name in the textbox
        self.button = Button(self.frame, text=self.textbox.get("1.0", END), command=self.show_Ponds)
        self.textbox.delete("1.0", END)
        self.button.grid(row=len(self.ponds)+1,column=1, padx=10, pady=10, sticky="w")
        #send data to database
        #     
        self.ponds.append(self.button)
        self.textbox.grid(row=len(self.ponds)+1)
        self.createpro.grid(row=len(self.ponds)+1)

    def show_Ponds(self):
        self.configure()
        #focus on this project and display all ponds involved
        for i in self.ponds:
            print(i)
        createPond = Pond("Name", self.frame, self.canvas)
        self.ponds.append(createPond)
        #add a generate random code thing for team invites


class TadPole():
    def __init__(self, root):
        self.root = root
        self.Projects = []
        self.add_new = Button()
        self.counter = 0


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
        # self.Buttons.append(self.User1)
        self.User2 = Button(self.frame, text="Member", command=self.member)
        self.User2.grid(row=1,column=2, padx=10, pady=10)
        # self.Buttons.append(self.User2)
        

    def leader(self):
        self.User1.destroy()
        self.User2.destroy()
        self.Projects.append(Project(self.frame, self.can))


    def member(self):
        self.User1.destroy()
        self.User2.destroy()
        self.frame.place(relx=0, rely=0, anchor="nw")
        self.Label1 = Label(self.frame, text="This is what the Team Member sees")
        self.Label1.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        # self.Label2 = Label(self.frame, text="I am still a God")
        # self.Label2.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        # self.add_new = Button(self.frame, text="+", command=self.create)
        # self.add_new.grid(row=3,column=1, padx=10, pady=10, sticky="w")




root = Tk()
TadpoleUI = TadPole(root)
root.mainloop()



    