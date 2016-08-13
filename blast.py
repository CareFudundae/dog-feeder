#grab username and password from myinfo.config file
with open('myinfo.config') as f:
  credentials = [x.strip().split(':') for x in f.readlines()]
  
for username,password in credentials:
  print('credentials')
