from time import sleep
from PyQt5.QtCore import QThread, pyqtSignal
from pygame import mixer
from player_view import music_player


class ThreadTask(QThread):
    trigger = pyqtSignal(str)
    qthread_signal = pyqtSignal(int)
    stop_thread = False

    def __init__(self, mplayer):
        super().__init__()
        self.mp = mplayer

    def run(self):
        while mixer.music.get_busy():
            sec = (mixer.music.get_pos() // 1000) % 60
            min = (int(mixer.music.get_pos() // 1000 // 60)) % 60
            timelapsed = "{:02d}:{:02d}".format(int(min), int(sec))
            self.trigger.emit(timelapsed)
            process_value = int(mixer.music.get_pos() // 1000)
            print(process_value)
            self.qthread_signal.emit(process_value)
            sleep(1)
            if self.stop_thread:
                break

    def s_thread(self):
        self.stop_thread = True

    def r_thread(self):
        self.stop_thread = False
