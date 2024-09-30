from file_downloader import download_file as download
import tkinter as tk
from tkinter import messagebox

def button_call():
    url = url_entry.get()
    file_name = file_name_entry.get()
    if url and file_name:
        download(url, file_name)
        messagebox.showinfo("Info", f"Download initiated for: {file_name}")
    else:
        messagebox.showwarning("Input Error", "Please enter both URL and file name.")

# Setting up the Tkinter window
root = tk.Tk()
root.title("File Downloader")
root.geometry("500x200")

# URL Label and Entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Filename Label and Entry
file_name_label = tk.Label(root, text="Enter Filename (without extension):")
file_name_label.pack(pady=10)
file_name_entry = tk.Entry(root, width=50)
file_name_entry.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="Download", command=button_call)
download_button.pack(pady=20)

# Run the application
root.mainloop()
