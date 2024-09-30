import tkinter as tk
import os
from file_organizer import organize_files

# Create the main window
root = tk.Tk()
root.title("File Organizer")# 
root.geometry("400x250")  # Set the window sizeFunction to be called when the button is clicked

def submit_function():
    address = entry.get()  # Get text from the entry box 
    print("Address is :\t", address)#Label for entry
    if os.path.exists(address):
        organize_files(address)

label = tk.Label(root, text="Enter Directory Address:")
label.pack(pady=20)  # Add padding around the labelEntry (input block) where user can type text

entry = tk.Entry(root, width=30)
entry.pack(pady=5)#Button to trigger the function show_input


button = tk.Button(root, text="Submit", command=submit_function)
# command with arguments
# button = tk.Button(root, text="Submit", command=lambda inputArgs:function(inputArgs))
button.pack(pady=10)#Start the GUI event loop

root.mainloop()

