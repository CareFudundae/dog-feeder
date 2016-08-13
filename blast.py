import smtplib
#grab username and password from myinfo.config file
with open('myinfo.config') as f:
  credentials = [x.strip().split(':') for x in f.readlines()]

#print(credentials)
  
for usr,pwd,to_address in credentials:
#  print(credentials)
#  print(usr)
#  print(pwd)
#  print(to_address)
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(usr, pwd)
 
  msg = "test message from pi"
  server.sendmail(usr, to_address, msg)
  server.quit()
