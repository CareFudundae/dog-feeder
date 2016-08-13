#grab username and password from myinfo.config file
with open('myinfo.config') as f:
  credentials = [x.strip().split(':') for x in f.readlines()]
  
for usr,pwd in credentials:
  print(credentials)
  print(usr)
  print(pwd)
