import pymysql
import time
import random
import math
import validate
import useprofile
import verifypass
import getpass
import mysqlfile

db = pymysql.connect("localhost","root","asdfjkl;jk","bank")
cur=db.cursor()
#------------------------------------------Log In Function-------------------------------------------
def login():
	usrname = (input("Enter Your username:"))
	password = getpass.getpass("Enter Your password:")

	if usrname in mysqlfile.getUserNames():
		if verifypass.verifypassword(usrname,password):
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
	debinfo = validate.getDebitCard()

	person["debcard"] = debinfo[1]
	person["debcardtype"] = debinfo[0]
	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~User Name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	person["username"] = validate.getusername()
	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PassWord~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	password = validate.getpassword()
	person["password"] = validate.getfinalencryption(password)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~Inserting into Database~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	mysqlfile.insertvalues(person)
	mysqlfile.create_transmission(person['username'])
	mysqlfile.insert_emission(person['username'])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
