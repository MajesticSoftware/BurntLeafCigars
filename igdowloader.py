import os
from yt_dlp import YoutubeDL

# URL of the Instagram reel
instagram_url = "https://www.instagram.com/p/DDCxwAOJqJ3/"

# Output directory for the downloaded video
output_directory = "downloads"
os.makedirs(output_directory, exist_ok=True)

# Download options
ydl_opts = {
    "format": "best",  # Download the best quality available
    "outtmpl": os.path.join(output_directory, "%(title)s.%(ext)s"),  # Save with the video's title
}

# Download the video
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([instagram_url])

print("Download complete!")