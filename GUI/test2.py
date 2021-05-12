import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from random import randrange
from threading import Thread
import socket

fig = plt.figure(facecolor='#2e2e2e')
ax1 = fig.add_subplot(111, projection='3d')

def udpReader():
    try:
        UDP_IP = "192.168.4.11" # IP address of base station
        UDP_PORT = 5005

        sock = socket.socket(socket.AF_INET, # Internet
                            socket.SOCK_DGRAM) # UDP
        sock.bind((UDP_IP, UDP_PORT))

        print("UDP start")
        while True:
            data, addr = sock.recvfrom(128)
            print("received message: %s" % data)
            file = open("incomingData.txt", "a")
            file.write(data.decode('utf-8') + '\n')
            file.close()
    except:
        print("Couldn't open socket")

def LastNlines(fname, N):
    assert N >= 0
    pos = N + 1
    lines = []
    with open(fname) as f:
        while len(lines) <= N:
            try:
                f.seek(-pos, 2)
            except IOError:
                f.seek(0)
                break
            finally:
                lines = list(f)
            pos *= 2
    return lines[-N:]

def animate(i):
    fname = "incomingData.txt"
    N = 20
    xar = []
    yar = []
    zar = []
    lines = LastNlines(fname,N)
    for line in lines:
        if len(line)>1:
            time,xstr,ystr,zstr = line.split(',')
            x = float(xstr)
            y = float(ystr)     
            z = float(zstr)
            xar.append(x)
            yar.append(y)
            zar.append(z)
    ax1.clear()
    ax1.scatter(xar, yar, zar, s=50, c='green')

    for x in range(0, len(xar)-1):
        ax1.plot3D([xar[x],xar[x+1]], [yar[x],yar[x+1]], [zar[x],zar[x+1]], linestyle='--', c='white')

def Main():
    t1=Thread(target=udpReader)
    t1.start()
    
    ani = animation.FuncAnimation(fig, animate, interval=1000)

    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Altitude')
    ax1.xaxis.label.set_color("white")
    ax1.yaxis.label.set_color("white")
    ax1.zaxis.label.set_color("white")
    ax1.tick_params(axis='x', colors='white')
    ax1.tick_params(axis='y', colors='white')
    ax1.tick_params(axis='z', colors='white')
    ax1.set_facecolor('#2e2e2e')

    plt.show()
    print("done")

Main()