class playlist:
    def __init__(self,name,genre):
        self.name = name 
        self.genre = genre 
        self.songs = []
        print(f"playlist '{self.name}' ({self.genre}) is ready!")
def add_song(self,songs):
    self.songs.append(songs)
    print(f" '{songs}' added to {self.name}.")

def remove_song(self, song):
    if song in self.songs:
        self.songs.remove(song)
        print(f" '{song}' removed.")
    else:
        print(f"'{song}' not found in playlist.")

def display(self):
    print(f"\n--- {self.name} ({self.genre})---")
    if self.songs:
        for i, song in enumerate(self.songs, 1):
            print(f" {i}. {song}")
    else:
        print(" no songs yet. add some!")

def __del__(self):
    print(f"playlist '{self.name}' has been deleted. goodbye!")

my_playlist = playlist("road trip mix", "pop")

while True:
    print("\n1. add song 2. remove song 3. view playlist 4.delete & quit")
    choice == input("enter your choice:")

    if Choice == "1":
        song = input("enter song name:")
        my_playlist.add_song(song)
    elif Choice == "2":
         song = input("enter song to remove:")
         my_playlist.remove_song(song)
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        del my_playlist 
        break
    else:
        print("invalid choice. enter 1,2,3, or 4.")             