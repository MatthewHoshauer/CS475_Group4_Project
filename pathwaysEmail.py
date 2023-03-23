from socket import *
msg = "\r\nHello [Agency Name], you have an upcoming appointment with [Client Name] on [Appointment Date]. Their needs are [Client Needs].\n"
msg = msg + "The client's phone number is [Client Phone Number] if more information is needed from the client.\n\n--Pathways Staff\n[Pathways Contact Information Phone & Email]"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("list.winthrop.edu", 25)
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end
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
# Fill in start
mailFrom = "MAIL FROM: pathwaystest@gmail.com\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: " + recv2)
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
rcptTo = "RCPT TO: owense6@mailbox.winthrop.edu\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print("After RCPT TO command: " + recv3)
# Fill in end
# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print("After DATA command: " + recv4)
# Fill in end
# Send message data.
# Fill in start
subject = "Subject: Upcoming Client Appointment.\r\n\r\n" 
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body:" + recv_msg.decode())
# Fill in end
# Message ends with a single period.
# Fill in start 
clientSocket.send(endmsg.encode())
recv_endmsg = clientSocket.recv(1024)
print("Response after sending the single period:" + recv_endmsg.decode())
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
clientSocket.close()
# Fill in end
