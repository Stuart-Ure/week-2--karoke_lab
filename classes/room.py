class Room:

    def __init__ (self, name, capacity):
        self.name= name
        self.capacity = capacity
        self.songs = []
        self.guests= []


    def add_guest_to_room(self, guest):
        self.guests.append(guest)

    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)
