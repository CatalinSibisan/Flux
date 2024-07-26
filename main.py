import customtkinter
import os
# this app is a mp3 player app
# it's not done, yet


# system settings
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Flux")
app.config(bg="#111B36")
app.resizable(None, None)

# Important variables
text_pb = "►"
song_link = 'Rap'
song_names = os.listdir(song_link)

# fonts area
font_PB = customtkinter.CTkFont(family='Impact', size=40, weight='bold')
font_lable = customtkinter.CTkFont(family='Impact', size=20)
font_lable1 = customtkinter.CTkFont(family='Impact', size=15)

# frame for song list
songs_area = customtkinter.CTkScrollableFrame(app, width=200, height=480, fg_color='#1F3291', label_text="Rap", label_fg_color='#08186C',
                                               label_font=font_lable, scrollbar_button_color='#08186C',
                                               scrollbar_button_hover_color='#192879')
songs_area.pack(side=customtkinter.LEFT)

# show all the songs in the list
for i in range(len(song_names)):
    customtkinter.CTkButton(songs_area, hover_color='#192879',
                             text=song_names[i][:-4],
                               width=200, fg_color='transparent', anchor='w').pack(padx=2, pady=2)

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


song_duration = customtkinter.CTkLabel(buttons_area, text="0:00", font=font_lable1)
song_duration.place(x=465, y=1)

song_play_time = customtkinter.CTkLabel(buttons_area, text="0:00", font=font_lable1)
song_play_time.place(x=20, y=1)

# Start/pause button
play_button = customtkinter.CTkButton(buttons_area, font=font_PB, hover_color='#192879',
                                      text=text_pb, width=50, height=50, fg_color='#1F3291',
                                        corner_radius=100)
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
