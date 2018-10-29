import pymysql
import time
import datetime
import validate


db= pymysql.connect("localhost","root","asdfjkl;jk","bank")
cur = db.cursor()

def profile(username):
	cur.execute("""SELECT * FROM users WHERE username =%s""",username)
	details = (cur.fetchall())
	details = details[0]

def transfer(username):
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	accno = validate.getaccno()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~			
	trnsbal = validate.getbalance()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~			
	comment = input("What is this for:")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	confirm = validate.getconfirmation()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#print(username)
	x = username
	bal = ""
	cur.execute("""SELECT balance FROM users WHERE username = %s """,x)
	balance = (cur.fetchall())
	balance = str(balance[0][0])
	if balance.isalpha():
		balance = 0
		bal = 0
	# else:
	# 	bal = int(balance)-int(trnsbal)
	flag = 1
	if int(balance) < int(trnsbal) :
		print("Your balance is too low for this transaction")
		flag = 0
	else:
		bal = int(balance) - int(trnsbal)
		print("Remaining balance",end="")
		print(bal)
		print(balance)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	if confirm == 'Y' and flag == 1:
		
		cur.execute("""UPDATE users SET balance = %s,lastmodified = %s WHERE username = %s """,
			(bal,time.asctime(time.localtime()),username))
		cur.execute("""INSERT INTO transactions(date,description,comment,withdraw,remaining,username)
		VALUES (%s,%s,%s,%s,%s,%s) """,(str(datetime.date.today()),accno,comment,trnsbal,bal,username))
		db.commit()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	cur.execute("SELECT acc_no FROM users")
	accnos = str(cur.fetchall())
	user_name = ""
	balance = ''
	if accno in accnos:
		user_accno = ""
		cur.execute("""SELECT acc_no FROM users WHERE username = %s """,username)
		user_accno = cur.fetchall()
		user_accno = user_accno[0][0]
		cur.execute("""SELECT username FROM users WHERE acc_no = %s """,accno)
		user_name  = cur.fetchall();
		user_name = user_name[0][0]
		cur.execute("""SELECT balance FROM users WHERE acc_no = %s """,accno)
		balance = cur.fetchall()
		balance = balance[0][0]
		if balance == 'None':
			balance = '0'
		balance = int(balance) + int(trnsbal)
		cur.execute("""UPDATE users SET balance = %s WHERE acc_no = %s """,
			(balance,accno))
		cur.execute("""INSERT INTO transactions(date,description,comment,deposit,remaining,username)
		VALUES (%s,%s,%s,%s,%s,%s) """,(str(datetime.date.today()),user_accno,comment,trnsbal,balance,user_name))
		db.commit()
		

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#transfer("akshay.k17")
db.close()

