import pymysql
import time
import random
import math
from collections import OrderedDict


db= pymysql.connect("localhost","root","asdfjkl;jk","bank")
cur = db.cursor()


def admin(username,choice):
	cur.execute("""SELECT * FROM users WHERE username = %s""",username)
	data  = cur.fetchall()
	data=data[0]
	user=OrderedDict()
	user['Account Number'] = data[0]
	user['Name']= data[1]+" "+data[2]+" "+data[3]
	user['Guardian \'s name'] = data[4]+" "+data[5]+" "+data[6]
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
	count=1
	print("Enter the field choice you want to edit")
	for x in user.keys():
		print(count,":",x)
		count=count+1
	choice=eval(input())
	editlist(username,choice,user,data)

def editlist(username,choice,user,data):
	data_column={"1":["f_name","m_name","l_name"],"2":["gfname","gmname","glname"],"15":["nfname","nmname","nlname"],"3":"email",
	"4":"mob","5":"addhouse_no","6":"addcity","7":"adddistt","8":"addstate","9":"age","11":"debcard_no","14":"pan"}
	if(choice==2 or choice==3 or choice==16):
		keys=list(user.keys())
		print("Edit: 1.First name  2.Middle name  3.Last name")
		choice2=eval(input())
		key=keys[choice-1]
		curr_data=user[key]
		print("Current name is:",curr_data,"\nEnter the new name:")
		new=input()
		print("Are you sure to make these changes ? :[Y/N]")
		while(1):
			choice3=input()
			choice3=choice3.upper()
			if(choice3 == "Y"):
				cur.execute('UPDATE users SET %s = "%s" where username = "%s"' % (data_column[str(choice-1)][choice2-1],new,username))
				db.commit()
				break
			elif(choice3 == "N"):
				print("No changes made")
				break	
			else:
				print("Enter a valid choice")
	elif(choice==1 or choice==10 or choice==14 or choice==17):
		print("Cannot make changes in this data\n")
	else:
		keys=list(user.keys())
		key=keys[choice-1]
		curr_data=user[key]
		print("Current data is:",curr_data,"\nEnter the new data:")
		new=input()
		print("Are you sure to make these changes ? :[Y/N]")
		while(1):
			choice3=input()
			choice3=choice3.upper()
			if(choice3 == "Y"):
				cur.execute('UPDATE users SET %s = "%s" where username = "%s"'% (data_column[str(choice-1)],new,username))
				db.commit()
				break
			elif(choice3 == "N"):
				print("No changes made")
				break	
			else:
				print("Enter a valid choice")
	db.close()
		
			
def editselect():
	print("Select the username whose data you want to edit:")
	cur.execute("""SELECT * FROM users""")
	data = cur.fetchall()
	for x in range(len(data)):
		print(x+1,".",data[x][21])
	choice=eval(input())
	username=data[choice-1][21]
	admin(username,choice)

	
editselect()
	
