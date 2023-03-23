from socket import *

# import openpyxl

# dataframe = openpyxl.load_workbook("TestBook.csv")

# # Define variable to read sheet
# dataframe1 = dataframe.active
 
# # Iterate the loop to read the cell values
# for row in range(0, dataframe1.max_row):
#     for col in dataframe1.iter_cols(1, dataframe1.max_column):
#         print(col[row].value)

# import csv

# file = open('TestBook.csv')

# type(file)

import pandas as pd

sample_data = pd.read_csv('TestBook.csv')

print(sample_data.head)

print("test===================")

















msg = "\r\nHello [Agency Name], you have an upcoming appointment with [Client Name] on [Appointment Date]. Their needs are [Client Needs].\n"
msg = msg + "The client's phone number is [Client Phone Number] if more information is needed from the client.\n\n--Pathways Staff\n[Pathways Contact Information Phone & Email]"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("list.winthrop.edu", 25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO list.winthrop.edu\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
heloCommand = 'HELO list.winthrop.edu\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("Message after HELO command:" + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: pathwaystest@gmail.com\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: " + recv2)

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: owense6@mailbox.winthrop.edu\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print("After RCPT TO command: " + recv3)

# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print("After DATA command: " + recv4)

# Send message data.
subject = "Subject: Upcoming Client Appointment.\r\n\r\n" 
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body:" + recv_msg.decode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv_endmsg = clientSocket.recv(1024)
print("Response after sending the single period:" + recv_endmsg.decode())

# Send QUIT command and get server response.
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
clientSocket.close()
