class user:
	def __init__(self):
		self.username=""
		self.deposit = 0
		self.withdraw = 0
		self.description = ""
		self.comment = ""
		self.balance = ''
	

def chotu(cor):
	print(cor.username)
akshay = user()
akshay.username = 'akshay.k17'
akshay.deposit = 9000
akshay.description = 'chotu'
akshay.comment = 'waah chotu'

chotu(akshay)


