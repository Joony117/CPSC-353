#import socket module
import socket
#rand for rng bytes
import random
#time to calculate RTT
import time

#making our UDP socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#our timeout value, this sets our timeout to 1 sec for the .recvfrom(1024) function in line 25
clientSocket.settimeout(1.0)
#this is our server/port we try to connect to, we use a tuple since .sendto((bytes,tuple)) expects (bytes,tuple)
server = ("localhost", 12000)


for sequence in range(1,11):
    try:
        startTime = time.time()
        #randomize bytes we;re sending
        sentPing = f"{random.randint(69,420)}"
        #send UDP ping to our server
        clientSocket.sendto(sentPing.encode(), server)
        
        #wait for reply
        message, address = clientSocket.recvfrom(1024)
        
        #our RTT
        rtt = time.time() - startTime
        
        print(f"Reply from our server: {address[0]} ,port #: {address[1]} ,Ping #: {sequence}, {message.decode()}, RTT = {rtt:.3f}s")
    except socket.timeout:
        print("timed out")
        
clientSocket.close()
