import tkinter as tk
from moviepy.editor import VideoFileClip
import os

class VideoPlayer:
    def __init__(self, parent, video_filenames):
        self.parent = parent
        self.video_filenames = video_filenames
        self.current_video = None
        self.video_index = 0
        self.create_widgets()

    def create_widgets(self):
        self.video_frame = tk.Frame(self.parent)
        self.video_frame.pack()

        self.play_button = tk.Button(self.parent, text="Play", command=self.play_video)
        self.play_button.pack()

    def play_video(self):
        if self.current_video is not None:
            self.current_video.close()

        if self.video_index >= len(self.video_filenames):
            return

        video_filename = self.video_filenames[self.video_index]
        self.current_video = VideoFileClip(video_filename)
        self.current_video.preview(fps=30, fullscreen=False,
                                    #win_title="Video Player",
                                    audio=False
                                    )

        self.play_next_video()

    def play_next_video(self):
        print("hi")
        self.video_index += 1
        self.play_video()


def get_video(letter):
    pathtofile = os.getcwd()

    if letter == ' ' or letter == "'":
        thepath = os.path.join(pathtofile, "ASL Letter Videos", "Space.mp4")

    else:
        ltr = str(letter)
        ltrp = ltr + ".mp4"
        thepath = os.path.join(pathtofile, "ASL Letter Videos", ltrp)
    print(thepath)
    return thepath



root = tk.Tk()
root.title("Video Player")

video_filenames = ["ASL Letter Videos/q.mp4", "ASL Letter Videos/b.mp4", "ASL Letter Videos/x.mp4", "ASL Letter Videos/a.mp4"]
player = VideoPlayer(root, video_filenames)
#player.play_next_video()
root.mainloop()