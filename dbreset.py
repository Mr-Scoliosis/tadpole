import pymysql as db

try:
    connection = db.connect(host='cs1.ucc.ie',
                            user='ld8',
                            password='soodi',
                            database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)

    dropSQL = "DROP TABLE IF EXISTS Tasks, Lilypads, Ponds, Teams, Projects, Users;"

    userSQL = "CREATE TABLE Users ( Username varchar(20) NOT NULL, Pword varchar(20) NOT NULL, Email varchar(20) NOT NULL, PRIMARY KEY (Username) );"
    projectSQL = "CREATE TABLE Projects ( ID int AUTO_INCREMENT, Leader varchar(20) NOT NULL, Name varchar(20) NOT NULL, PRIMARY KEY (ID) );"
    teamSQL= "CREATE TABLE Teams ( ID int AUTO_INCREMENT, Name varchar(20) NOT NULL, Project_ID int NOT NULL, PRIMARY KEY (ID) );"
    pondSQL = "CREATE TABLE Ponds ( ID int AUTO_INCREMENT, Name varchar(20) NOT NULL, Project_ID int NOT NULL, PRIMARY KEY (ID) );"
    lilypadSQL = "CREATE TABLE Lilypads ( ID int AUTO_INCREMENT, Name varchar(20) NOT NULL, Pond_ID int NOT NULL, PRIMARY KEY (ID) );"
    taskSQL = "CREATE TABLE Tasks ( ID int AUTO_INCREMENT, Name varchar(20) NOT NULL, Descrpt varchar(200) NOT NULL, Deadline DATE, Status INT(3) NOT NULL, Lilypad_ID int NOT NULL, PRIMARY KEY (ID) );"

    cursor.execute(dropSQL)

    cursor.execute(userSQL)
    cursor.execute(projectSQL)
    cursor.execute(teamSQL)
    cursor.execute(pondSQL)
    cursor.execute(lilypadSQL)
    cursor.execute(taskSQL)


    connection.commit()
    print("success")
    cursor.close()
    connection.close()
except db.Error:
    print("failure")
