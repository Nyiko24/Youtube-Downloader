# Youtube-Downloader
This is a python project where I've created a youtube video and audio downloader

This code is a Python script for a YouTube video and audio downloader using the tkinter library for the graphical user interface and the pytube library to interact with YouTube. Let's break down the code step by step in an easy-to-understand way:

1. Importing Libraries:
The code begins by importing several Python libraries, including tkinter (for the GUI), pytube (for interacting with YouTube), PIL (Python Imaging Library for image manipulation), moviepy (for working with video files), requests (for making HTTP requests), and others.

2. Placeholder Functions:
Two functions on_entry_focusin and on_entry_focusout are defined for managing the text entry field's behavior. They handle placeholder text when the user clicks in and out of the input field.

3. Download Video Function (download_video):
This function is called when the "Download video" button is clicked. It does the following:
Takes the YouTube video URL input from the user.
Validates the URL using a regular expression to ensure it's a valid YouTube URL.
Simulates a progress bar update for several steps.
Creates a YouTube object, gets the highest resolution video stream, and downloads the video.
Displays a preview image of the video using the video's thumbnail.
Updates the progress bar again.
Shows a success message or an error message using tkinter's messagebox.

4. Download Audio Function (download_audio):
This function is called when the "Download audio (mp3)" button is clicked. It does the following:
Similar to the download_video function, it validates the URL, simulates a progress bar, gets the video stream, downloads the video, and then extracts the audio from the downloaded video.
The audio is saved as an MP3 file with the video's title as the filename.
Updates the progress bar and shows success or error messages.

5. GUI Setup:
The code sets up a graphical user interface using tkinter with a title and a header displaying the logo and a text label.
It also creates an input field for the YouTube URL and two buttons for downloading video and audio.

6. Custom Styling:
Custom styling for the GUI is applied using the customtkinter library, including appearance mode and color themes.

8. Footer:
A footer is added with text indicating the author or source of the application.

8. Running the Application:
Finally, the application is run with app.mainloop().

9. This how the interface of the application looks like when you run it
¬
![YT1](https://github.com/Nyiko24/Youtube-Downloader/assets/114064061/f5291314-510d-4365-919b-594946aab895)

10. This gif shows that this application has error handling when you try to download without the link being inputted.¬
![PYEEE](https://github.com/Nyiko24/Youtube-Downloader/assets/114064061/6721f0eb-ec7b-4c1b-abb2-c6b4774f6159)

12. This GIF shows a demonstration of how the application is donwloading a drake laugh now cry later video from youtube via the progressbar.¬ 
![My Video11](https://github.com/Nyiko24/Youtube-Downloader/assets/114064061/cdca7b99-6940-4c9f-b32b-1028d2bfdc86)

    
