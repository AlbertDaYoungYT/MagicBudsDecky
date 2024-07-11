import socket	
import logging		 

s = socket.socket()
port = 2020			

s.bind(('0.0.0.0', port))

# put the socket into listening mode 
s.listen(5)	 
print ("socket is listening")		 

# a forever loop until we interrupt it or 
# an error occurs 
while True: 

    c, addr = s.accept()
    print("connected")

    c.send('Thank you for connecting'.encode()) 



c.close()
