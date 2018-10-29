import easyimap
import re
import smtplib
import pymysql

def reply_mail(user,pasword):
	login = user
	password = pasword
	imapper = easyimap.connect('imap.gmail.com', login, password)
	for mail_id in imapper.listids(limit=1):
		mail = imapper.mail(mail_id)
		sender=mail.from_addr
		strt_in=0
		for x in range(len(sender)):
			if(sender[x]=="<"):
				strt_in=x
				break
		sender=sender[strt_in+1:len(sender)-1]
		body=mail.body
		regx=re.compile(r'statement',re.I)
		a=regx.findall(body)
		if(len(a)!=0):
			db= pymysql.connect("localhost","root","AmAn@2686","bank")
			cur = db.cursor()
			cur.execute("""SELECT username FROM users WHERE email = %s""",sender)
			data  = cur.fetchall()
			u_name=data[0]
			cur.execute("""\n\nSELECT * FROM transactions WHERE username = %s""",u_name)
			data  = cur.fetchall()
			msg="   DATE   "+"DESCRIPTION "+" WITHDRAW "+" DEPOSIT "+" REMAINING "+" COMMENT"+"\n"
			for x in range(len(data)):			
				msg+=data[x][0]+"    "+data[x][1]+"       "+str(data[x][2])+"      "+str(data[x][3])+"     "+str(data[x][4])+"      "+data[x][6]+"\n"
			print(msg)
		regx=re.compile(r'balance',re.I)
		a=regx.findall(body)
		if(len(a)!=0):
			db= pymysql.connect("localhost","root","AmAn@2686","bank")
			cur = db.cursor()
			cur.execute("""SELECT username FROM users WHERE email = %s""",sender)
			data  = cur.fetchall()
			u_name=data[0]
			cur.execute("""SELECT  remaining FROM transactions WHERE username = %s""",u_name)
			data  = cur.fetchall()
			x=len(data)-1
			msg="\n\nBalance:"+str(data[x])
			connection = smtplib.SMTP('smtp.gmail.com' , 587)
			connection.ehlo()
			connection.starttls()
			connection.login('projectpython3@gmail.com','8555892745')
			connection.sendmail('projectpython3@gmail.com',sender,msg)
			connection.quit()
			db.close()
			
reply_mail('projectpython3@gmail.com','8555892745')
