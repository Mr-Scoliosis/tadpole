from html import escape
import pymysql as db

username = escape(input("Username: ").strip())
password = escape(input("Password: ").strip())
password2 = escape(input("Confirm Password: ").strip())
if not username or not password or not password2:
    print("Error: You must enter a user name and password.")
elif len(username) > 20:
    print("Error: Your username may not exceed 20 characters.")
elif password != password2:
    print("Error: Your passwords must match.")
elif len(password) > 20:
    print("Error: Your password is too long.")
else:
    connection = db.connect(
        host='cs1.ucc.ie',
        user='ld8',
        password='soodi',
        database='cs2208_ld8')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT * FROM Users
                        WHERE Username = %s""", (username))
    if cursor.rowcount != 0:
        print("Error: Username already taken.")
    else:
        print("Success!")
        '''cursor.execute("""INSERT INTO Users
                        VALUES(%s, %s)""", (username, password))'''
    cursor.close()
    connection.close()
