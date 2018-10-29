

import passwd
import getpass
import mysqlfile
import random
import math
import sendemail
import send_sms
def generateOTP():
	a = random.random()
	a = a * 1000000
	a = math.ceil(a)
	return str(a)

def masking(user_email):
	temp = ""

	for i in user_email:
		if i != '@':
			temp = temp + i
		else:
			break
	x = 2*len(temp)
	x = x//3
	y = 'X'*x
	y = y+user_email[x:]
	return y

def getOTP(maskedemail):
	a = int(input("Enter the OTP sent to your Email: "+maskedemail+" :  \n"))
	return str(a)
def verifyOTP(user_email):
	OTP = str(generateOTP())

	try:
		sendemail.sendemail(user_email,OTP)
		import loading
	except:
		print("Email Id not found!!!")
		return 2
	maskedemail = masking(user_email)
	usersOTP = getOTP(maskedemail)
	if(usersOTP == OTP):
		s2 = """
					Email Verified
					Please Continue....
		 """
		print(s2)
		return 1
	else:
		print("Incorrect OTP!!! Try Again")
		return 0

	return getemail()

def verifyEmail(user_email):
	x = verifyOTP(user_email)
	if x == 1:
		return 1
	elif x == 0:
		s=	"""
			Press 
				1: To get OTP again
				

				Enter Your Choice:
			"""
		print(s)
		choice = input()
		if choice == '1':
			return verifyEmail(user_email)
		else:
			return 2


def getemail():		
	email = ""
	email = input("Enter your Email id *:")
	if "@" in email and "." in email :
		if verifyEmail(email) == 1:
			return email
		else :

			return getemail()
	else:
		print("Email id is not valid:")
		return getemail() 

def verifyPhone(mob):
	x = verifyPhoneOTP(mob)
	if x == 1:
		return 1
	elif x == 0:
		s=	"""
			Press 
				1: To get OTP again
				
				2: Change Mobile Number
				Enter Your Choice:
			"""
		print(s)
		choice = input()
		if choice == '1':
			return verifyPhone(mob)
		else:
			return 2	
def getPhoneOTP(mob):
	return input("Enter the OTP sent to +91"+mob+": ")

def verifyPhoneOTP(mob):
	OTP = str(generateOTP())

	try:
		send_sms.sendsms("+91"+str(mob),OTP)
	except:
		print("Phone Number Not Found!!!")
		return 2
	usersOTP = getPhoneOTP(mob)
	if(usersOTP == OTP):
		s2 = """
					Phone Number Verified
					Please Continue....
		 """
		print(s2)
		return 1
	else:
		print("Incorrect OTP!!! Try Again")
		return 0

def getfname():
	fname=""
	fname=input("Enter Your First Name*:")
	fname = fname.strip()
	if fname.isalpha():
		return fname.title()
	else:
		print("First Name is not in correct format!!!")
		return getfname()
def getmname():
	mname=""
	mname = input("Enter Your Middle Name(optional):")
	mname = mname.strip()
	if mname.isalpha() or len(mname) == 0:
		return mname.title()
	else:
		print("Middle Name is not in correct format!!!")
		return getmname()
def getlname():
	lname=""
	lname=input("Enter Your Last Name:")
	lname = lname.strip()
	if lname.isalpha() or len(lname) == 0:
		return lname.title()
	else:
		print("Last Name is not in correct format!!!")
		return getlname()

def getage():
	age=""
	age = (input("Enter your age*:"))
	age=age.strip()
	if age.isdigit():
		return age
	else:
		print("Enter the correct age!!!")
		return getage()
def getsex():
	sex=""
	sex=input("Enter your gender ('M','F', or 'OTHER')*:")
	sex = sex.strip()
	sex = sex.upper()
	if sex == 'M' or sex == 'F' or sex == 'OTHER':
		return sex
	else:
		print("Enter the valid gender!!!")
		return getsex()
def getgfname():
	gfname = ""
	gfname=input("Enter Your Father/Guardian/Husband 's' First Name*:")
	gfname = gfname.strip()
	if gfname.isalpha() and len(gfname)>0:
		return gfname.title()
	else:
		print("Name is not in correct format!!!")
		return getgfname()
def getgmname():
	gmname = ""
	gmname = input("Enter Your Father/Guardian/Husband 's' Middle Name(optional):")
	gmname = gmname.strip()
	if gmname.isalpha() or len(gmname) == 0:
		return gmname.title()
	else:
		print("Name is not in correct format!!!")
		return getgmname()
def getglname():
	glname = ""
	glname=input("Enter Your Father/Guardian/Husband 's' Last Name:")
	glname = glname.strip()
	if glname.isalpha() or len(glname) == 0:
		return glname.title()
	else:
		print("Name is not in correct format!!!")
		return getglname()
