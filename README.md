Live Video Streaming with Nginx and FFmpeg

**Project Description**
This project enables live video streaming using Nginx and FFmpeg on a virtual machine. Users initiate the video stream by running a Python script on their local computer, and the stream is broadcasted through a cloud-based VM.

****Getting Started****
**Prerequisites**
To use this project, the following software needs to be installed:

#
*Nginx
*FFmpeg
*Python 3.x
#

**Installation**
**1.Installing Nginx and FFmpeg:** Install Nginx and FFmpeg on the VM.
-> sudo apt update
-> sudo apt install nginx ffmpeg

**2. Nginx Configuration:** Add the necessary RTMP module and HLS settings to the nginx.conf file.
**3.Replacing the HTML File:** Replace the HTML file in the root directory of Nginx with the index.html provided in this repository.

****USAGE****
# 1. Start Nginx on the VM: "sudo systemctl start nginx"
# 2. Start the video stream by running the Python script on your local machine: "python main.py"


