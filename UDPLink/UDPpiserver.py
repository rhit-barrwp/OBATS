import socket

UDP_IP = "192.168.4.7"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)
 
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
while True:
    print("loopy boi")
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    
