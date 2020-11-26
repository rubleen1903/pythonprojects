import smtplib

gmail_user = 'rubleen16@gmail.com'
gmail_password = 'Shinobi2201'

sent_from = gmail_user
to = ['rubleen16@gmail.com', 'hanjrarubleen@gmail.com']
subject = 'Hey bro !'
body = 'Hey, whats up?\n\n- Rubleen'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!') 
except:
    print ('Something went wrong...')