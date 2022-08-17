from pygame import mixer
from glob import glob
from music import music


class music_player:
    path = "C:/Users/fung/Desktop/music/*/*/*.mp3"
    music = []
    current_play = ""
    playtime = ""
    ispaued = False
    current_index = 0
    current_playing = ""
    finished = True

    def __init__(self):
        mixer.init()
        self.music = [music(x) for x in self.gensong()]
        self.current_playing = self.playlist()[0].path

    def setcurrentplaying(self, filename):
        self.current_playing = filename
        self.__findindex()

    def currentmusic(self):
        return self.music[self.current_index]

    def __findindex(self, filename):
        if filename in self.playlist():
            for index in range(0, len(self.playlist())):
                if filename == self.playlist()[index]:
                    self.current_index = index

    def gensong(self):
        a = glob(self.path, recursive=False)
        return a

    def totaltime(self, index):
        return self.music[index].total_time()

    def playlist(self):
        return self.music

    def duration_from_seconds(self, s):
        """Module to get the convert Seconds to a time like format."""
        s = s
        m, s = divmod(s, 1000)
        h, m = divmod(m, 60)
        # d, h = divmod(h, 24)
        timelapsed = "{:02d}:{:02d}".format(int(m), int(s))
        return timelapsed

    def playtime(self):
        return self.music[self.current_index].end_time

    def pause(self):
        mixer.music.pause()
        self.ispaued = True

    def unpause(self):
        mixer.music.unpause()
        self.ispaued = False

    def getname(self):
        return self.playlist()[self.current_index].author

    def getimgurl(self):
        return self.playlist()[self.current_index].img

    def gettitle(self):
        return self.playlist()[self.current_index].title

    def getsec(self, index):
        sec = self.totaltime(index) % 60
        return int(sec)

    def getmin(self, index):
        min = self.totaltime(index) // 60
        return int(min)

    def test(self):
        return mixer.music.get_pos()

    def play_song(self, index):
        if not mixer.music.get_busy() and not self.ispaued:
            self.current_index = index
            mixer.music.load(self.playlist()[index].path)
            mixer.music.play()
        else:
            mixer.music.unpause()
            self.ispaued = False

    def play_song(self):
        if self.current_index == 0:
            mixer.music.load(self.playlist()[0].path)
            mixer.music.play()
        if not mixer.music.get_busy() and not self.ispaued:
            self.next()
        elif self.ispaued:
            mixer.music.pause()




    def next(self):
        if self.current_index < len(self.playlist())-1:
            mixer.music.stop()
            self.current_index+=1
            mixer.music.load(self.playlist()[self.current_index].path)
            mixer.music.play()

    def pre(self):
        if self.current_index > 0:
            mixer.music.stop()
            self.current_index -= 1
            mixer.music.load(self.playlist()[self.current_index].path)
            mixer.music.play()

    def setvolum(self, num):
        if num < 1:
            mixer.music.set_volume(num)
