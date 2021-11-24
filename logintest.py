from html import escape
import pymysql as db

def login(username, password):
    #username = escape(input("Username: ").strip())
    #password = escape(input("Password: ").strip())
    print(username, password)
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT * FROM Users
                        WHERE Username = %s
                        AND Pword = %s""", (username, password))
    if cursor.rowcount == 0:
        print("Error: incorrect user name or password")
    else:
        print("Success!")
    cursor.close()
    connection.close()
    return None
