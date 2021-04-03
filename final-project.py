import smtplib  #SOURCE : https://www.youtube.com/watch?v=m9ojKEBYCvQ, https://www.youtube.com/watch?v=iICg4Vn2Rkk&t=603s
import ssl
import getpass
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Untuk login
sender = input("From: ")  
password = getpass.getpass("Password: ")  
# menaruh receive email di receiver_list.txt
with open("receiver_list.txt") as r:
    reciever = [recievers.rstrip() for recievers in r]
#membuat subject dan pesan
emailSubject = "HALO!"
emailMessage = "THIS MESSAGE WAS SENT USING PYTHON"

#membuat subject, message, from, to
msg = MIMEText(emailMessage, 'html')
msg['Subject'] = emailSubject
msg['From'] = sender
msg['To'] = ",".join(reciever)

# # Connect Gmail SMTP Server
s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
s.login(user=sender, password=password)
print('Login Success!')
s.sendmail(sender, reciever, msg.as_string())
print('Email has been sent to', reciever)
s.quit()