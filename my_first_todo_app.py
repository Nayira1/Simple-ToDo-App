#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(action):
    global tasks
    new_task = input("Please enter your new task")
    tasks.append(new_task)
    print ("Your task has been added ˗ˏˋ ★ ˎˊ˗")
    return(checking())

def remove(action):
    global tasks
    while True:
        removedTask = input("What task do you want to remove (Please enter the exact same task): ")
        if removedTask in tasks:
            tasks.remove(removedTask)
            print("The task has been removed!!")
            break  
        else:
            print("Task not found. Please try again.")
    return(checking())

def view(action):
    global tasks
    if tasks:
        print("Your tasks are",tasks)
    else:
        print("Your list is empty")
            
def checking():   
    while True:
        check = input("Please choose an option : \n 1- Add a task\n 2- Remove a task \n 3- View\n 4- End\n").strip()
        if check == "1":
            add(check)
        elif check == "2":
            remove(check)
        elif check == "3":
           view(check)
        elif check == "4":
           print("ミ💖 Thanks for using our To-Do list, have a great day 💖彡")
           break
        else :
            print("!!ERROR!! ICORRECT INPUT, PLEASE TRY AGAIN")
        


# In[ ]:


print("𝒴ℴ𝓊𝓇 𝓉ℴ 𝒹ℴ 𝓁𝒾𝓈𝓉 𝓅𝓎𝓉𝒽ℴ𝓃 𝒶𝓅𝓅\n")
tasks = []
checking()


# In[3]:


import tkinter as tk
from PIL import Image, ImageTk #This libary handles images cu tikenter cannot
window  = tk.Tk()
window.title("¸.·✩·.¸¸.·¯⍣✩ To-Do ✩⍣¯·.¸¸.·✩·.¸")

bg_image = tk.PhotoImage(file="E:/stickers/pic.png")
image = Image.open(r"E:/stickers/pic.jpg")  # Or use forward slashes "E:/stickers/pic.jpg"
bg_image = ImageTk.PhotoImage(image)  # Convert the image for Tkinter
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)  # This ensures the image fills the entire window

# Keep a reference to the image object to prevent garbage collection
bg_label.image = bg_image  # This line preven
todo_header = tk.Label(window, text="Ⲧⲟ-ꓓⲟ", font = ("Arial", 24, "bold"), fg="plum", bg="white")
todo_header.place(relx=0.5, rely=0.5, anchor="center")



window.mainloop()#To window



# In[1]:





# In[ ]:


'''def checking():   
    while True:
        check = input("Please choose an option : \n 1- Add a task\n 2- Remove a task \n 3- View\n 4- End\n").strip()
        if check == "1":
            add(check)
        elif check == "2":
            remove(check)
        elif check == "3":
           view(check)
        elif check == "4":
           print("ミ💖 Thanks for using our To-Do list, have a great day 💖彡")
           break
        else :
            print("!!ERROR!! ICORRECT INPUT, PLEASE TRY AGAIN")'''

