import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def sound_input():
    file_path = filedialog.askopenfilename(
        title="Select audio file",
        filetypes=[
            ("Audio files", "*.wav *.mp3 *.flac"),
            ("WAV files", "*.wav"),
            ("MP3 files", "*.mp3")
        ]
    )
    return file_path