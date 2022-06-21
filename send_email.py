def email_sender():
    import smtplib as smtp
    connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
        
    email_addr = 'the.hub.pp3@gmail.com'
    email_passwd = 'rmvirccjqikzpdcx'
    connection.login(email_addr, email_passwd)
    connection.sendmail(from_addr=email_addr, to_addrs='alan17wilson@gmail.com', msg="Sent from my IDE. Hehe")
    connection.close()
