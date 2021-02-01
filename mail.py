import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def mail(message,ee):
	fromaddr ="aakankshab04@gmail.com"
	toaddr = ee
	pwd="ppsuniver"

	# MIMEMultipart
	msg = MIMEMultipart()

	# senders email address
	msg['From'] = fromaddr

	# receivers email address
	msg['To'] = toaddr

	# the subject of mail
	msg['Subject'] = "Your BMI Result"

	# the body of the mail
	body = message

	# attaching the body with the msg
	msg.attach(MIMEText(body, 'plain'))

	# creates SMTP session
	email = smtplib.SMTP('smtp.gmail.com', 587)

	# TLS for security
	email.starttls()

	# authentication
	email.login(fromaddr,'ppsuniver')

	# Converts the Multipart msg into a string
	messge = msg.as_string()

	# sending the mail
	email.sendmail(fromaddr, toaddr, messge)

	# terminating the session
	email.quit()
