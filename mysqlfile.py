import pymysql
import time
import datetime
import class_bank
import transmission_class
db= pymysql.connect("localhost","root","asdfjkl;jk","bank")
cur = db.cursor()


def insertvalues(person):
	cur.execute("""INSERT INTO users(acc_no,f_name,m_name,l_name,gfname,gmname,
	glname,aadhar,pan,email,mob,addhouse_no,
	addcity,adddistt,addstate,age,sex,
	password,username,nfname,nmname,nlname,debcard_no,debcard_type,lastmodified,ifsc_code,balance) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
	%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """,
	(person["accno"],person["fname"],person["mname"],person["lname"]
		,person["gfname"],person["gmname"],person["glname"],person["aadhar"],person["pan"],person["email"]
		,person["phone"],person["addhouseno"],person["addcity"],person["adddistt"],person["addstate"],person["age"],
		person["gender_"],person["password"],person["username"],person["nfname"],person["nmname"],
		person["nlname"],person["debcard"],person["debcardtype"],time.asctime(time.localtime()),"SBIN0",'0'))
	db.commit()
	db.close()

def strexecute(command):
	cur.execute(command)
	return str(cur.fetchall())
def execute(command):
	cur.execute(command) 
	return cur.fetchall()
def getUserNames():
	s = """SELECT username FROM users """
	return strexecute(s)
def getDebitCardNos():
	s = "SELECT debcard_no FROM users"
	return strexecute(s)
def getBankStatement(username):
	s = "SELECT * FROM transactions WHERE username = \'{0}\'".format(username)
	balance = execute(s)
	return balance[0]

def get_Balance(username):
	s = "SELECT balance FROM users WHERE username = \'{0}\' ".format(username)
	return str(execute(s)[0][0])
def update_balance(person):
	cur.execute("""UPDATE users SET balance = %s,lastmodified = %s WHERE username = %s """,
			(person.balance,time.asctime(time.localtime()),person.username))
	db.commit()
	db.close()
def insert_transaction(deposit):
	cur.execute("""INSERT INTO transactions(date,description,comment,withdraw,deposit,remaining,username)
		VALUES (%s,%s,%s,%s,%s,%s,%s) """,(str(datetime.date.today()),deposit.description,deposit.comment
			,deposit.withdraw,deposit.deposit,deposit.balance,deposit.username))
	db.commit()
	db.close()
def get_accnos():
	s = "SELECT acc_no FROM users"
	return strexecute(s)
def get_accno(username):
	s = "SELECT acc_no FROM users WHERE username = \'{0}\' ".format(username)
	return str(execute(s)[0][0])

def get_username(accno):
	s = "SELECT username FROM users WHERE acc_no = \'{}\'".format(accno)
	return str(execute(s)[0][0])

def create_transmission(username):
	for i in range(1,4):
		cur.execute( """INSERT INTO transmission (low,medium,high,username,curr_state,sl_no)
		 VALUES(%s,%s,%s,%s,%s,%s) """,('0','0','0',username,'0',i))
		db.commit()
		
	db.close()

def update_transmission(person):
	cur.execute( """UPDATE transmission SET low = %s,medium=%s,high=%s,curr_state=%s
		 WHERE username = %s and sl_no = %s""",(person.low,person.medium,person.high,person.current,
		 	person.username,person.serial))
	db.commit()
	db.close()

def take_transmission_data(username):
	cur.execute("""SELECT low,medium,high,curr_state from transmission where username =  %s""",username)
	x = cur.fetchall()
	db.close()
	return x

def insert_emission(username):
	cur.execute("""	INSERT INTO emmision (low,medium,high,username) VALUES('0','0','0',%s) """,username)
	db.commit()
	db.close()

def take_emmision_data(username):
	cur.execute(""" SELECT low,medium,high from emmision where username = %s""",username)
	s = cur.fetchall()
	db.close()
	return s
def update_emmision(person):
	cur.execute(""" UPDATE emmision SET low = %s,high = %s , medium = %s where username = %s""",(person.low,
		person.high,person.medium,person.username))
	db.commit()
	db.close()