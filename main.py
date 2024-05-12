from videoCapture import VideoCapture
from streamer import VideoStreamer
import cv2

def main():
    capture = VideoCapture()
    streamer = VideoStreamer([
        'ffmpeg',
        '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-s', '640x480',
        '-pix_fmt', 'bgr24',
        '-r', '25',
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        '-f', 'flv',
        'rtmp://**your vms IP address here**/live/stream'
    ])
    try:
        while True:
            frame = capture.get_frame()
            if frame is None:
                break
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            streamer.stream_frame(frame)
    finally:
        capture.release()
        streamer.stop()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
