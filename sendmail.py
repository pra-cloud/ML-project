import smtplib 
# creates SMTP session 
s = smtplib.SMTP('pm68199@gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("sender-mail", "password") 
# message to be sent 
message = "Hey Developer, Finally we got the model trained. "
# sending the mail 
s.sendmail("sender_mail", "developer_mail", message) 
# terminating the session 
s.quit()
