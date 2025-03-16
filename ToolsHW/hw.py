import webbrowser, sys, time, random, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def input_math():
    user_input = input("1 times 1 = ? ")
    if user_input == 1: 
        open_video()

def open_video():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")

input_math()
