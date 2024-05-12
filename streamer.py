import subprocess

class VideoStreamer:
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command, stdin=subprocess.PIPE)

    def stream_frame(self, frame):
        self.process.stdin.write(frame.tobytes())

    def stop(self):
        self.process.stdin.close()
        self.process.terminate()
        self.process.wait()
