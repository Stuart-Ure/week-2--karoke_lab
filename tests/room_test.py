import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):


    def setUp (self):
        self.song1 = Song ("Nosebleed Section", "Hilltop Hoods")
        self.song2 = Song ("All my life", " Foo Fighters")
        self.song3 = Song ("Blank Space", "Taylor Swift")

        self.room1 = Room ("NYC Room", 3)  #need to add person to the room in the setup before the remove function can work, need to add attendance.
        self.room2 = Room ("Leith room", 5) 

        self.guest1 = Guest ("Alfredo")
        self.guest2 = Guest ("Winston")
        self.guest3 = Guest ("Jesus")
    

    def test_room_has_name(self):
        self.assertEqual("NYC Room", self.room1.name)

    def test_room_capacity(self):
        self.assertEqual (5, self.room2.capacity)


    def test_add_guest_to_room(self):
        self.room2.add_guest_to_room(self.guest2)
        self.assertEqual(1, len(self.room2.guests))

    def test_remove_guest_from_room(self):
        self.room2.remove_guest_from_room(self.guest2)
        self.assertEqual(0,len(self.room2.guests))

    def test_add_song_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.assertEqual(1, len(self.room1.songs))
