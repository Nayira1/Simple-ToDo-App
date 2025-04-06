#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from PIL import Image, ImageTk  # This library handles images as Tkinter cannot

window = tk.Tk()
window.title("¸.·✩·.¸¸.·¯⍣✩ To-Do ✩⍣¯·.¸¸.·✩·.¸")
window.iconbitmap('E:/Projects/Simple_ToDo/why.ico')
bg_image = tk.PhotoImage(file="E:/stickers/pic.png")
image = Image.open(r"E:/stickers/pic.jpg")  # Or use forward slashes "E:/stickers/pic.jpg"
bg_image = ImageTk.PhotoImage(image)  # Convert the image for Tkinter
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # This ensures the image fills the entire window

# Keep a reference to the image object to prevent garbage collection
bg_label.image = bg_image  # This line prevents garbage collection
window.geometry("700x700") 
window.resizable(0,0)
todo_header = tk.Label(window, text="Ⲧⲟ-ꓓⲟ", font=("Arial", 24, "bold"), fg="plum", bg="white")
todo_header.place(relx=0.5, rely=0.2, anchor="center")

actionLabel = tk.Label(window, text="Please enter the task and click on the action you want ⋆ ˚｡⋆୨୧˚", font=("Georgia", 14, "bold"), fg="light pink", bg="white")
actionLabel.place(relx=0.5, rely=0.3, anchor="center")

entry = tk.Entry(window, font=("Georgia", 12), fg="hot pink", bg="light pink")
entry.place(relx=0.5, rely=0.4, anchor="center")

# Initialize task list
tasks = []

# Define functions before buttons
def add():
    global tasks
    new_task = entry.get()
    if new_task:
        tasks.append(new_task)
        entry.delete(0, tk.END)  # Clear the entry box after adding
        statusLabel.config(text="Your task has been added!")  # Update the status label
    else:
        statusLabel.config(text="Please enter a task to add.")  # If no input, show a message

def remove():
    global tasks
    removedTask = entry.get()
    entry.delete(0, tk.END)  # Clear the entry box after trying to remove
    if removedTask in tasks:
        tasks.remove(removedTask)
        statusLabel.config(text="Task has been removed.")
    else:
        statusLabel.config(text="Task not found. Please try again.")

def view():
    global tasks
    if tasks:
        # Convert tasks list into a string and show it in the label
        statusLabel.config(text="Your tasks are: " + ", ".join(tasks))
    else:
        statusLabel.config(text="Your list is empty.")

# Buttons for actions
addButton = tk.Button(window, text="Add", font=("Georgia", 12, "bold"), fg="hot pink", bg="light pink", command=add)
removeButton = tk.Button(window, text="Remove", font=("Georgia", 12, "bold"), fg="hot pink", bg="light pink", command=remove)
viewButton = tk.Button(window, text="View", font=("Georgia", 12, "bold"), fg="hot pink", bg="light pink", command=view)
endButton = tk.Button(window, text="End", font=("Georgia", 12, "bold"), fg="hot pink", bg="light pink", command=window.quit)

# Place buttons
addButton.place(relx=0.5, rely=0.5, anchor="center")
removeButton.place(relx=0.5, rely=0.6, anchor="center")
viewButton.place(relx=0.5, rely=0.7, anchor="center")
endButton.place(relx=0.5, rely=0.8, anchor="center")

# Label to display task status
statusLabel = tk.Label(window, text="", font=("Georgia", 12, "bold"), fg="purple", bg="white")
statusLabel.place(relx=0.5, rely=0.9, anchor="center")

window.mainloop()


# In[ ]:





# In[ ]:




