
'''
    Inteligência Artificial
    CEFET-MG
    27/0/2023
    
    A* labirinto
    Tarcísio Prates

'''



import os
import sys

import PyQt5
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from pages import home

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = home.Ui_Form()
ui.setupUi(Form)

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(
        QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(
        QtCore.Qt.AA_UseHighDpiPixmaps, True)


icon = QIcon('./images/logo.png')
Form.setWindowIcon(icon)
Form.setWindowTitle("A* Labirinto | Inteligência Artificial | CEFET-MG/2023 | " + str(os.getlogin()))

Form.show()
sys.exit(app.exec_())