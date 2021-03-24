import socket

UDP_IP = "192.168.4.7" # IP address of base station
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print("UDP start")
while True:
    data, addr = sock.recvfrom(128) # buffer size is 1024 bytes
    print("received message: %s" % data)
	
