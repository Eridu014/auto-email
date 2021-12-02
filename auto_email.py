import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo() #creates server


smtp_object.starttls()


#generate app password for gmail

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email, password)

#send email
from_address = email
to_address = getpass.getpass('Where would you like to send it to?: ')
subject = input("Enter the subject line: ")
message = input("enter the body message: ")

msg = "Subject: " + subject + '\n' + message
#for loop to determine how many
for x in range(1, 100, 1):
    x = smtp_object.sendmail(from_address, to_address, msg)
    x