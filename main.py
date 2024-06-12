import tkinter
import customtkinter
from pytube import YouTube

def videoDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink , on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Video Download Complete")
    except:
        finishLabel.configure(text="Video Download Failed")


def audioDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink , on_progress_callback=on_progress)
        video = ytObject.streams.get_audio_only()
        title.configure(text=ytObject.title)
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Audio Download Complete")
    except:
        finishLabel.configure(text="Audio Download Failed")


def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_completed = bytes_downloaded / total_size * 100
    per = str(int(percent_completed))
    percent.configure(text=per + '%')
    percent.update()

    bar.set(float(percent_completed)/100)

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("520x280")
app.title("Simple Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Enter your YouTube link here.")
title.pack(padx=10 , pady=10)

# Input Link 
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app , width=350 , height=40, textvariable=url_var)
link.pack() 

# Finished Indicator
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress Bar
percent = customtkinter.CTkLabel(app, text="0%")
percent.pack()

bar = customtkinter.CTkProgressBar(app , width=400)
bar.set(0)
bar.pack(padx=10,pady=10)

# Download 
dl = customtkinter.CTkButton(app , text="Download Video" , command=videoDownload)
dl.pack(padx = 10 , pady = 10)
dl_a = customtkinter.CTkButton(app , text="Download Audio Only" , command=audioDownload)
dl_a.pack(padx = 10 , pady = 10)

# Run App
app.mainloop()