import pymysql as db

try:
    connection = db.connect(host='cs1.ucc.ie',
                            user='ld8',
                            password='soodi',
                            database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)


    # project_ID = cursor.execute("SELECT ID FROM Projects WHERE name = %s;", (project_name))
    cursor.execute("INSERT INTO Users VALUES (%s, %s, %s)", ("username3", "email", "encrypted_password"))
    # cursor.execute("INSERT INTO Projects(Leader, Name) VALUES(%s, %s);", ("cool epic leader", "cool epic project"))
    #
    # cursor.execute("INSERT INTO Teams(Name) VALUES(%s);", ("guy"))
    # cursor.execute("INSERT INTO Ponds(Name) VALUES(%s);", ("guy"))

    # cursor.execute("INSERT INTO Tasks(Name, Desc, Deadline) VALUES(%s, %s, %s);", ("name", "desc", "deadline"))

    connection.commit()
    print("success")
    cursor.close()
    connection.close()
except db.Error:
    print("failure")
