# <img src="https://github.com/user-attachments/assets/27f0e6f9-b491-4848-89b8-5445fe6d93a2" alt="youtube-logo" width=32 /> 🔊 YouTube Audio Downloader

### 📦 Requirements
- Python 3.12
- PIP package manager

## Installation
1. Install dependencies:
   
    ```bash
    git clone https://github.com/mashisdev/youtube-audio-downloader.git
    cd youtube-audio-downloader
    pip install -r requirements.txt
    python main.py
    ```
2. Install ffmpeg: the external tool used to convert the downloaded files to MP3. If you haven't installed it, you can get it from the official [FFmpeg website](https://ffmpeg.org/download.html).

    [![How to install ffmpeg on Windows](https://markdown-videos-api.jorgenkh.no/url?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DJR36oH35Fgg)](https://www.youtube.com/watch?v=JR36oH35Fgg)
4. Locate the `ydl_opts` dictionary and configure the value of `ffmpeg_location` variable. For example, if your ffmpeg folder is in `C:\ffmpeg`, the path would be `C:/ffmpeg/bin`.
