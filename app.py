'''
pip install SpeechRecognition
pip install pocketsphinx
pip install moviepy
'''
import speech_recognition as sr
import urllib.request
import re

from moviepy.editor import AudioFileClip

from watson_ibm import getWatsonSpeech2txt
from formatter_custom import mp4_2_wav
import nlp_azure

import youtubeVideoDownloader
def main():

    youtube_link = "https://www.youtube.com/watch?v=Rwgux6vo9qs"
    youtubeVideoDownloader.getAudioFrom(youtube_link, output_path='source_of_knowledge', file_name='youtubeAudio.mp4')

    # convert mp4 to mav
    mp4_2_wav(audio_file)
    #print(getWatsonSpeech2txt(audio_file))
    #mp4_2_wav('ah.mp4')
    # nlp_azure.getText('output.wav')
    nlp_azure.getTextSdk('output.wav') #success: but doesn't give the entire text.