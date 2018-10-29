import send_email


def generateOTP():
	a = random.random()
	a = a * 10000
	a = math.ceil(a)
	return a

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
	a = int(input("Enter the OTP sent to your Email:"+maskedemail))
	return a
def verifyOTP(user_email):
	OTP = generateOTP()
	send_email.sendmail(user_email,OTP)
	maskedemail = masking(user_email)
	usersOTP = getOTP(maskedemail)
	if(usersOTP == OTP):
		return 1
	else:
		print("Incorrect OTP!!! Try Again")
		return 0
def verifyEmail(user_email):
	if verifyOTP(user_email) == 1:
		return 1
	else:
		s=	"""
			Press 
				1: To get OTP again
				2: TO verify email later

				Enter Your Choice:
			"""
		print(s)
		choice = input()
		if choice == '1':
			askforOTP(user_email)
		else:
			return 2


def getemail():		
	email = ""
	email = input("Enter your Email id (optional):")
	if "@" in email and "." in email or len(email) == 0:
		if verifyEmail('akshay.k17@iiits.in') == 1:
			print("Email Verified")
		return email
	else:
		print("Email id is not valid:")
		getemail() 