def getaadhar():
	aadhar = input("Enter your 12 digits AADHAR number*:")
	if aadhar.isdigit() and len(aadhar) == 12:
		return aadhar
	else:
		print("Your AADHAR number is not correct!!!")
		return getaadhar()
def getpan():
	pan = ""
	pan = input("Enter Your 10 digits PAN number:")
	if len(pan) == 10  and pan[0:5].isalpha() and pan[5:9].isdigit() and pan[9].isalpha() or len(pan) == 0:
		return pan.upper()
	else:
		print("Enter correct PAN number!!! e.g. ABCDE1234F")
		return getpan()

def getphone():
	phone = input("Enter your Mobile number*: +91")
	if phone.isdigit() and len(phone) == 10:
		if verifyPhone(phone) == 1:
			return phone
		else:
			return getphone()
	else:
		print("Enter valid Mobile number!!!")
		return getphone()

def gethouseno():
	addhouseno = ""
	addhouseno = input("Enter Your House No. or Flat No.(optional):")
	return addhouseno.capitalize()

def getcity():
	city = ""
	city = input("Enter your city / Village:")
	if any(char.isdigit() for char in city):
		print("Enter the correct city / Village !!!")
		return getcity()
	else:
		return city.title()

def getdistrict():
	distt = input("Enter your District*:")
	if distt.isalpha() and len(distt)>=3:
		return distt.title()
	else:
		print("Enter valid District !!!")
		return getdistrict()

def getstate():
	state = input("Enter your State*:")
	if any(char.isdigit() for char in state):
		print("Enter the correct State !!!")
		return getstate()
	else:
		return state.title()

def getnfname():
	nfname = ""
	nfname=input("Enter Your Nominee's First Name(Optional):")
	nfname = nfname.strip()
	if nfname.isalpha() or len(nfname) == 0:
		return nfname.title()
	else:
		print("First Name is not in correct format!!!")
		return getnfname()

def getnmname():
	mname=""
	mname = input("Enter Nominee's Middle Name(optional):")
	mname = mname.strip()
	if mname.isalpha() or len(mname) == 0:
		return mname.title()
	else:
		print("Middle Name is not in correct format!!!")
		return getnmname()
def getnlname():
	mname=""
	mname = input("Enter Nominee's Last Name(optional):")
	mname = mname.strip()
	if mname.isalpha() or len(mname) == 0:
		return mname.title()
	else:
		print("Last Name is not in correct format!!!")
		return getnlname()

def getpassword():
	pass_word = ""
	pass_word = getpass.getpass("Enter password (6 <=length <=20 )*:")
	if len(pass_word)>=6 :
		return pass_word

	else:
		print("Enter valid password!!!")
		return getpassword()
def getpassword1(password):
	return passwd.encryption(password)
def getfinalencryption(password):
	return passwd.finalencrypt(password)
def getaccno():
	accno = ""
	accno = input("Enter Account Number in which you have to transfer:")
	accno = accno.upper()
	if accno.isalnum():
		return accno.ljust(15,' ')
	else:
		print("Enter the valid Account Number")
		return getaccno()

def getbalance():
	trnsbal = input("Enter the balance:")
	if trnsbal.isdigit():
		return str(trnsbal)
	else:
		print("Invalid balance !!!")
		return getbalance()

def getconfirmation():
	print("Are you sure to make this transaction ?")
	confirm = input("Press 'Y' to confirm 'N' to discard:" )
	confirm = confirm.upper()
	if confirm == 'Y' or confirm == 'N':
		return confirm
	else:
		print("Invalid Choice !!!")
		return getconfirmation()

def getusername():
	user_name=input("Enter username(length <= 30)* :")
	usernames = mysqlfile.getUserNames()
	if user_name not in usernames and len(user_name) <= 30 and len(user_name) >0:
		return user_name
	else:
		print("Username already exists !!! Choose other...")
		return getusername()

def WantDebitCard():
	debcard=input("Do you want Debit Card (Y/N)*:")
	debcard=debcard.upper()
	if debcard == 'Y' or debcard == 'N':
		return debcard
	else:
		print("Enter valid choice!!!")
		return WantDebitCard()

def TypeDebitCard():
	print("Select Debit Card type:\n")
	print("1-Visa \n2-Visa Electron\n3-MasterCard\n4-Contactless\n5-RuPay\nBy Default-Maestro")
	d_c=input("Enter Your choice:")
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
	return d_c_t

def getDebitCard():
		
	debcard = WantDebitCard()
	d_c_t = ""
	if debcard == 'Y':
		d_c_t = TypeDebitCard()

		debcards=mysqlfile.getDebitCardNos()
		while (1):
			
			card_no=str(random.randrange(math.pow(10,17),(math.pow(10,18)-1)))
			if card_no not in debcards:
				li = [d_c_t,str(card_no)]
				return li
	else:
		return ["Not Issued",None]