#IMPORT LIB
import tkinter as tk             #windows
from pytube import YouTube      #Youtube
from PIL import Image, ImageTk  #Image
import os                       #system


#define Function
# ------------------------------------------------------------------------------------
def download_video():
    url = urlInput.get()  # Get the url
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")  # This use the DOWLOADS folder of your computer

    try:                                                                  #Try and exept
        yt = YouTube(url)                                                   #Conect with the URL
        my_video = yt.streams.get_highest_resolution()                      #Take the highest resolution of the video
        title=my_video.title
        my_video.download(output_path=download_folder)                       #Dowload on the folder
        status_label.config(text=f"{title} downloaded successfully!")        #Message GREAT with the title
    except Exception as E:
        status_label.config(text="ERROR!!: " + str(E))                    #jumm a ERROR, chek

# ------------------------------------------------------------------------------------
# MAIN WINDOW
window = tk.Tk()
window.title("Youtube Download")

xWindow = 600   #width
yWindow = 400   #height

# Take width and height of the screen
x_screen = window.winfo_screenwidth()
y_screen = window.winfo_screenheight()

#calculate the position
x = (x_screen - xWindow) // 2
y = (y_screen - yWindow) // 2

# SIZE AND POSITION OF THE WINDOW
window.geometry(f"{xWindow}x{yWindow}+{x}+{y}")
# ------------------------------------------------------------------------------------
#IMAGE
image = Image.open("youtubeImage.png")  #The image on the folder
image = image.resize((200, 200))        #Ajust size

image = ImageTk.PhotoImage(image)       
image_label = tk.Label(window, image=image) #The image on the window
image_label.pack(pady=10)

# ------------------------------------------------------------------------------------
# TXT 
url_label = tk.Label(window, text="URL:",font=("Arial", 12)) # THE "Message GREAT"
url_label.pack()
urlInput = tk.Entry(window, width=60,font=("Arial", 12)) #Here you put your URL
urlInput.pack(pady=10)

# ------------------------------------------------------------------------------------
# BUTTON
#This button go to dowload_video()
boton_dowload = tk.Button(window, text="DOWNLOAD", command=download_video, height=2, width=20, bg="blue", fg="white", font=("Arial", 12))
boton_dowload.pack()

# ------------------------------------------------------------------------------------
#STATUS
status_label = tk.Label(window, text="", fg="green") # THE "Message GREAT"
status_label.pack()

#LOOP FOR THE WINDOWS
window.mainloop()
