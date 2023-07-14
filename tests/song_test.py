import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):
    


    def setUp (self):
        self.song1 = Song ("Nosebleed Section", "Hilltop Hoods")
        self.song2 = Song ("All my life", " Foo Fighters")
        self.song3 = Song ("Blank Space", "Taylor Swift")

        self.guest1 = Guest ("Alfredo")
        self.guest2 = Guest ("Winston")
        self.guest3 = Guest ("Jesus")

    def test_song_has_title(self):
        self.assertEqual("Nosebleed Section", self.song1.title)

    def test_song_has_artist(self):
        self.song2 = Song("All my life", "Foo Fighters")
        self.assertEqual("Foo Fighters", self.song2.artist)
