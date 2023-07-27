from tkinter import *
import os 
import vlc
def pause_music(player,unpause_button):
    player.pause()
    unpause_button['state'] = ACTIVE
def unpause_music(player,unpause_button):
    player.play()
    unpause_button['state'] = DISABLED
def music_controls(player):
    controls = Toplevel()
    controls_icon = PhotoImage(file='Projects_for_cv/Music_Player/images/play_button.png')
    controls.geometry('300x300')
    controls.title('Music Control!')
    controls.iconphoto(True, controls_icon)
    controls.config(background='#c69dc9')
    pause_button_logo = PhotoImage(file = '/Users/regiloshi/Documents/Projects/Projects_for_cv/Music_Player/images/pause_button.png')
    play_button_logo = PhotoImage(file='/Users/regiloshi/Documents/Projects/Projects_for_cv/Music_Player/images/play_button.png')
    unpauseButton = Button(controls, image=play_button_logo , state=DISABLED , command= lambda: unpause_music(player, unpauseButton))
    pauseButton = Button(controls, image = pause_button_logo , command= lambda: pause_music(player, unpauseButton))
    unpauseButton.image = play_button_logo
    pauseButton.image = pause_button_logo
    unpauseButton.pack(side=RIGHT)
    pauseButton.pack(side=LEFT)
def play_once(music_list,folder):
    music = music_list.get(music_list.curselection())
    full_music_file_path = f"{folder}/{music}"
    player = vlc.MediaPlayer(full_music_file_path)
    player.play()
    music_controls(player)
def play_order(music_list, folder, idx=0):
    music = music_list.get(idx)
    full_music_file_path = f"{folder}/{music}"
    def on_end_reached(event):
        play_order(music_list, folder, idx + 1)
    player = vlc.MediaPlayer(full_music_file_path)
    player.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached, on_end_reached)
    player.play()
    music_controls(player)
def createbuttons(music_library,folder,window):
    music_list = Listbox(window,
                        bg='white',
                        fg='black',
                        width=50)
    i = 0
    for music in music_library:
        music_list.insert(i , music)
        i+=1
    music_list.config(height=100)
    music_list.pack(side=LEFT)
    playButton = Button(window, text="Play", command=lambda: play_once(music_list,folder))
    playButton.pack(side=RIGHT)
    play_order_Button = Button(window, text="Play in order", command=lambda: play_order(music_list,folder))
    play_order_Button.pack(side=RIGHT)
def play_music_window(folder):
    controls = Toplevel()
    controls_icon = PhotoImage(file='Projects_for_cv/Music_Player/images/play_button.png')
    controls.geometry('600x400')
    controls.title('Play Music!')
    controls.iconphoto(True, controls_icon)
    controls.config(background='#c69dc9')
    music_library = []
    for filename in os.listdir(folder):
        if not os.path.exists(folder):
            print(f"Folder '{folder}' does not exist.")
            return
        if filename.endswith('.mp3'):
            music_library.append(filename)
    createbuttons(music_library,folder,controls)