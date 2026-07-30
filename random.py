import tkinter as tk

root = tk.Tk()
root.title("YOUR AN IDIOT")
root.attributes("-fullscreen", True)

text_area = tk.Text(root, bg="black", font=("Courier", 16))
text_area.pack(expand=True, fill="both")

text_area.tag_config("green_text", foreground="#00FF00")
text_area.tag_config("red_text", foreground="#FF0000")

is_green = True

def exit_program(event):
    root.destroy()



def update_text():
    global is_green
    
    current_tag = "green_text" if is_green else "red_text"
    
    text_area.insert(tk.END, "HACKED BY GENGA\n", current_tag)
    text_area.see(tk.END)
    
    is_green = not is_green
    root.after(150, update_text)

update_text()

root.mainloop()
