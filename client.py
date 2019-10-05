from socket import *
import time
serverName = 'localhost'
serverPort = 12000
print('connecting to: ',gethostname(),'...', sep="")
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('connection complete')
host = gethostname()
while True:
    number = input('input a number between 1-100 - anything else to exit: ')
    if int(number) < 1 or int(number) > 100 or int(number) == ValueError:
        break
    clientName = input('enter your name (leave blank for [blank]): ')
    if clientName=="":
        clientName='[blank]'
    sentence = 'Client '+ clientName +' of '+host+ ' sends the number '+ number +'!'
    print("Sending: ", sentence)

    clientSocket.send(sentence.encode()) #this part doesn't work again for some reason - solved. server loop issue. make it a double loop
    print("Waiting for server...")
    modifiedsentence = clientSocket.recv(1024) #receiver buffer
    print('From Server: ', modifiedsentence.decode())
clientSocket.close()
print('Goodbye coder! Exiting now...')
time.sleep(2)