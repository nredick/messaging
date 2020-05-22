import smtplib 
import sms_config 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# create sms_config for login data. necessary to create a 16 char google "app password" to replace generic email password.

email = sms_config.email
pas = sms_config.pas
sms_gateway = input("Recipient phone number (10-digits, US & Canada): ") +'@vtext.com'

# Email server and smtp
smtp = "smtp.gmail.com" 
port = 587

# start the server
server = smtplib.SMTP(smtp,port)
server.starttls()

# login to email 
server.login(email,pas)

# Use the MIME module to structure the message

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = sms_gateway

while(True):
	# sms message body
	body = input("Enter SMS message: ")

	# send sms msg 
	server.sendmail(email, sms_gateway, body)
	
	if (input("Send another message? (y/n): ").lower() == 'n'):
		break
	elif(input("Change recipient? (y/n): ").lower() == 'y'):
		sms_gateway = input("Recipient phone number (10-digits, US & Canada): ") +'@vtext.com'

# quit the server
server.quit()

