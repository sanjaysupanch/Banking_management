import pymysql
import passwd
db= pymysql.connect("localhost","root","asdfjkl;jk","bank")
cur = db.cursor()
cur.execute("""SELECT balance FROM users WHERE username = %s ""","rahul.p")
balance = (cur.fetchall())
balance = str(balance[0][0])
print(int(balance))
print(int(balance) - 100)
print(balance.isalpha())