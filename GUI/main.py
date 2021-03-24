from  PyQt5.QtWidgets  import * 
from  PyQt5.uic  import  loadUi

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

import  numpy  as  np 
import  random
     
class  MatplotlibWidget ( QMainWindow ):
    
    def  __init__ ( self ):
        
        QMainWindow . __init__ ( self )

        loadUi ( "qt_designer.ui" , self )     

app  =  QApplication ([]) 
window  =  MatplotlibWidget () 
window . show () 
app . exec_ ()