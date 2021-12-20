import os
import random

# music_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# print(music_dir)
# songs = os.listdir("Music")
# for song in songs:
#     print(song, end="\n")
# play_random = random.randint(0, (len(music_dir) - 1))
# os.startfile(os.path.join(music_dir, songs[play_random]))


# files=os.listdir(music_dir)
# d=random.choice(files)
# os.startfile(d)
music_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
songs = os.listdir("Music")

def play_music():
    play_random = random.randint(0, (len(music_dir) - 1))
    os.startfile(os.path.join(music_dir, songs[play_random]))

def print_music_available():
    for song in songs:
        print(song, end="\n")


# play_music()
# print_music_available()