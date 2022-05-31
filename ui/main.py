from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100,100,500,400)
    win.setWindowTitle("ARC Bot Manager")
    
    win.show()
    sys.exit(app.exec_())
window()