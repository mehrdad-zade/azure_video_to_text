'''
pip install SpeechRecognition
pip install pocketsphinx
pip install moviepy
'''
import speech_recognition as sr
import urllib.request
import re
from pytube import YouTube
from moviepy.editor import AudioFileClip

# Function to download audio from YouTube video
# def download_audio_from_youtube(link):
#     # Extract video ID from link
#     video_id = re.findall(r"v=(\S+)", link)[0]
#     # Construct URL for audio stream
#     audio_url = f"https://www.youtube.com/s/{video_id}/audio"
#     # Download audio stream
#     urllib.request.urlretrieve(audio_url, f"{video_id}.mp3")
#     return f"{video_id}.mp3"
def download_audio_from_youtube(link):
    # Create YouTube object
    yt = YouTube(link)
    # Get the first stream that contains only audio
    audio_stream = yt.streams.filter(only_audio=True).first()
    # Download the audio stream as an MP4 file
    audio_file = audio_stream.download()
    # Convert the MP4 file to an MP3 file
    mp3_file = f"{yt.title}.mp3"
    audio_clip = AudioFileClip(audio_file)
    audio_clip.write_audiofile(mp3_file)
    # Return the path to the MP3 file
    return mp3_file


# Function to convert audio to text
def audio_to_text(audio_file):
    # Initialize recognizer
    r = sr.Recognizer()
    # Load audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
    # Convert audio to text
    text = r.recognize_google(audio_data)
    return text

# Example usage
link = "https://www.youtube.com/watch?v=cp9GXl9Qk_s"
audio_file = download_audio_from_youtube(link)
text = audio_to_text(audio_file)
print(text)