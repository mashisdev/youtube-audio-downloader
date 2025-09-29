import yt_dlp
import os

def download_audio(url: str):
    downloads_folder = os.path.join(os.path.dirname(__file__), "downloads")
    os.makedirs(downloads_folder, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(downloads_folder, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "ffmpeg_location": "C:/ffmpeg/bin",
        # Nuevas opciones para evitar el problema
        "extract_flat": False,
        "ignore_errors": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error durante la descarga: {e}")

if __name__ == "__main__":
    video_url = str(input("Enter the YouTube video URL: ")).strip()
    download_audio(video_url)
    print("Download completed! File saved in the 'downloads' folder.")