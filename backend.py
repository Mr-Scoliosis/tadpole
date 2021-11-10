import pymysql as db
import UI as frontend

connection = db.connect(
    host='cs1.ucc.ie',
    user='ld8',
    password='soodi',
    database='cs2208_ld8')
cursor = connection.cursor(db.cursors.DictCursor)

def downloadProjects(self):
    # connection

    cursor.execute("""SELECT * FROM Projects""")
    for row in cursor.fetchall():
        id = row['ID']
        leader = row['Leader']
        name = row['Name']
        self.Projects.append(Project(id, leader, name, self.frame, self.can))

    cursor.execute("""SELECT * FROM Teams""")
    for row in cursor.fetchall():
        id = row['ID']
        name = row['Name']
        project_id = row['Project_ID']
        project_above = self.get_project_by_id(project_id)
        project_above.addMembers(Team(id, name, self.can, project_above))

    cursor.execute("""SELECT * FROM Ponds""")
    for row in cursor.fetchall():
        id = row['ID']
        name = row['Name']
        project_id = row['Project_ID']
        project_above = self.get_project_by_id(project_id)
        project_above.addPond(Pond(id, name, self.can, project_above))

    cursor.execute("""SELECT * FROM Lilypads""")
    for row in cursor.fetchall():
        id = row['ID']
        name = row['Name']
        pond_id = row['Pond_ID']
        project_above = self.get_project_by_id(pond_id)
        project_above.addLilyPad(LilyPad(id, name, self.can, pond_above))


    cursor.execute("""SELECT * FROM Tasks""")
    for row in cursor.fetchall():
        id = row['ID']
        name = row['Name']
        descrpt = row["Descrpt"]
	    deadline = row["Deadline"]
        status = row["Status"]
        pond_id = row['Pond_ID']
        project_above = self.get_project_by_id(pond_id)
        project_above.addLilyPad(LilyPad(id, name, self.can, pond_above))


    # testMember = member("Testing", [], self.memberFrame)
    # testMember2 = member("Testing12", [], self.memberFrame)
    # for i in self.Projects:
    #     i.add_to_members(testMember)


    def get_project_by_id(self, project_id):
        print(self.Projects)
        for i in self.Projects:
            if i.id == project_id:
                return i

    def get_pond_by_id(self, pond_id):
        print(self.ponds)
        for i in self.ponds:
            if i.id == project_id:
                return i

    def get_lilypad_by_id(self, lilypad_id):
        print(self.Projects)
        for i in self.Projects:
            if i.id == project_id:
                return i

    connection.commit()
    cursor.close()
    connection.close()
    return






from frontend import *


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
