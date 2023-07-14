import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):



    def setUp (self):
        self.song1 = Song ("Nosebleed Section", "Hilltop Hoods")
        self.song2 = Song ("All my life", " Foo Fighters")
        self.song3 = Song ("Blank Space", "Taylor Swift")

        self.room1 = Room ("NYC_Room", 3)
        self.room2 = Room ("Leith_room", 5)

        self.guest1 = Guest ("Alfredo")
        self.guest2 = Guest ("Winston")
        self.guest3 = Guest ("Jesus")