import mysqlfile
class transmission:
	def __init__(self,username):
		self.username = username
		self.low='0'
		self.medium='0'
		self.high = '0'
		self.serial = ''
		self.current = ''

class transmission_data:
	def __init__(self,username):
		self.username = username
		self.l2l =''
		self.l2m = ''
		self.l2h = ''
		self.m2l = ''
		self.m2m = ''
		self.m2h = ''
		self.h2l = ''
		self.h2m = ''
		self.h2h = ''
		self.current = ''
		self.next = ''

def fill_transmission(node,x):
	def __init__(self):
		pass
	y = x[0]
	node.l2l,node.l2m,node.l2h = y[0],y[1],y[2]
	y = x[1]
	node.m2l,node.m2m,node.m2h = y[0],y[1],y[2]
	y = x[2]
	node.h2l,node.h2m,node.h2h = y[0],y[1],y[2]

	for i in range(0,3):
		if x[i][3] == '1':
			if i == 0:
				node.current = 'L'
			elif i == 1:
				node.current = 'M'
			else:
				node.current = 'H'
			return node

class emmision():
	def __init__(self,username):
		self.username = username
		self.low = ''
		self.medium = ''
		self.high = ''

def fill_emmision(node):
	x = mysqlfile.take_emmision_data(node.username)
	
	node.low = x[0][0]
	node.medium = x[0][1]
	node.high = x[0][2]

	return node

