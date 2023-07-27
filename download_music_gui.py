from tkinter import *
from youtube_music_downloader import download_video

link = None
entry = None  # Declare the entry widget as a global variable

def store_input(selected_folder_path,window):
    global link
    link = entry.get()  # Retrieve the input from the entry widget using .get()
    download_video(link,selected_folder_path)

def create_buttons(window,selected_folder_path):
    global entry  # Declare the entry widget as a global variable
    entry = Entry(window, font=('Jasper', 20), bg='white', fg='#a032a8')
    submit_button = Button(window, text='Submit', font=('Jasper', 20), bg='white', fg='#a032a8', command=lambda: store_input(selected_folder_path, window))
    submit_button.pack(side=RIGHT)
    entry.pack(side=RIGHT)
def download_window(selected_folder_path):
    download_screen = Toplevel()
    download_button_icon = PhotoImage(file='Projects_for_cv/Music_Player/images/download_button.png')
    download_screen.geometry('300x200')
    download_screen.title('Download video!')
    download_screen.iconphoto(True, download_button_icon)
    download_screen.config(background='#c69dc9')
    create_buttons(download_screen,selected_folder_path)
