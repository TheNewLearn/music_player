from time import sleep
from PyQt5.QtCore import QThread, pyqtSignal
from pygame import mixer

class Music_handler(QThread):
    finished = pyqtSignal(str)

    def __init__(self,mp):
        super(Music_handler, self).__init__()
        self.mp = mp
        self.isplaying = False

    def run(self):
        while True:
            print("running")
            if not mixer.music.get_busy() and not self.mp.ispaued and self.isplaying:
                self.finished.emit("Finished")

            sleep(1)

    def playing(self):
        self.isplaying = True

    def Stop_play(self):
        self.isplaying = False