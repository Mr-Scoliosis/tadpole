import pymysql as db

try:
    connection = db.connect(host='cs1.ucc.ie',
                            user='ld8',
                            password='soodi',
                            database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)


    user_name = "username2"

    project_name = "cool epic projecz"

    cursor.execute("INSERT INTO Projects(Leader, Name) VALUES(%s, %s);", (user_name, project_name))

    project_ID = str(cursor.execute("SELECT ID FROM Projects WHERE name = %s;", (project_name)))
    print(project_ID, type(project_ID))
    cursor.execute("INSERT INTO Teams(Name, Project_ID) VALUES(%s, %s);", ("group of guys", project_ID))


    # cursor.execute("INSERT INTO Users VALUES (%s, %s, %s)", (username, "email", "encrypted_password"))
    # cursor.execute("INSERT INTO Ponds(Name) VALUES(%s);", ("guy"))

    # cursor.execute("INSERT INTO Tasks(Name, Desc, Deadline) VALUES(%s, %s, %s);", ("name", "desc", "deadline"))

    connection.commit()
    print("success")
    cursor.close()
    connection.close()
except db.Error:
    print("failure")
