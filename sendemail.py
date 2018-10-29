import smtplib


def sendemail(reciever,message):
	s = smtplib.SMTP('smtp.gmail.com', 587)
	 
	
	s.starttls()
	 
	
	s.login("projectpython3@gmail.com", "8555892745")
	 
	
	 
	
	s.sendmail("projectpython3@gmail.com", reciever, message)
	 
	
	s.quit()

for i in range(10):
	sendemail("sanjaykumarsupanch@gmail.com","Rahul Chutiya hai")