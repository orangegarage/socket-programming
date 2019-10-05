from socket import *
import time
import re
import random
serverName = 'localhost'
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
print('Hostname: ',gethostname())
hostName = gethostname()
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1) #number of connections
print ('Server',gethostname(),'online. awaiting connections...')
while True:
    connectionSocket, addr= serverSocket.accept() #called when client requests
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if not sentence:
            print('goodbye now!')
            time.sleep(2)
            break
        print("Received: ", sentence)
        searchName = re.search('Client (.*)of',sentence)
        clientName = searchName.group(1)
        searchNumber = re.search('the number (.*)!',sentence)
        clientNumber = searchNumber.group(1)
        randomNumber = random.randint(1,101)
        newNumber = int(clientNumber)+ int(randomNumber)
        print("Extracted clientName:", clientName)
        print("Extracted number:", clientNumber)
        print("new number:", newNumber)
        newsentence = "Host " + hostName + " sends back the sum " +str(newNumber) + " to client " + clientName + "!"
        connectionSocket.send(newsentence.encode())
    connectionSocket.close()