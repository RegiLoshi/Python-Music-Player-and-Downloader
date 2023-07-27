from tkinter import *
from download_music_gui import download_window
from play_music_gui import play_music_window
from tkinter import filedialog

selected_folder_path = None

def select_folder():
    global selected_folder_path
    folder = filedialog.askdirectory()
    selected_folder_path = folder
    play_music_button['state'] = ACTIVE
    play_music_button['bg'] = 'white'
    play_music_button['fg'] = '#a032a8'
    download_music_button['state'] = ACTIVE
    download_music_button['bg'] = 'white'
    download_music_button['fg'] = '#a032a8'
def start_menu_buttons(window):
    play_button_logo = PhotoImage(file='/Users/regiloshi/Documents/Projects/Projects_for_cv/Music_Player/images/play_button.png')
    download_button_logo = PhotoImage(file='Projects_for_cv/Music_Player/images/download_button.png')
    select_folder_logo= PhotoImage(file='Projects_for_cv/Music_Player/images/select_folder.png')
    global download_music_button
    global play_music_button
    download_music_button = Button(window, 
                                  text='Download Music',
                                  font=('Jasper', 50),
                                  bg='white',
                                  fg='#a032a8',
                                  command=lambda:download_window (selected_folder_path),
                                  image = download_button_logo,
                                  compound = 'left',
                                  state=DISABLED)
    play_music_button = Button(window, 
                               text='Play Music',
                               font=('Jasper', 50),
                               bg='white',
                               fg='#a032a8',
                               command=lambda: play_music_window(selected_folder_path),
                               image = play_button_logo,
                               compound = 'left',
                               state=DISABLED)
    select_folder_button = Button(window, 
                               text='Select Folder',
                               font=('Jasper', 50),
                               bg='white',
                               fg='#a032a8',
                               command=select_folder,
                               image = select_folder_logo,
                               compound = 'left')
    select_folder_button.image = select_folder_logo
    play_music_button.image = play_button_logo
    download_music_button.image = download_button_logo
    download_music_button.pack(side=BOTTOM)
    play_music_button.pack(side=BOTTOM)
    select_folder_button.pack(side=BOTTOM)
def create_window():
    window = Tk()
    window.geometry('500x400')
    window.title('Music Player')
    logo = PhotoImage(file='Projects_for_cv/Music_Player/images/music_logo.png')
    window.iconphoto(True,logo)
    window.config(background='#6f8ac9')
    welcome_logo = PhotoImage(file='Projects_for_cv/Music_Player/images/welcome.png')
    welcome_label = Label(window, image=welcome_logo , bg = '#6f8ac9' )
    welcome_label.pack(side=TOP, pady=10)
    start_menu_buttons(window)
    window.mainloop()
if __name__ == '__main__':
    create_window() 