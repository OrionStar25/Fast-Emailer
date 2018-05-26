import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = raw_input("Your email address: ")
frompass = raw_input("Your PASSWORD: ")
toaddr = raw_input("EMAIL ADDRESS YOU SEND TO: ")
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = raw_input("SUBJECT OF THE EMAIL: ")
 
body = raw_input("TEXT YOU WANT TO SEND: ")
 
msg.attach(MIMEText(body, 'plain'))

 
# filename = "NAME OF THE FILE WITH ITS EXTENSION"
# attachment = open("PATH OF THE FILE", "rb")
 
# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
# msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, frompass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print("Done!")

#add multiple contact lists
#add attachments
#import body from a text file
#add signatures
#add bcc, cc