import random
# li=[m for m in range(6)]
# random.shuffle(li)
# msg=" "
# for x in li:
# 	msg=msg+str(x)
def sendsms(to_no,msg):
	from twilio.rest import Client
	account_sid = "ACb19a998489ba4d3d6b2fd997991dd5f3"
	auth_token = "611a4bae77bab190000854e59847968f"

	client = Client(account_sid, auth_token)

	client.api.account.messages.create(
		to=to_no,
		from_="+18583041295",
		body=msg)

# sendsms("+918555892745","Chotu")