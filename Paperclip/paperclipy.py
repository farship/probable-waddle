from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt5.QtCore import pyqtSlot
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400,400,300,300)
    win.setWindowTitle("Paperclip")
    
    
    
    
    win.show()
    sys.exit(app.exec_())

#window()

class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()
    
    global numpaperclips
    numpaperclips = 0
    @pyqtSlot()
    def makePaperclip(self):
        
        #if numpaperclips == None:
        #    numpaperclips = 0
        numpaperclips =+ 1
        print (str(numpaperclips))
        #label1.setText('Paperclips: ' + str(numpaperclips))
    
    def UI(self):
        global label1
        label1 = QtWidgets.QLabel(self)
        #label1.setText('Paperclips: ' + str(numpaperclips))
        label1.adjustSize()
        label1.move(25,50)
        
        
        #topheaders1 = QPushButton('')
        topheaders2 = QPushButton('')
        topheaders3 = QPushButton('')
        topheaders4 = QPushButton('')
        sideheaders1 = QPushButton('')
        sideheaders2 = QPushButton('')
        sideheaders3 = QPushButton('')
        sideheaders4 = QPushButton('')

        Button1 = QPushButton('Up')
        Button1.clicked.connect(self.makePaperclip)
        #Button1.addAction(mmakePaperclip(1))
        Button2 = QPushButton('Left')
        Button3 = QPushButton('Right')
        Button4 = QPushButton('Down')
        

        grid = QGridLayout()

        #grid.addWidget(topheaders1, 0, 0)
        grid.addWidget(topheaders2, 0, 1)
        grid.addWidget(topheaders3, 0, 2)
        grid.addWidget(topheaders4, 0, 3)
        grid.addWidget(sideheaders1, 0, 0)
        grid.addWidget(sideheaders2, 1, 0)
        grid.addWidget(sideheaders3, 2, 0)
        grid.addWidget(sideheaders4, 3, 0)

        grid.addWidget(Button1, 0, 1)
        grid.addWidget(Button2, 1, 0)
        grid.addWidget(Button3, 1, 2)
        grid.addWidget(Button4, 1, 1)
 
        self.setLayout(grid)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('PyQt5 Layout')
        self.show()

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyQtLayout()
    sys.exit(app.exec_())