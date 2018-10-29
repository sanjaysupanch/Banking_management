import pymysql
import passwd
db= pymysql.connect("localhost","root","asdfjkl;jk","bank")
cur = db.cursor()
def verifypassword(username,password):
	cur.execute("""SELECT password FROM users WHERE username =%s""",username)
	passwords=str(cur.fetchall())
	passwords = passwords[3:len(passwords)-5]
	first = passwd.encryption(password)
	db.close()
	temp = passwd.finaldecrypt(passwords,first)
	if temp == password: 
		return 1
	else :
		return 0
# print(verifypassword("aman.g12","amangupta"))