import viewprofile2
import deposit
def Menu():
	s = """ 
		Press:
			1 - View Your Profile
			2 - Make Transactions
			3 - Deposit Money
			4 - Bank Statement
			5 - Log Out
			Enter Your Choice:
		"""
	choice = int(input(s))
	li = [1,2,3,4]
	#print(li)
	if choice in li:
		return choice

def useProfile(username):
	choice = Menu()
	if choice == 1:
		viewprofile2.viewprofile(username)
		useProfile(username)
	elif choice == 2:
		deposit.transfer(username)
		useProfile(username)
	elif choice == 3:
		deposit.deposit(username)
		useProfile(username)
	elif choice == 4:
		viewprofile2.viewstatement(username)
		useProfile(username)
		return ""

