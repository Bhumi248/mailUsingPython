import smtplib
import getpass
#from email.MIMEBase import MIMEBase
#from email.MIMEText import MIMEText
#import os
From=''
To=''
Subject="hi just for fun "
username=''
count=0
try:

        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.ehlo()

        while(count<20):
            server.sendmail(From,To,Subject)
            count+=1

        server.quit()

        print "succsessfully send massage"

except Exception as e:
    print e
