import smtplib
import getpass

try:
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
except:
  print("Something went wrong")

# make connection secure
server.starttls()

mypwd = getpass.getpass('Enter your password: ')  

myemail = "email@gmail.com"

recip = "email@gmail.com"

server.login(myemail, mypwd)

msg = "HELLO YOUTUBE!"

server.sendmail(myemail, recip, msg)
print("Success!")
server.quit()
