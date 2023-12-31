import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):


    def setUp (self):
        self.song1 = Song ("Nosebleed Section", "Hilltop Hoods")
        self.song2 = Song ("All my life", " Foo Fighters")
        self.song3 = Song ("Blank Space", "Taylor Swift")

        self.songs = [self.song1, self.song2, self.song3]
    
        self.room1 = Room ("NYC Room", 3, 10)  #need to add person to the room in the setup before the remove function can work, need to add attendance.
        self.room2 = Room ("Leith room", 5, 5) 

        self.rooms = [self.room1, self.room2]

        self.guest1 = Guest ("Alfredo")
        self.guest2 = Guest ("Winston")
        self.guest3 = Guest ("Jesus")

        self.guests= [self.guest1, self.guest2, self.guest3]

        self.guest4= Guest ("Brad")
    

    def test_room_has_name(self):
        self.assertEqual("NYC Room", self.room1.name)

    def test_room_capacity(self):
        self.assertEqual (5, self.room2.capacity)
        self.assertEqual ( 3 ,self.room1.capacity)


    def test_add_guest_to_room(self):
        self.room2.add_guest_to_room(self.guest1)
        self.assertEqual(1, len(self.room2.guests))


    def test_remove_guest_from_room(self):
        self.room2.add_guest_to_room(self.guest2)
        self.room2.remove_guest_from_room(self.guest2)
        self.assertEqual(0,len(self.room2.guests))

    def test_add_song_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.assertEqual(1, len(self.room1.songs))

    def test_room_till_starts_empty(self):
        self.assertEqual(0, self.room2.till)

    def test_can_add_to_till(self):
        self.room2.till = 10
        self.assertEqual(10, self.room2.till)


    