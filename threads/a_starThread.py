
import time

from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from threading import Thread

from Scripts import a_star
from Utils import broadcast


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)


    def setParams(self, begin, end):

        self.begin = begin
        self.end = end

    def run(self):

        self.application = a_star.AStar_script()


        self.app = Thread(target=self.application.calculateA, args=(self.begin, self.end, ))
        self.app.start()

        while (self.app.is_alive()):
            time.sleep(1)
            self.progress.emit(1)

        self.finished.emit()


class AStar(QMainWindow):

    broadcast = broadcast.Broadcast()

    def acabou(self):
        self.endApp()

    def runUpdate(self):

        '''try:
            data = self.broadcast.bottonBarInfo()
        except:
            data = "Connecting to service..."

        text = '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#5B738B3D;">' + str(data) + '</span></p></body></html>'
        self.labelInfo.setText(text)'''

        None



    def run(self, begin, end, beginApp, endApp):
        # Step 2: Create a QThread object
        self.thread = QThread()

        self.beginApp = beginApp
        self.endApp = endApp
        #self.labelInfo = labelInfo

        # Step 3: Create a worker object
        self.worker = Worker()
        self.worker.setParams(begin, end)
        # Step 4: Move worker to the threads
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.runUpdate)

        # Step 6: Start the threads
        self.beginApp()
        self.thread.start()

        self.thread.finished.connect(self.acabou)




