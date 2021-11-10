import pymysql as db
import UI as frontend

# connection = db.connect(
#     host='cs1.ucc.ie',
#     user='ld8',
#     password='soodi',
#     database='cs2208_ld8')
# cursor = connection.cursor(db.cursors.DictCursor)

# connection.commit()
# cursor.close()
# connection.close()




def downloadProjects(main):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    
    cursor.execute("""SELECT * FROM Projects""")
    Projects = []
    for row in cursor.fetchall():
        print("row")
        id = row['ID']
        leader = row['Leader']
        name = row['Name']
        Projects.append(frontend.Project(id, leader, name, main.frame, main.can, main.root))
    
    connection.commit()
    cursor.close()
    connection.close()

    return Projects

def get_project_by_id(self, project_id):
    print(self.Projects)
    for i in self.Projects:
        if i.id == project_id:
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
        project_id = row['Project_ID']
        project_above = project.get_project_by_id(project_id)
        project_above.addMembers(frontend.member(id, name, project.can, project_above))
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

    cursor.execute("""SELECT * FROM Ponds""")
    for row in cursor.fetchall():
        id = row['ID']
        name = row['Name']
        project_id = row['Project_ID']
        project_above = project.get_project_by_id(project_id)
        project_above.addPond(frontend.Pond(id, name, project.can, project_above))
    connection.commit()
    cursor.close()
    connection.close()


def get_pond_by_id(self, pond_id):
    print(self.ponds)
    for i in self.ponds:
        if i.id == pond_id:
            return i



def downloadLilypads(pond):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)

    cursor.execute("""SELECT * FROM Lilypads""")
    for row in cursor.fetchall():
        id = row['ID']
        name = row['Name']
        pond_id = row['Pond_ID']
        pond_above = pond.get_pond_by_id(pond_id)
        pond_above.addLilyPad(frontend.LilyPad(id, name, pond.can, pond_above))
    connection.commit()
    cursor.close()
    connection.close()


def get_lilypad_by_id(self, lilypad_id):
    print(self.Projects)
    for i in self.Projects:
        if i.id == lilypad_id:
            return i



def downloadTasks(lilypad):
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)

    cursor.execute("""SELECT * FROM Tasks""")
    #the descrpt variable is written this way as description is a keyword in
    #python, and this was the cleanest alternative
    for row in cursor.fetchall():
        id = row['ID']
        name = row['Name']
        descrpt = row["Descrpt"]
        deadline = row["Deadline"]
        status = row["Status"]
        lilypad_id = row['Lilypad_ID']
        lilypad_above = lilypad.get_lilypad_by_id(lilypad_id)
        lilypad_above.addTask(frontend.Task(id, name, descrpt, deadline, status, lilypad_above.canvas, lilypad_above))
    connection.commit()
    cursor.close()
    connection.close()






    # testMember = member("Testing", [], self.memberFrame)
    # testMember2 = member("Testing12", [], self.memberFrame)
    # for i in self.Projects:
    #     i.add_to_members(testMember)

    # return
    #these are to demonstrate downloading the projects from a database

    # user_name = "username2"
    #
    # project_name = "cool epic projecz"
    #
    # cursor.execute("INSERT INTO Projects(Leader, Name) VALUES(%s, %s);", (user_name, project_name))
    #
    # project_ID = str(cursor.execute("SELECT ID FROM Projects WHERE name = %s;", (project_name)))
    # print(project_ID, type(project_ID))
    # cursor.execute("INSERT INTO Teams(Name, Project_ID) VALUES(%s, %s);", ("group of guys", project_ID))


    # cursor.execute("INSERT INTO Users VALUES (%s, %s, %s)", (username, "email", "encrypted_password"))
    # cursor.execute("INSERT INTO Ponds(Name) VALUES(%s);", ("guy"))

    # cursor.execute("INSERT INTO Tasks(Name, Desc, Deadline) VALUES(%s, %s, %s);", ("name", "desc", "deadline"))
