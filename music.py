import eyed3
from pprint import pprint
from glob import glob


class music:
    title = ""
    path = ""
    end_time = ""
    totaltime = ""
    author = ""
    img = ""

    def __init__(self, path):
        self.path = path
        song = eyed3.load(path)
        self.author = song.tag.artist
        self.title = song.tag.title
        self.end_time = self.duration_from_seconds(song.info.time_secs)
        self.totaltime = song.info.time_secs
        self.img = self.__genimg(song)

    def __genimg(self, song):
        r_index = str(self.path).rfind("\\")
        img_save_path = str(self.path[0:r_index])
        img_path = ""
        for image in song.tag.images:
            file_format = img_save_path + "{0} - {1}.jpg".format(self.author, song.tag.album, image.picture_type)
            img_path = file_format
            if file_format not in glob(img_save_path + "*.jpg"):
                image_file = open(file_format, "wb")
                image_file.write(image.image_data)
                image_file.close()
        return img_path

    @property
    def get_img(self):
        return self.img

    def total_time(self):
        return self.totaltime

    def get_endtime(self):
        return self.end_time

    def total_time_ms(self):
        return self.totaltime * 1000

    def duration_from_seconds(self, s):
        """Module to get the convert Seconds to a time like format."""
        s = s
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        # d, h = divmod(h, 24)
        timelapsed = "{:02d}:{:02d}".format(int(m), int(s))
        return timelapsed
