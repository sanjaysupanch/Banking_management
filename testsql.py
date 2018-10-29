import mysqlfile
import validate
import time
import deposit
import transmission_class
import pymysql

# node = transmission_class.emmision('chotu.f17')
# x =mysqlfile.take_emmision_data(node.username)
# node = transmission_class.fill_emmision(node)
# print(node.username,node.low)
node = transmission_class.emmision('chotu.f17')
# x = mysqlfile.take_emmision_data(node.username)

# for i in range(0,3):
# 	print(x[0][i])


node = transmission_class.fill_emmision(node)
# node.low = '4'
# node.medium = '5'
# node.high = '6'
# print(node.username)
# print(node.low,node.medium,node.high)
# mysqlfile.update_emmision(node)