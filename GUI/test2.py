import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from random import randrange
from threading import Thread

fig = plt.figure(facecolor='#2e2e2e')
ax1 = fig.add_subplot(111, projection='3d')

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
    fname = "../UDPLink/incomingData.txt"
    N = 5
    xar = []
    yar = []
    zar = []
    lines = LastNlines(fname,N)
    for line in lines:
        if len(line)>1:
            time,x,y,z = line.split(',')
            xar.append(float(x))
            yar.append(float(y))
            zar.append(float(z))
    print(xar)
    ax1.clear()
    ax1.scatter(xar, yar, zar, s=50, c='green')
    for x in range(0, N-1):
        ax1.plot3D([xar[x],xar[x+1]], [yar[x],yar[x+1]], [zar[x],zar[x+1]], linestyle='--', c='white')

def Main():
    # t1=Thread(target=FileWriter)
    # t1.start()
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