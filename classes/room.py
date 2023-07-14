class Room:

    def __init__ (self, name, capacity, fee):
        self.name= name
        self.capacity = capacity
        self.fee=fee
        self.songs = []
        self.guests= []
        self.till = 0


    def add_guest_to_room(self, guest):
        self.guests.append(guest)

    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)

    # def remove_guest_from_room(self, guest):
    #     if guest in self.guests:
    #         self.guests.remove(guest)


    def add_song_to_room(self, song):
        self.songs.append(song)

    def add_to_till(self, amount):
        self.till += amount
