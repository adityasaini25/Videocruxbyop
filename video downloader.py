import yt_dlp


video_url = input('enter video url: ' )


output_path = r"C:\Users\saini\PycharmProjects\PythonProject2\Data\video2.mp4"

ydl_opts = {
    'format': 'best',
    'outtmpl': output_path,
    'noplaylist': True,
}


try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading video from: {video_url}")
        ydl.download([video_url])
        print(f"Video downloaded successfully to: {output_path}")
except Exception as e:
    print(f"An error occurred: {e}")


