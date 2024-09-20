import tkinter as tk

def show_input():
    user_input = entry.get()
    result_label.config(text=f"User Input: {user_input}")

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
