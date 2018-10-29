import pymysql
import time
import random
import math
import validate
import useprofile
import newsend_email

db = pymysql.connect("localhost","root","asdfjkl;jk","bank")
cur=db.cursor()
#------------------------------------------Log In Function-------------------------------------------
def login():
	usrname = (input("Enter Your username:"))
	password = (input("Enter Your password:"))
	cur.execute("SELECT username FROM  users")
	persons=str(cur.fetchall())
	if usrname in persons:
		cur.execute("""SELECT password FROM users WHERE username =%s""",usrname)
		passwords=str(cur.fetchall())
		if password in passwords:
			print("Login Successfull !!!")
			# return usrname
			useprofile.useProfile(usrname)
		else:
			print("username and password doesn't match!!! Try Again!!!")
	else:
		print("username and password doesn't match!!! Try Again!!!")

#----------------------------------------------------------------------------------------------------
#----------------------------------------Sign Up Function-------------------------------------------
def signup():
	person={}
	accno="89360"+str(int(time.time()))
	person["accno"]=accno
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~First Name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
	person["fname"] = validate.getfname()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Middle Name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["mname"]=validate.getmname()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Last Name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["lname"]= validate.getlname()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Age~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["age"]=validate.getage()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Sex~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["gender_"] = validate.getsex()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Guardian's First Name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["gfname"]= validate.getgfname()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Guardian's Middle Name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["gmname"]=validate.getgmname()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Guardian's Last Name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["glname"]=validate.getglname()	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Aadhar~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["aadhar"] = validate.getaadhar()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Pan Card~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["pan"]=validate.getpan()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EMail~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["email"] = validate.getemail()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Phone~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["phone"] = validate.getphone()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Address House No~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["addhouseno"] = validate.gethouseno()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Address City~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["addcity"] = validate.getcity()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~District~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["adddistt"] = validate.getdistrict();
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~State~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["addstate"] = validate.getstate();
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Nominee's First name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["nfname"]=validate.getnfname()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Nominee's Middle Name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["nmname"]=validate.getnmname()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Nominee last Name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["nlname"]=validate.getlname()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Debit Card~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["debcard"] = ""
	debcard=""
	d_c_t=""
	while(1):
		debcard=input("Do you want Debit Card (Y/N)*:")
		debcard=debcard.upper()
		if debcard == 'Y' or debcard == 'N':
			break
		else:
			print("Enter valid choice!!!")

	if debcard == 'Y':
		d_c = ""
		d_c_t = ""
		while (1):
			
			print("Select Debit Card type:\n")
			print("1-Visa \n2-Visa Electron\n3-MasterCard\n4-Contactless\n5-RuPay\n6-Maestro")
			d_c=input("Enter Your choice:")
			if d_c in "123456" and len(d_c) == 1:
				if d_c == '1':
					d_c_t = "Visa"
				elif d_c == '2':
					d_c_t = "Visa Electron"
				elif d_c == '3':
					d_c_t = "MasterCard"
				elif d_c == '4':
					d_c_t = "Contactless"
				elif d_c =='5':
					d_c_t="RuPay"
				else:
					d_c_t = "Maestro"
				break
		
		cur.execute("SELECT debcard_no FROM users")
		debcards=str(cur.fetchall())
		while (1):
			
			card_no=str(random.randrange(math.pow(10,17),(math.pow(10,18)-1)))
			if card_no not in debcards:
				person["debcard"]=card_no[0:16]
				break
	person["debcardtype"] = d_c_t
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~User Name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	user_name = ""
	while (1):
		
		user_name=input("Enter username(length <= 30)* :")
		cur.execute("SELECT username FROM users")
		usernames=str(cur.fetchall())	
		if user_name not in usernames and len(user_name) <= 30:
			break
		else:
			print("Username already exists !!! Choose other...")

	person["username"] = user_name

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PassWord~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person["password"] = validate.getpassword()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~Inserting into Database~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#----------------------------------------------------------------------------------------------------

	



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#----------------------------------------------------------------------------------------------------
s = """
		Press
					1- Login
					2- SignUp
					3- Exit

		"Enter Your choice:"
	
	"""
print(s)
choice = int(input())
if choice == 1:
	login()
elif choice == 2:
	signup()




db.close()
