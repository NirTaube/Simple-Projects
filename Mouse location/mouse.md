# Mouse Position Tracker

## Overview
The Mouse Position Tracker is a Python script that displays a small window showing the current coordinates of your mouse cursor in real-time. It uses `Tkinter` for the graphical user interface and `pyautogui` for tracking the mouse position.

## Features
- **Real-Time Tracking**: Updates the mouse coordinates in real-time.
- **Simple GUI**: A minimalistic window that shows the current X and Y coordinates of the mouse.

## Requirements
- Python 3.x
- `Tkinter` (usually comes with Python)
- `pyautogui` library

## Installation
To run this script, you need to install the `pyautogui` library. If it's not already installed, you can install it using pip:

## Usage
1. **Run the Script**: Execute the script in your Python environment.
2. **View Mouse Coordinates**: Move your mouse around and watch the coordinates update in real-time.

## Code Explanation
- The script creates a basic Tkinter window.
- It then continuously fetches the mouse position using `pyautogui.position()` and updates the label in the Tkinter window.
- The window updates every 100 milliseconds to reflect the current position of the mouse.
