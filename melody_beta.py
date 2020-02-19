import requests
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from PyQt4.QtGui import QInputDialog, QLineEdit
from subprocess import Popen
import time
import smtplib
import webbrowser
from pynput.keyboard import Key, Controller

mel = "https://chaturbate.com/projektmelody/"
keyboard = Controller()
while True:
    url = requests.get(mel)

    if "Room is currently offline" in url.text:
        print("I miss melody....")
        time.sleep(60)
        continue
        
    if True:
        keyboard.press(Key.alt)
        keyboard.press(Key.f4)
        keyboard.release(Key.alt)
        keyboard.release(Key.alt)
        
        class Window(QtGui.QMainWindow):

            def __init__(self):
                super(Window, self).__init__()
                self.setGeometry(400, 125, 1000, 750)
                self.setWindowTitle("ProjektMelody")
                self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
          

                self.home()

            def home(self):
                btn = QtGui.QPushButton("Melody is Streaming!", self)
                btn.clicked.connect(self.close_application)
                btn.resize(btn.minimumSizeHint())
                btn.setGeometry(235,135 , 500, 450)

                extractAction = QtGui.QAction(QtGui.QIcon('Melody.png'), 'Flee the Scene', self)
                extractAction.triggered.connect(self.close_application)
                
         
                self.show()

            def close_application(self):
                choice = QtGui.QMessageBox.question(self, 'Waifu Alert',
                                                    "Watch Stream?",
                                                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                if choice == QtGui.QMessageBox.Yes:
                    webbrowser.open_new(mel)
                    sys.exit()
                else:
                    pass

            
        def run():
            app = QtGui.QApplication(sys.argv)
            GUI = Window()
            sys.exit(app.exec_())


        run()
        
        print("Stream time!")
        break
