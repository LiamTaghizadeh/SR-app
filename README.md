#Screen Recorder Application

## Overview
This project implements a basic screen recording application with a graphical user interface (GUI) using Python's `tkinter`. The application allows users to start and stop recording their screen, capturing frames at a specified frame rate, and saving the recorded video to a file.

---

## Features
- **Start/Stop Recording**: A button toggles between starting and stopping the screen recording.
- **Screen Capture**: Continuously captures screenshots of the entire screen.
- **Video Saving**: Saves the captured frames into an AVI video file using the XVID codec.
- **Simple GUI**: Basic interface with a button indicating recording status and a minimal canvas.

---

## Dependencies
- `tkinter`: Standard Python library for GUI applications.
- `pyautogui`: For capturing screenshots.
- `opencv-python` (`cv2`): For saving video files.
- `numpy`: For image array manipulation.
- `time`: To manage frame rate.

---

## Setup Instructions
1. **Install Required Libraries**
   ```bash
   pip install pyautogui opencv-python numpy
   ```
2. **Run the Script**
   Save the script to a `.py` file and execute:
   ```bash
   python your_script_name.py
   ```

---

## Code Breakdown

### Import Statements
```python
import tkinter as tk
import time
import pyautogui
import cv2
import numpy as np
```
- Imports necessary modules for GUI, timing, screen capture, video processing, and array manipulation.

### `ScreenRecorder` Class
#### Initialization (`__init__`)
```python
def __init__(self, master):
    self.master = master
    master.title("Screen Recorder")
    
    # Recording state
    self.recording = False
    
    # Output filename
    self.filename = "my_video.avi"
    
    # Screen size (adjust as needed)
    self.screen_size = (1920, 1080)
    
    # Frames per second
    self.fps = 30.0
    
    # GUI Elements
    self.canvas = tk.Canvas(master, width=200, height=50)
    self.canvas.pack()
    
    self.button = tk.Button(master, text="Record", command=self.toggle_recording)
    self.button.pack()
```
- Sets up the main window, initializes variables, and creates GUI components.

#### Toggle Recording (`toggle_recording`)
```python
def toggle_recording(self):
    if not self.recording:
        self.recording = True
        self.button.config(text="Stop")
        self.start_recording()
    else:
        self.recording = False
        self.button.config(text="Record")
```
- Starts or stops recording based on current state.
- Calls `start_recording()` when starting.

#### Start Recording (`start_recording`)
```python
def start_recording(self):
    out = cv2.VideoWriter(self.filename, cv2.VideoWriter_fourcc(*"XVID"), self.fps, self.screen_size)
    while self.recording:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        time.sleep(1 / self.fps)
    out.release()
```
- Opens a video writer object.
- Continuously captures screenshots, converts them to proper format, and writes frames to the video file.
- Runs until `self.recording` becomes `False`.

### Main Application Loop
```python
root = tk.Tk()
app = ScreenRecorder(root)
root.mainloop()
```
- Creates the main window and runs the application's event loop.

---

## Notes & Recommendations
- **Screen Size**: Adjust `self.screen_size` to match your actual screen resolution for accurate recording.
- **Performance**: Recording at high frame rates or resolutions may affect performance.
- **Improvements**:
  - Run `start_recording()` in a separate thread to avoid freezing the GUI.
  - Add progress indicators or timestamp display.
  - Customize output filename and resolution options.

---

## Example Usage
1. Launch the script.
2. Click "Record" to start capturing your screen.
3. Click "Stop" to end recording and save the video as `my_video.avi`.

---

## Troubleshooting
- Ensure all dependencies are installed.
- Adjust `self.screen_size` if the resulting video is distorted or cropped.
- For high-resolution screens, consider reducing resolution for better performance.

---

This documentation provides an overview and guidance for using and modifying the screen recorder project. Feel free to extend its functionality according to your needs!
