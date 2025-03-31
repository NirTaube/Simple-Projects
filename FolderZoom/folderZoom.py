import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os

def show_path(file_path):
    """ Show a messagebox with the full path of the file. """
    messagebox.showinfo("File Path", file_path)

def main():
    root = tk.Tk()
    root.title("Select a File")

    # Prompt user to select a directory
    directory = filedialog.askdirectory(parent=root, title='Choose a folder')
    if not directory:  # Exit if no directory is chosen
        return

    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:  # Notify if the directory is empty
        messagebox.showinfo("No Files", "No files found in the directory.")
        return

    # Create a button for each file
    for file in files:
        file_path = os.path.join(directory, file)
        btn = tk.Button(root, text=file, command=lambda f=file_path: show_path(f))
        btn.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
