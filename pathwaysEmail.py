from socket import * # used for sending mail

import pandas as pd  # used for getting stuff from spreadsheet
import itertools     # used for iterating through lists


SHEET_ID = '1y2n-h76i_VXaba_DRtOYiPcUoQGUjvBudb0mTNfHzzc'                                              # ID associated with Google Sheets linked to Google Form
SHEET_NAME = 'Test'                                                                                    # Testing
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'      # URL to load will be the URL of the Google Sheets linked to Google Form
df = pd.read_csv(url)                                                                                  # put the data into a dataframe

agencyName = df["agency name"].iloc[-1]           # This section takes the information from each column
clientName = df["client name"].iloc[-1]           # and stores it inside a variable. This information
apptDate = df["appt date"].iloc[-1]               # is used in the print-out statement immediately
needs = df["needs"].iloc[-1]                      # below this codeblock.
clientNum = df["client phone number"].iloc[-1]    
agencyEmail = df["agency email"].iloc[-1]         

# Separates for different agency emails and names
agencyEmailList = agencyEmail.split(", ")
agencyNameList = agencyName.split(", ")

# This print statement below will print either one of two statements depending on whether or not the client has a phone number.
for (i, j) in itertools.zip_longest(agencyEmailList, agencyNameList):
    if clientNum != "0": # if the client has a phone number have a phone number
        msg = "\r\nHello " + j + ", you have an upcoming appointment with " + clientName + " on " + apptDate + ". Their needs are " + needs + ".\n"
        msg = msg + "The client's phone number is " + clientNum + " if more information is needed from the client.\n\n--Pathways Staff\nPathways Phone: (803) 366-PATH (7284)"
        endmsg = "\r\n.\r\n"

    elif clientNum == "0": # if the client does NOT have a phone number
        msg = "\r\nHello " + j + ", you have an upcoming appointment with " + clientName + " on " + apptDate + ". Their needs are " + needs + ".\n"
        msg = msg + "\n\n--Pathways Staff\nPathways Phone: (803) 366-PATH (7284)"
        endmsg = "\r\n.\r\n"

    # Gives user information (mostly testing purposes)
    print("\n" + "Email has been sent successfully. Associated information is below:" + "\n")
    print(df.iloc[-1])
    print(i, j)

    # Choose a mail server (e.g. Google mail server) and call it mailserver
    mailserver = ("list.winthrop.edu", 25)

    # Create socket called clientSocket and establish a TCP connection with mailserver
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)
    recv = clientSocket.recv(1024).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO list.winthrop.edu\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    heloCommand = 'HELO list.winthrop.edu\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()

    # Send MAIL FROM command and print server response.
    mailFrom = "MAIL FROM: pathwaystest@gmail.com\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    recv2 = recv2.decode()

    # Send RCPT TO command and print server response.
    rcptTo = "RCPT TO: " + i + "\r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    recv3 = recv3.decode()

    # Send DATA command and print server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    recv4 = recv4.decode()

    # Send message data.
    subject = "Subject: Upcoming Client Appointment.\r\n\r\n" 
    clientSocket.send(subject.encode())
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)

    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
    recv_endmsg = clientSocket.recv(1024)

    # Send QUIT command and get server response.
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv5 = clientSocket.recv(1024)
    clientSocket.close()
