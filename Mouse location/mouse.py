import tkinter as tk
import pyautogui

def update_mouse_position():
    x, y = pyautogui.position()
    position_str.set(f"X: {x}, Y: {y}")
    root.after(100, update_mouse_position)

root = tk.Tk()
root.title("Mouse Position Tracker")

position_str = tk.StringVar()
position_label = tk.Label(root, textvariable=position_str)
position_label.pack()

update_mouse_position()
root.mainloop()
