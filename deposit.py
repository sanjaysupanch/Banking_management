import pymysql
import time
import datetime
import validate
import mysqlfile

db= pymysql.connect("localhost","root","asdfjkl;jk","bank")
cur = db.cursor()

class user:
	def __init__(self):
		self.username=""
		self.deposit = '0'.ljust(16,' ')
		self.withdraw = '0'.ljust(16,' ')
		self.description = ""
		self.comment = ""
		self.balance = ''

def deposit(username):

	node = user()
	node.username = username
	node.deposit = validate.getbalance()
	node.comment = input("Enter any comment:")
	
	bal = mysqlfile.get_Balance(username)
	bal = int(bal) + int(node.deposit)
	node.balance = bal
	node.description = "Cash".ljust(16,' ')
	
	mysqlfile.update_balance(node)
	mysqlfile.insert_transaction(node)
		
	print("Successfully Deposited")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def withdraw(username):
	node = user()
	person['balance'] = validate.getbalance()
	node.username = username
			
	node.comment = input("Enter any comment:")

	bal = mysqlfile.get_Balance(username)
	node.balance = int(bal) - int(person['balance'])
	node.description = "Cash"+" "*11
	node.withdraw = 0
	node.deposit = 0
	mysqlfile.update_balance(node)
	mysqlfile.insert_transaction(node)
	print("Successfully Withdrawn")

def transfer(username):
	node = user()
	reciever = user()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person = {}
	node.username = username
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	node.description = validate.getaccno()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~			
	person['trnsbal'] = validate.getbalance()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~			
	node.comment = input("What is this for:")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	person['confirm'] = validate.getconfirmation()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	
	x = username
	node.balance = ""
	person['balance'] = mysqlfile.get_Balance(username)
	if person['balance'].isalpha():
		person['balance'] = 0
		node.balance = 0
	else:
		node.balance = int(person['balance'])-int(person['trnsbal'])
	flag = 1
	if int(person['balance']) < int(person['trnsbal']) :
		print("Your balance is too low for this transaction")
		flag = 0
	

	node.withdraw = person['trnsbal']
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	if person['confirm'] == 'Y' and flag == 1:
		
		mysqlfile.update_balance(node)
		mysqlfile.insert_transaction(node)
	accno = node.description
	
	accnos = mysqlfile.get_accnos()
	user_name = ""
	balance = ''
	if accno in accnos:
		person2 = {}
		reciever.comment = node.comment
		reciever.description = mysqlfile.get_accno(username)
		
		reciever.username = mysqlfile.get_username(node.description)
		
		balance = mysqlfile.get_Balance(reciever.username)
		if balance == 'None':
			balance = '0'
		reciever.balance = int(balance) + int(person['trnsbal'])
		reciever.deposit = person['trnsbal']
		reciever.withdraw = 0
		mysqlfile.update_balance(reciever)
		mysqlfile.insert_transaction(reciever)
		db.commit()
