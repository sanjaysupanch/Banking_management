import pymysql
import time
import datetime
import os
from collections import OrderedDict

db= pymysql.connect("localhost","root","asdfjkl;jk","bank")
cur = db.cursor()

def viewprofile(username):
	cur.execute("""SELECT * FROM users WHERE username = %s""",username)
	data  = cur.fetchall()
	data=data[0]
	user=OrderedDict()
	user['Account Number'] = data[0]
	user['Name']= data[1]+" "+data[2]+" "+data[3]
	user['Gname'] = data[4]+" "+data[5]+" "+data[6]
	user['Email'] = data[7]
	user['Mob'] = data[8]
	user['House No'] = data[9]
	user['City'] = data[10]
	user['District'] = data[11]
	user['State'] = data[12]
	user['Age'] = data[13]
	user['sex'] = data[14]
	user['Debit Card No'] = data[15]
	user['Balance'] = data[17]
	user['Aadhar'] = data[22]
	user['Pan'] = data[23]
	user['Nominee \'s Name']=data[24]+" "+data[25]+" "+data[26]
	user['Last Modified'] = data[27]	
	for key in user.keys():
		print(key,":",user[key])
	db.commit()
#viewprofile("technical.c17")

def viewstatement(username):
	cur.execute("""SELECT * FROM transactions WHERE username = %s""",username)
	#s = """Date\t\t\tDescription \t\t Withdraw\tDeposit\t\tRemaining\tUsername\t\tComment """
	s = ["Date","Description","Withdraw","Deposit","Remaining","Username","Comment"]
	for i in s:
		print(i.ljust(20," "),end = "")
	print()
	data = cur.fetchall()
	for i in data:
		for j in i:
			j = str(j)
			print(j.ljust(20," "),end = "")
		print('\n')
	db.commit()

# viewstatement('akshay.k17')