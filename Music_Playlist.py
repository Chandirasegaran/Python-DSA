class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration} min)"

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        
import random

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_song(self, title):
        current = self.head
        prev = None
        while current and current.song.title != title:
            prev = current
            current = current.next
        if not current:
            print("Song not found.")
            return
        if prev:
            prev.next = current.next
        else:
            self.head = current.next

    def display_songs(self):
        current = self.head
        while current:
            print(current.song)
            current = current.next

    def play_songs(self):
        current = self.head
        while current:
            print(f"Playing: {current.song}")
            current = current.next

    def shuffle_play(self):
        current = self.head
        songs = []
        while current:
            songs.append(current.song)
            current = current.next
        random.shuffle(songs)
        for song in songs:
            print(f"Playing: {song}")
def main():
    playlist = Playlist()

    while True:
        print("\n1. Add Song")
        print("2. Delete Song")
        print("3. Display Songs")
        print("4. Play Songs")
        print("5. Shuffle Play")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter song title: ")
            artist = input("Enter song artist: ")
            duration = input("Enter song duration (in minutes): ")
            song = Song(title, artist, duration)
            playlist.add_song(song)
        elif choice == "2":
            title = input("Enter song title to delete: ")
            playlist.delete_song(title)
        elif choice == "3":
            playlist.display_songs()
        elif choice == "4":
            playlist.play_songs()
        elif choice == "5":
            playlist.shuffle_play()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
