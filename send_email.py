#importing yagmail and its packages
import yagmail

yagmail.register('the.hub.pp3@gmail.com', 'rmvirccjqikzpdcx')

try:
    #initializing the server connection
    yag = yagmail.SMTP(user='the.hub.pp3@gmail.com', password='rmvirccjqikzpdcx')

    #sending the email
    yag.send(to='gisawear@gmail.com', subject='Testing Yagmail', contents='Hurray, it worked!')
    print("Email sent successfully")

except:
    print("Error, email was not sent")