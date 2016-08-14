import time
import smtplib
import email
import email.mime.application
import sys

from datetime import datetime
#from smtplib import SMTP
#from smtplib import SMTPException
#from email.mime.image import MIMEImage
#from email.mime.multipart import MIMEMultipart

#grab username and password from myinfo.config file
with open('myinfo.config') as f:
  credentials = [x.strip().split(':') for x in f.readlines()]

#print(credentials)
  
#for usr,pwd,to_address in credentials:
for cred1,cred2,cred3 in credentials:
  usr=cred1
  pwd=cred2
  to_address=cred3




#send email with attachment 
f_time = datetime.now().strftime('%a %d %b @ %H:%M')

subject = 'dog-feeder animation ' + f_time
print(subject)

#msg = MIMEMultipart()
msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = subject
msg['From'] = usr
msg['To'] = to_address
#msg.preamble = "Photo @ " + f_time

filename = 'animation.gif'
fp = open(filename, 'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype=type)
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)

print('sending email...')
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(usr,pwd)
s.sendmail(usr,to_address, msg.as_string())
s.quit()
print('email sent')


#img = MIMEImage(fp.read())
#fp.close()
#msg.attach(img)

#try:
#   s = smtplib.SMTP('smtp.gmail.com',587)
#   s.ehlo()
#   s.starttls()
#   s.ehlo()
#   s.login(user = usr,password = pwd)
#   s.sendmail(usr, to_address, msg.as_string())
#   s.quit()

#except:
#   print ("Error: unable to send email")
#except SMTPException as error:
#      print "Error: unable to send email :  {err}".format(err=error) 
