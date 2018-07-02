import smtplib
import getpass
from os.path import basename
from email.mime.application import MIMEApplication
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from contacts import *

# Add body content here
def get_body(name, age):
	body = "Happy birthday " + name + "! You're " + age + " years old now."
	return body


def get_details():
	fromaddr = raw_input("Your email address: ")
	frompass = getpass.getpass(prompt='Password: ', stream=None)	
	subject = raw_input("SUBJECT OF THE EMAIL: ")

	print("Sending.....")

	for name,age,toaddr in zip(Names,Ages,Emails):	
		msg = MIMEMultipart()
		msg['Subject'] = subject
		msg['From'] = fromaddr	
		msg['To'] = toaddr
		msg.attach(MIMEText(get_body(name,age)))

		for f in Files or []:
		    with open(f, "rb") as fil:
		    	part = MIMEApplication(fil.read(), Name=basename(f))
		    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
		    msg.attach(part)

		send_email(fromaddr, frompass, toaddr, msg)



def send_email(fromaddr, frompass, toaddr, msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, frompass)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()	
 


def main():
	get_details() 
	print("Done!")
  
if __name__== "__main__":
	main() 