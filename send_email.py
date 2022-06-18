# importing yagmail and its packages
import yagmail

try:
    #initializing the server connection
    yag = yagmail.SMTP(user='the.hub.pp3@gmail.com', password='rmvirccjqikzpdcx')

    # yag = yagmail.SMTP("my_username@gmail.com", oauth2_file="~/oauth2_creds.json")

    #sending the email
    yag.send(to='gisawear@gmail.com', subject='Testing Yagmail', contents='Hurray, it worked!')
    print("Email sent successfully")
except:
    print("Error, email was not sent")


# yag.send(to='user1@gmail.com', cc='user2@gmail.com', bcc='user3@gmail.com', subject='Greetings...', contents='How are you?')

# yag.send(to='user1@gmail.com', subject='Greetings...', contents='<h1>How are you?</h1>')