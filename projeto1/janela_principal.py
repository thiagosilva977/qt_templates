import time
from threading import Thread

from projeto1.form import Ui_MainWindow

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
import multiprocessing as mp
from PySide2 import QtCore
from PySide2.QtCore import Qt
import PySide2.QtWidgets as QtWidgets


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

        def saudacao():
            print("ola mundo")

        def saudacao2():
            print("funcao2")

        def loading_connectdb():
            thread = Thread(target=connectdb, daemon=True)
            thread.start()

        def connectdb ():
            progressnumber = 0
            for i in range(100):
                print("Connecting . . .")
                self.progresso.setValue(progressnumber)
                time.sleep(0.1)
                progressnumber = progressnumber+1

        def timing():
            progressnumber = 0
            for i in range(100):
                print("Connecting . . ."+str(progressnumber))
                time.sleep(0.1)
                progressnumber = progressnumber + 1



        self.button_checkdb.clicked.connect(loading_connectdb)
        #self.botao2.clicked.connect(saudacao2)





if __name__ == "__main__":
    print("inicializando")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    print("finalizado")
