###############################################################################
"""
Audmark main entry point

Description:
Contains the setup and control loop to play through an audio track while
receiving user input to mark instrument entries and exits in time.

Author:
Ian Hill
"""
################################################################################

import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

# noinspection PyCompatibility
import tkinter as tk
import vlc

class Audio():
    def __init__(self, media):
        self.audio = media
        self.name = 'some_name'
        self.is_playing = False

def run_and_mark_audio():
    # Load up audio file and new data entry
    track = Audio(vlc.MediaPlayer(r'C:\Users\IanHi\OneDrive - University of Waterloo\Music\Music\Live Snarky '
                                  '- November 22, 2019 - Paris, France -MP3\Snarky Puppy - LIVE SNARKY - November '
                                  '22, 2019 - Paris, France  - 08 - Chonks.mp3'))
    data_entry = {'name': track.name, 'piano': {'enters': [], 'exits': []}, 'guitar': []}
    print('Note: This program assumes a 1 second delay between audio and associated keypress, for example, if drums '
          'start playing, please aim to press "d" as close to 1 second later as possible.')

    def key_pressed(event):
        press_time = track.audio.get_time()
        if event.char == ' ':
            if not track.is_playing:
                track.is_playing = True
                track.audio.play()
                print(f"Now playing {track.name}.")
            else:
                track.is_playing = False
                track.audio.pause()
                print('Track paused.')
        elif event.char == 'p':
            if track.is_playing:
                data_entry['piano'].append(press_time - 1000)
                print('P key pressed...')
        else:
            pass

    root_window = tk.Tk()
    root_window.geometry('500x300')
    txt = tk.Text(root_window, background='black', foreground='white', font=('Comic Sans MS', 12))
    txt.pack()
    root_window.bind('<KeyPress>', key_pressed)
    root_window.mainloop()

    # TODO: Wait till end of tune to get length or find some other way of getting song length

    print(data_entry)


if __name__ == '__main__':
    run_and_mark_audio()
