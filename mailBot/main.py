import smtplib
from database import *
from email.message import EmailMessage

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()



with open('credentials.txt', 'rt') as file:
    text_data = file.readlines()
    from_address = text_data[0][23:]
    password = text_data[1][23:]
    DB = text_data[2][29:]
    TABLE = text_data[3][26:]

to = input("To : ")
tuples = readData(DB, TABLE)

for i in tuples:
    print(i)
    while True:
        if to == i[0]:
            to_address = i[1]
            break
        else: 
            print("Contact not found")
            choice = input("Would you like to add this contact ? (Y/N) : ")
            if choice.lower() == "Y":
                to_address = input("Enter email id of the contact : ")
                insertData(DB, TABLE, to, to_address)
            else:
                to_address = input("Enter email id for temporary basis : ")
                break
    break



msg = EmailMessage()
content = input("Enter message here : \n")
msg.set_content(content)

msg['Subject'] = input("Enter the subject : ")
msg['From'] = from_address
msg['To'] = to_address

server.login(from_address, password)
server.send_message(msg)
server.quit()
