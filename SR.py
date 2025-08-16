import tkinter as tk
import time
import pyautogui

class ScreenRecorder:
    def __init__(self, master):
        self.master = master
        master.title("Screen Recorder")

        self.recording = False
        self.filename = "my_video.avi"
        self.screen_size = (1920, 1080)
        self.fps = 30.0

        self.canvas = tk.Canvas(master, width=200, height=50)
        self.canvas.pack()

        self.button = tk.Button(master, text="Record", command=self.toggle_recording)
        self.button.pack()

    def toggle_recording(self):
        if not self.recording:
            self.recording = True
            self.button.config(text="Stop")
            self.start_recording()
        else:
            self.recording = False
            self.button.config(text="Record")

    def start_recording(self):
        out = cv2.VideoWriter(self.filename, cv2.VideoWriter_fourcc(*"XVID"), self.fps, self.screen_size)
        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            time.sleep(1/self.fps)
        out.release()

root = tk.Tk()
app = ScreenRecorder(root)
root.mainloop()
