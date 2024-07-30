import customtkinter
import os
import pygame.mixer
from tkinter import filedialog

# this app is a mp3 player app
# it's not done, yet


# system settings
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Flux")
app.config(bg="#111B36")
app.resizable(False, False)

# Important variables
text_play = customtkinter.StringVar(value="►")
text_pause = customtkinter.StringVar(value="| |")
lable_text = "Songs"


# fonts area
font_PB = customtkinter.CTkFont(family='Impact', size=40, weight='bold')
font_sett = customtkinter.CTkFont(family='Impact', size=20, weight='bold')
font_lable = customtkinter.CTkFont(family='Impact', size=20)
font_lable1 = customtkinter.CTkFont(family='Impact', size=15)


# functions
def folder_selection():
    # here I make the link input area, for the folder with songs
    global song_link
    song_link = filedialog.askdirectory()
    is_folder = os.path.exists(song_link)

    # this condition runs if the folder exist
    if is_folder:
        lable_title = os.path.split(song_link)
        songs_area.configure(label_text=lable_title[1])
        songs_area.update()
        # with this for loop I delete all the items in the songs frame
        for widgets in songs_area.winfo_children():
            widgets.destroy()
        song_names = os.listdir(song_link)
        # show all the songs in the list
        for i in range(len(song_names)):
            # the lambda function help to get the button id and send to play_song function
            customtkinter.CTkButton(songs_area, hover_color='#192879',
                                                  text=song_names[i][:-4], width=200, fg_color='transparent',
                                                  anchor='w', command=lambda id_button=song_names[i]: play_song(id_button)).pack(padx=1, pady=1)
    else:
        for widgets in songs_area.winfo_children():
            widgets.destroy()
        customtkinter.CTkLabel(songs_area, text="No folder found!", text_color="red", font=font_lable1).pack(padx=2, pady=2)


def play_song(id_button):
    # with this function, play the song. From global variable 'song_link' I get the song link and with 'id_button' I get the button I pressed
    # using pygame, the program can play any mp3 files
    local_song_link = song_link
    playing_song = local_song_link + "/" + id_button
    pygame.mixer.init(frequency=50000)
    pygame.mixer.music.load(playing_song)
    pygame.mixer.music.play()
    pygame.mixer_music.queue(playing_song)
    play_button.configure(textvariable=text_pause, command=pause_song)
    play_button.update()


def pause_song():
    pygame.mixer.music.pause()
    play_button.configure(textvariable=text_play, command=unpause_song)
    play_button.update()


def unpause_song():
    pygame.mixer.music.unpause()
    play_button.configure(textvariable=text_pause, command=pause_song)
    play_button.update()


# frame for song list
songs_area = customtkinter.CTkScrollableFrame(app, width=200, height=480, fg_color='#1F3291', label_text=lable_text, label_fg_color='#08186C',
                                               label_font=font_lable, scrollbar_button_color='#08186C',
                                               scrollbar_button_hover_color='#192879')
songs_area.pack(side=customtkinter.LEFT)

# buttons area 
buttons_area = customtkinter.CTkFrame(app, width=520, height=100, fg_color='#111B36')
buttons_area.pack(side=customtkinter.BOTTOM)

# song duration bar/text
progressBar = customtkinter.CTkSlider(buttons_area, width=400, from_=0, to=100,
                                      border_width=1, border_color="black", fg_color="#111B36",
                                      progress_color="#1F3291", button_color="#08186C", button_hover_color="#192879",
                                      state="disable")
progressBar.set(0)
progressBar.place(x=55, y=7)

# select the folder
folder_select = customtkinter.CTkButton(buttons_area, width=30, height=30, text="☼", hover_color='#192879', fg_color='#1F3291', font=font_sett, command=folder_selection)
folder_select.place(x=30, y=50)

# song duration
song_duration = customtkinter.CTkLabel(buttons_area, text="0:00", font=font_lable1)
song_duration.place(x=465, y=1)

# song time
song_play_time = customtkinter.CTkLabel(buttons_area, text="0:00", font=font_lable1)
song_play_time.place(x=20, y=1)

# Start/pause button
play_button = customtkinter.CTkButton(buttons_area, font=font_PB, hover_color='#192879',
                                      textvariable=text_play, width=50, height=50, fg_color='#1F3291',
                                        corner_radius=100, command=pause_song)
play_button.place(x=220, y=27)

# Go to next song
next_button = customtkinter.CTkButton(buttons_area, font=font_PB, text="►", width=10, hover=False,
                                      text_color='#1F3291', fg_color='transparent')
next_button.place(x=310, y=25)

# Go to preview song
preview_button = customtkinter.CTkButton(buttons_area, font=font_PB, text="◄", width=10, hover=False,
                                         text_color='#1F3291', fg_color='transparent')
preview_button.place(x=160, y=25)

# Image area
image_area = customtkinter.CTkFrame(app, width=510, height=360, bg_color="#111B36", fg_color='#1F3291', corner_radius=20)
image_area.pack(side=customtkinter.RIGHT, padx=10, pady=2)


app.mainloop()
