import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


def get_details():
	fromaddr = raw_input("Your email address: ")
	frompass = raw_input("Your PASSWORD: ")
	msg = MIMEMultipart()
	msg['Subject'] = raw_input("SUBJECT OF THE EMAIL: ")
	msg['From'] = fromaddr

	print("Hope you've added all the people you want to send email to in contacts.txt")

	#send every contact email
	contacts = open("contacts.txt")
	for line in contacts:
		#get names and email of contacts
		name, toaddr = line.split()
		msg['To'] = toaddr
		#get customized message	
		body = open("body.txt").read().replace("<name>", name)
		msg = MIMEText(body)
		send_email(fromaddr, frompass, toaddr, msg)
		#used for attachment purpose
		# msg.attach(MIMEText(body, 'plain'))


def send_email(fromaddr, frompass, toaddr, msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, frompass)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()	
 

get_details() 
print("Done! You can check your sent if you want :)")
 


 
# filename = "NAME OF THE FILE WITH ITS EXTENSION"
# attachment = open("PATH OF THE FILE", "rb")
 
# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
# msg.attach(part)
 


#add attachments
#add signatures
#add bcc, cc