
import smtplib
import os
import sys
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def makeMessage(fromAddress,toAddress,attachmentFilename,Subject): 
    message = MIMEMultipart()
    message['From'] = fromAddress
    message['To'] = ', '.join(toAddress)
    message['Subject'] = Subject
    fid = open((attachmentFilename))
    attachment = MIMEBase('application','octet-stream')
    attachment.set_payload(fid.read())
    fid.close()
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition','attachment; filename=%s' %os.path.basename(attachmentFilename))
    message.attach(attachment)
    return  message.as_string()

def connectToServer(fromAddress,smtpSERVER):
    smtpServer = smtplib.SMTP_SSL(smtpSERVER)

    password =getpass.getpass('Enter Your Password\n')
    smtpServer.login(fromAddress,password)
    return smtpServer
def sendMessage(smtpServer,fromAddress,toAddress,msg):
    smtpServer.sendmail(fromAddress,toAddress,msg)
    


    
