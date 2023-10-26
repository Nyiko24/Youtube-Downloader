from logging import root
import tkinter as tk
from pytube import YouTube
import pytube
from tkinter import messagebox
from tkinter.ttk import Progressbar
import customtkinter
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import font
from moviepy.video.io.VideoFileClip import VideoFileClip
import requests
import re
import time
from io import BytesIO

#placeholder
def on_entry_focusin(event):
    if url_var.get() == "Enter URL":
        link.delete(0, tk.END)

def on_entry_focusout(event):
    if not url_var.get():
        link.insert(0, "Enter URL")


def download_video():
    try:
        # get the video URL
        video_url = link.get()

        # validate the input
        pattern = r"^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+"
        match = re.match(pattern, video_url)
        if video_url=="":
            messagebox.showinfo("Empty field","Please enter a link") 
            
        if match is not None and match.group(0) == video_url:
            print("Valid YouTube video_url")
            for i in range(10):
                progressBar.set(i / 100)
                app.update_idletasks()  # Forces the GUI to update
                time.sleep(0.05)  # Simulate some work
        else:
            print("Invalid YouTube video_url")
            raise ValueError("Invalid YouTube video_url")

        # create a YouTube object from the URL
        youtube = pytube.YouTube(video_url)
        for i in range(11,31):
            progressBar.set(i / 100)
            app.update_idletasks()  # Forces the GUI to update
            time.sleep(0.05)  # Simulate some work
        # get the highest quality video stream
        video_stream = youtube.streams.get_highest_resolution()
        for i in range(31,51):
            progressBar.set(i / 100)
            app.update_idletasks()  # Forces the GUI to update
            time.sleep(0.05)  # Simulate some work
        # download the video to a file
        #preview canvas
        video = YouTube(video_url)
        thumbnail_url = video.thumbnail_url.replace('hqdefault', 'maxresdefault')
        response = requests.get(thumbnail_url)
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        resized_image = image.resize((480, 270))
        photo = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.photo = photo
        canvas.pack()
        video_file = video_stream.download()
        for i in range(51,71):
            progressBar.set(i / 100)
            app.update_idletasks()  # Forces the GUI to update
            time.sleep(0.05)  # Simulate some work
        # update the progress bar
        for i in range(71,101):
            progressBar.set(i / 100)
            app.update_idletasks()  # Forces the GUI to update
            time.sleep(0.05)  # Simulate some work
        #label
        #label2 = tk.Label(root,text="Successful",font=('Arial',18))
        #label2.pack(padx=20, pady=20 )
        messagebox.showinfo("Success", "Video downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
#==========================================================================================================================
# define the function to extract audio from the YouTube video
def download_audio():
    try:
        # Get the YouTube video URL
        video_url = link.get()

        # Validate the input
        pattern = r"^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+"
        match = re.match(pattern, video_url)
        if match is not None and match.group(0) == video_url:
            print("Valid YouTube video_url")
            for i in range(10):
                progressBar.set(i / 100)
                app.update_idletasks()  # Forces the GUI to update
                time.sleep(0.05)  # Simulate some work
        else:
            print("Invalid YouTube video_url")
            raise ValueError("Invalid YouTube video_url")

        # Create a YouTube object from the URL
        youtube = pytube.YouTube(video_url)
        for i in range(11,31):
            progressBar.set(i / 100)
            app.update_idletasks()  # Forces the GUI to update
            time.sleep(0.05)  # Simulate some work
        # Get the highest quality video stream
        video_stream = youtube.streams.get_highest_resolution()
        for i in range(31,51):
            progressBar.set(i / 100)
            app.update_idletasks()  # Forces the GUI to update
            time.sleep(0.05)  # Simulate some work
        # Download the video to a file
        video_filename = video_stream.download()
        for i in range(51,61):
            progressBar.set(i / 100)
            app.update_idletasks()  # Forces the GUI to update
            time.sleep(0.05)  # Simulate some work
        # Create a VideoFileClip object from the video file
        video_clip = VideoFileClip(video_filename)
        for i in range(61,71):
            progressBar.set(i / 100)
            app.update_idletasks()  # Forces the GUI to update
            time.sleep(0.05)  # Simulate some work
        # Extract the audio from the video
        audio_clip = video_clip.audio
        for i in range(71,81):
            progressBar.set(i / 100)
            app.update_idletasks()  # Forces the GUI to update
            time.sleep(0.05)  # Simulate some work
        # Define the output audio file path
        output_audio_path = youtube.title + ".mp3"
        for i in range(81,91):
            progressBar.set(i / 100)
            app.update_idletasks()  # Forces the GUI to update
            time.sleep(0.05)  # Simulate some work
        # Write the audio to the output file
        audio_clip.write_audiofile(output_audio_path)
        for i in range(91,101):
            progressBar.set(i / 100)
            app.update_idletasks()  # Forces the GUI to update
            time.sleep(0.05)  # Simulate some work
        # Show success message
        messagebox.showinfo("Success", "Audio downloaded successfully.")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# System Settings
customtkinter.set_appearance_mode("System-")
customtkinter.set_default_color_theme("blue")



# App frame
app = customtkinter.CTk()
app.geometry("960x720")
app.title("YouTube Downloader")
# create the header frame
header_frame = tk.Frame(app)
header_frame.pack(side=tk.TOP, fill=tk.X)

# add the logo to the header and resize it
logo_image = Image.open('logoR.jpg')
logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(header_frame, image=logo_photo)
logo_label.pack(side=tk.LEFT)

# # add the text to the header
text_label = tk.Label(header_frame, text='Youtube Video & Audio Downloader', font=('Arial', 18,'bold'))
text_label.pack(side=tk.LEFT, padx=10)
# Adding ui elements
label = tk.Label(app, text="Positive Energy", bg='yellow')


# load the original YouTube image
youtube_image = Image.open("youtube.png")

# resize the YouTube image
resized_youtube_image = youtube_image.resize((200, 200))
#resized_youtube_image.pack(padx=10, pady=10)
# create a PhotoImage object from the resized YouTube image
youtube_img = ImageTk.PhotoImage(resized_youtube_image)

# create the label widget with the resized YouTube image
youtube_label = customtkinter.CTkLabel(app, image=youtube_img, anchor="w")
youtube_label.pack()
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)
# link input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.insert(0, "Enter URL")
link.bind("<FocusIn>", on_entry_focusin)
link.bind("<FocusOut>", on_entry_focusout)
link.pack(padx=10, pady=10)

# Finished Downloading
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack()




progressBar = customtkinter.CTkProgressBar(app, width=600)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)



# Download Button
download = customtkinter.CTkButton(app, text="Download video", command=download_video)
download.pack(padx=10, pady=10)

# Convert Button
convert = customtkinter.CTkButton(app, text="Download audio (mp3)", command=download_audio)
convert.pack(padx=10, pady=10)
canvas = tk.Canvas(app, width=480, height=270)
canvas.pack()
#footer
footer_frame = tk.Frame(app)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
footer = tk.Label(footer_frame, text='By Positive Energy', font=('Arial', 18,'bold'))
footer.pack(side=tk.LEFT, padx=10)
# Run app
app.mainloop()
