from PyQt5.QtWidgets import*
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
    
class MplWidget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        fig = plt.figure(facecolor='#2e2e2e')

        self.canvas = FigureCanvas(fig)
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111, projection='3d')
        plt.tight_layout()

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
            self.canvas.axes.clear()
            fname = "data.txt"
            N = 3
            try:
                xar = []
                yar = []
                zar = []
                lines = LastNlines(fname,N)
                for line in lines:
                    x,y,z = line.split(',')
                    xar.append(float(x))
                    yar.append(float(y))
                    zar.append(float(z))
                self.canvas.axes.scatter(xar, yar, zar, s=50, c='white')
            except:
                print("File not found")

            # pullData = open("data.txt","r").read()
            # dataArray = pullData.split('\n')
            # xar = []
            # yar = []
            # zar = []
            # for eachLine in dataArray:
            #     if len(eachLine)>1:
            #         x,y,z = eachLine.split(',')
            #         xar.append(float(x))
            #         yar.append(float(y))
            #         zar.append(float(z))
            # self.canvas.axes.scatter(xar, yar, zar, s=50, c='white')

        ani = animation.FuncAnimation(fig, animate, interval=500)

        # x = [4.542239785,8.941687139,6.069811259,3.309678808,7.917407072]
        # y = [3.785100660,4.224900914,4.714002905,6.675400922,4.071284793]
        # z = [8.064804442,1.482040275,6.398090959,6.669711291,4.554042746]

        # x1 = [4.542239785,8.941687139,6.069811259,7.917407072]
        # y1 = [3.785100660,4.224900914,4.714002905,4.071284793]
        # z1 = [8.064804442,1.482040275,6.398090959,4.554042746]


        # self.canvas.axes.scatter(0, 0, 0, s=100, c='#A00000', marker='^')
        # self.canvas.axes.scatter(x1, y1, z1, s=50, c='white')
        # self.canvas.axes.plot3D([x[0],x[3]], [y[0],y[3]], [z[0],z[3]], linestyle='--', c='white')
        # self.canvas.axes.plot3D([x[0],x[2]], [y[0],y[2]], [z[0],z[2]], linestyle='--', c='white')
        # self.canvas.axes.plot3D([x[4],x[2]], [y[4],y[2]], [z[4],z[2]], linestyle='--', c='white')
        # self.canvas.axes.plot3D([x[4],x[1]], [y[4],y[1]], [z[4],z[1]], linestyle='--', c='white')
        # self.canvas.axes.scatter(x[3], y[3], z[3], s=60, c='green')

        # a = Arrow3D([0,3], [0,7], 
        #             [0,6], mutation_scale=10, 
        #             lw=2, arrowstyle="-|>", color="white")
        # self.canvas.axes.add_artist(a)
        # b = Arrow3D([x[3],x[3]], [y[3],y[3]], 
        #             [z[3]-1,z[3]+1], mutation_scale=2, 
        #             lw=1, arrowstyle="|-|", color="black")
        # self.canvas.axes.add_artist(b)
        # c = Arrow3D([x[3]+1,x[3]-1], [y[3],y[3]], 
        #             [z[3],z[3]], mutation_scale=2, 
        #             lw=1, arrowstyle="|-|", color="black")
        # self.canvas.axes.add_artist(c)
        # d = Arrow3D([x[3],x[3]], [y[3]+1,y[3]-1], 
        #             [z[3],z[3]], mutation_scale=2, 
        #             lw=1, arrowstyle="|-|", color="black")
        # self.canvas.axes.add_artist(d)

        self.canvas.axes.set_xlabel('X')
        self.canvas.axes.set_ylabel('Y')
        self.canvas.axes.set_zlabel('Altitude')
        self.canvas.axes.xaxis.label.set_color("white")
        self.canvas.axes.yaxis.label.set_color("white")
        self.canvas.axes.zaxis.label.set_color("white")
        self.canvas.axes.tick_params(axis='x', colors='white')
        self.canvas.axes.tick_params(axis='y', colors='white')
        self.canvas.axes.tick_params(axis='z', colors='white')

        self.setLayout(vertical_layout)

        self.canvas.axes.set_facecolor('#2e2e2e')

        plt.show()