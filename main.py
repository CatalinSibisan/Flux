import customtkinter
import os
import pygame.mixer
from tkinter import filedialog
from mutagen.mp3 import MP3
from PIL import Image
import time
# this app is a mp3 player app


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
default_image = customtkinter.CTkImage(size=(510, 360), light_image=Image.open("defaultSongPhoto.png"),
                                       dark_image=Image.open("defaultSongPhoto.png"))
repeat_image = customtkinter.CTkImage(size=(24, 24), light_image=Image.open("repeat.png"),
                                       dark_image=Image.open("repeat.png"))
add_folder_image = customtkinter.CTkImage(size=(24, 24), light_image=Image.open("add.png"),
                                       dark_image=Image.open("add.png"))

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
        global song_names
        song_names = os.listdir(song_link)
        # make sure, the folder have mp3 files only
        for files in song_names:
            if files.endswith(".mp3"):
                # the lambda function help to get the button id and send to play_song function
                customtkinter.CTkButton(songs_area, hover_color='#192879',
                                        text=files[:-4], width=200, fg_color='transparent',
                                        anchor='w', command=lambda id_button=files: play_song(id_button)).pack(padx=1, pady=1)
            else:
                for widgets in songs_area.winfo_children():
                    widgets.destroy()
                customtkinter.CTkLabel(songs_area, text="Folder not contain .mp3 files!", text_color="red", font=font_lable1).pack(padx=2, pady=2)
    else:
        for widgets in songs_area.winfo_children():
            widgets.destroy()
        customtkinter.CTkLabel(songs_area, text="No folder found!", text_color="red", font=font_lable1).pack(padx=2, pady=2)


def play_song(id_button):
    # with this function, play the song. From global variable 'song_link' I get the song link and with 'id_button' I get the button I pressed
    # using pygame, the program can play any mp3 files
    global test
    test = id_button
    local_song_link = song_link
    playing_song = local_song_link + "/" + id_button
    pygame.mixer.init(frequency=50000)
    pygame.mixer.music.load(playing_song)
    pygame.mixer.music.play()
    play_button.configure(textvariable=text_pause, command=pause_song)
    play_button.update()
    repeat_button.configure(command=repeat, hover_color="#192879", fg_color='#1F3291')
    image_default.configure(text=id_button[:-4])
    progress_bar_active()

    # show how long is the song
    audio = MP3(playing_song)
    global length
    length = audio.info.length
    global minutes
    minutes = time.strftime('%M:%S', time.gmtime(length))
    song_duration.configure(text=minutes)
    song_duration.update()

    # set the slider max pos
    transform = int(length)
    progressBar.configure(to=transform)
    progressBar.set(0)
    song_play_time.configure(text="00:00")


# pause the song
def pause_song():
    pygame.mixer.music.pause()
    play_button.configure(textvariable=text_play, command=unpause_song)
    play_button.update()


# unpause the song
def unpause_song():
    pygame.mixer.music.unpause()
    play_button.configure(textvariable=text_pause, command=pause_song)
    play_button.update()
    

def progress_bar_active():
    if pygame.mixer.music.get_busy():
        global current_time
        current_time = int(pygame.mixer.music.get_pos()) / 1000
        converted_time = time.strftime('%M:%S', time.gmtime(current_time))
        song_play_time.configure(text=converted_time)
        song_play_time.update()
        progressBar.after(1000, progress_bar_active)
        progressBar.set(current_time)

    else:
        play_button.configure(textvariable = text_play, font=font_PB)
        song_play_time.configure(text=minutes)
        song_play_time.update()

# activate the song to repeat
def repeat():
    pygame.mixer.music.play(loops=-1)
    repeat_button.configure(command=unrepeat, hover_color="#1F3291", fg_color='#192879')

# dezactivate the song to repeat
def unrepeat():
    repeat_button.configure(command=repeat, hover_color="#192879", fg_color='#1F3291')
    pygame.mixer.music.play(loops=0)

# set the volume of the song
def volume(value):
    volume_value = int(value)
    volume_text.configure(text=volume_value)
    pygame.mixer.music.set_volume(value / 100)


# frame for song list
songs_area = customtkinter.CTkScrollableFrame(app, width=200, height=480, fg_color='#1F3291', label_text=lable_text, label_fg_color='#08186C',
                                               label_font=font_lable, scrollbar_button_color='#08186C',
                                               scrollbar_button_hover_color='#192879')
songs_area.pack(side=customtkinter.LEFT)

# buttons area 
buttons_area = customtkinter.CTkFrame(app, width=520, height=100, fg_color='#111B36')
buttons_area.pack(side=customtkinter.BOTTOM)

# song duration bar/text
progressBar = customtkinter.CTkSlider(buttons_area, width=390, from_=0, to=100,
                                      border_width=1, border_color="black", fg_color="#111B36",
                                      progress_color="#1F3291", button_color="#08186C", button_hover_color="#192879",
                                      state="disable")
progressBar.set(0)
progressBar.place(x=55, y=7)

# select the folder
folder_select = customtkinter.CTkButton(buttons_area, width=24, height=24, text="",image=add_folder_image, hover_color='#192879', fg_color='#1F3291', font=font_sett, command=folder_selection)
folder_select.place(x=30, y=50)

# song duration
song_duration = customtkinter.CTkLabel(buttons_area, text="00:00", font=font_lable1)
song_duration.place(x=450, y=1)

# song time
song_play_time = customtkinter.CTkLabel(buttons_area, text="00:00", font=font_lable1)
song_play_time.place(x=15, y=1)

# volume settings
volume_button = customtkinter.CTkSlider(buttons_area, from_=0, to=100, width=150, number_of_steps=100, fg_color="#111B36",
                                      progress_color="#1F3291", button_color="#08186C", button_hover_color="#192879", command=volume)
volume_button.set(100)
volume_button.place(x=320, y=50)
volume_text = customtkinter.CTkLabel(buttons_area, text="100", font=font_lable1)
volume_text.place(x=390, y=65)

# Start/pause button
play_button = customtkinter.CTkButton(buttons_area, font=font_PB, hover_color='#192879',
                                      textvariable=text_play, width=50, height=50, fg_color='#1F3291',
                                        corner_radius=100, command=pause_song)
play_button.place(x=150, y=27)

# repeat the song button
repeat_button = customtkinter.CTkButton(buttons_area, image=repeat_image, text="", hover_color="#192879", fg_color='#1F3291', width=30, height=30, corner_radius=100, command=repeat)
repeat_button.place(x=250, y=40)

# Image area
image_area = customtkinter.CTkFrame(app, width=510, height=360, bg_color="#111B36", fg_color='#1F3291', corner_radius=20)
image_area.pack(side=customtkinter.RIGHT, padx=10, pady=2)

image_default = customtkinter.CTkLabel(image_area, image=default_image, text="", font=font_lable)
image_default.pack()


app.mainloop()
