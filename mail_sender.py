
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from web_scraper import readText

# Sender's email address and password
sender_email = 'ejcodepractices@gmail.com'
sender_password = 'cjlwgttrseeycmcb'

# Recipient's email address
recipient_email = 'ejcodepractices@gmail.com'

# Create a message object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Changes on desired advertisements page!'

# Add email body text
links = [single_link.split(',')[4] for single_link in readText()]
message.attach(MIMEText('Hello! Check the page!\n' + ' '.join(links), 'plain'))

# Connect to the SMTP server (in this case, Gmail's SMTP server)
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Establish a secure connection
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Login to your Gmail account
server.login(sender_email, sender_password)

# Send the email
server.sendmail(sender_email, recipient_email, message.as_string())

# Quit the server
server.quit()

print("Email sent successfully.")