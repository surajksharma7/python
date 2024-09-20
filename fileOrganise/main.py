import tkinter as tk
import os
from file_organizer import organize_file 

def submit_function():
    address = entry.get()
    print("address is at",address)
    if os.path.exist(address):
        organize_files(addres)

root = tk.Tk()
root.title("Simple Input and Output GUI")
root.geometry("300x200")

# Label for instructions
label = tk.Label(root, text="Enter value:")
label.pack(pady=10)

# Entry widget for user input
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button to submit the input
button = tk.Button(root, text='Submit', command=show_input)
button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="User Input will appear here")
result_label.pack(pady=10)

root.mainloop()


# import tkinter as tk
# import os
# from file_organizer import organize_file

# def submit_function():
#     address = entry.get()
#     print("Address is at", address)
#     if os.path.exists(address):
#         organize_file(address)
#         result_label.config(text="File organized successfully!")
#     else:
#         result_label.config(text="File does not exist.")

# root = tk.Tk()
# root.title("Simple Input and Output GUI")
# root.geometry("300x200")

# # Label for instructions
# label = tk.Label(root, text="Enter file path:")
# label.pack(pady=10)

# # Entry widget for user input
# entry = tk.Entry(root, width=30)
# entry.pack(pady=5)

# # Button to submit the input
# button = tk.Button(root, text='Submit', command=submit_function)
# button.pack(pady=10)

# # Label to display the result
# result_label = tk.Label(root, text="Result will appear here")
# result_label.pack(pady=10)

# root.mainloop()
