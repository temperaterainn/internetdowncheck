import os
import time.sleep
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("Your Email", "Password")
hostname = "https://google.com"
msg = "The internet is down. " + counter
counter = 0

while True:
  
  sleep(60)

    response = os.system("ping -c 1 " + hostname)

    if response == 0:
      pass
    else:
      server.sendmail("Your Email", "Email to send message", msg)
      server.quit()
      counter = counter + 1
