import os
from tkinter import messagebox
from pytube import YouTube
import threading

def download_video(link, folder_path):
    try:
        yt = YouTube(link)
        music = yt.streams.filter(only_audio=True).first()
        filename = f"{yt.title}_audio.mp3"
        file_path = os.path.join(folder_path, filename)

        def download_and_notify():
            try:
                music.download(output_path=folder_path, filename=filename)
                messagebox.showinfo(message="Download complete!")
            except Exception as e:
                messagebox.showerror("Error", f"Download failed: {str(e)}")

        threading.Thread(target=download_and_notify).start()
        messagebox.showinfo(message='Downloading...')

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")