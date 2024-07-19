import tkinter
import customtkinter
# this app is an mp3 player app
# it's not done, yet

# system settings
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Flux")
app.config(bg="#111B36")
app.resizable(0, 0)

# fonts area
font_PB = customtkinter.CTkFont(family='Impact', size = 40, weight = 'bold')

# frame for song list
songs_area = customtkinter.CTkFrame(app, width=200, height=480, fg_color=('#1F3291'))
songs_area.pack(side = customtkinter.LEFT)

# show all the songs in the list
for i in range(16):
    label1 = customtkinter.CTkButton(songs_area, hover_color=('#192879'), text=f"{i + 1}| Nume piesa                      timp", width= 200, fg_color = 'transparent')
    label1.place(x=1, y=i * 30)

# buttons area 
buttons_area = customtkinter.CTkFrame(app, width=520, height=100, fg_color=('#111B36'))
buttons_area.pack(side = customtkinter.BOTTOM)

# Start/pause button
play_button = customtkinter.CTkButton(buttons_area, font=font_PB, hover_color=('#192879'), text = "| |", width= 70, height= 70, fg_color=('#1F3291'), corner_radius= 100)
play_button.place(x=220 , y=15)


app.mainloop()