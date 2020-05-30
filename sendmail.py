#!/usr/bin/env python
# coding: utf-8




import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

email = 'Sender email'
password = 'Sender email password'
send_to_email = 'pm68199@gmail.com'
subject = 'Model Accuracy'
message = "Hey Developer!!! Check your final Model Accuracy after all tweaking. Now your model is giving desired accuracy."

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject



