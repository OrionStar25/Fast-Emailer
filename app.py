import smtplib
import socks
import getpass
from os.path import basename
from email.mime.application import MIMEApplication
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from contacts import *
from body import *


def get_details():
	fromaddr = raw_input("Your email address: ")
	frompass = getpass.getpass(prompt='Password: ', stream=None)	
	subject = raw_input("SUBJECT OF THE EMAIL: ")
	# username = os.getenv("proxy_username")
 #    password = os.getenv("proxy_password")
    
	print("Sending.....")

	for name,age,toaddr in zip(Names,Ages,Emails):	
		msg = MIMEMultipart()
		msg['Subject'] = subject
		msg['From'] = fromaddr	
		msg['To'] = toaddr
		msg.attach(MIMEText(message.format(Name=name, Age=age)))

		for f in Files or []:
		    with open(f, "rb") as fil:
		    	part = MIMEApplication(fil.read(), Name=basename(f))
		    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
		    msg.attach(part)

		send_email(fromaddr, frompass, toaddr, msg, username, password)



def send_email(fromaddr, frompass, toaddr, msg, username, password):
	# #socks.setdefaultproxy(TYPE, ADDR, PORT)
	# socks.setdefaultproxy(socks.SOCKS5, '172.31.1.3', 8080)
	# socks.wrapmodule(smtplib)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	# server.login(username, password) # optional
	server.login(fromaddr, frompass)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()	
 


def main():
	get_details() 
	print("Done!")
  
if __name__== "__main__":
	main() 