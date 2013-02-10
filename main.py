#!/usr/bin/python2
import sys
import argparse
import makerar 
import sendemail
import librar.file_helper
import getpass
import os 
import fnmatch
parser = argparse.ArgumentParser(description = 'Split a file into rarparts and email')
parser.add_argument('-t','--to',  type = str, nargs = '+', help = 'who to send email to ')
parser.add_argument('-f','--from', dest = 'fromAddress' , type = str, nargs = '+', help = 'your email address')
parser.add_argument('--filename',metavar='file',type = str, nargs = '+', help = 'path to file to send')
parser.add_argument('--subject',metavar='subject',type = str, nargs = '+', help = 'Email subject')
parser.add_argument('-s',metavar = 'smtp host',type = str, nargs = '+', help = 'smtp hostname, such as smtp.gmail.com')
parser.add_argument('--use_pass',  action='store_true',  help = 'to use a password')

args =  parser.parse_args()

if args.use_pass:
    password = getpass.getpass('Enter RAR Password Now \n')
else:
    password = " "
if args.subject:
    subject = args.subject[0]
else:
    subject = 'VACATION PHOTOS'

rarFileName = librar.file_helper.get_random_temp_dir_name(basedir="/tmp") 
makerar.makeArchive(rarFileName + '.rar',os.path.dirname(args.filename[0]),password,os.path.abspath(args.filename[0]))
srv = sendemail.connectToServer(args.fromAddress[0],args.s[0])
parts = fnmatch.filter(os.listdir('/tmp'),os.path.basename(rarFileName)+'.part*'+'.rar')
lenparts = str(len(parts))

for i,part in enumerate(parts):
    msg = sendemail.makeMessage(args.fromAddress[0],args.to,'/tmp/'+part,subject + ' [' +  str(i+1)+'/'+lenparts +']')
    sendemail.sendMessage(srv,args.fromAddress[0],args.to,msg)









