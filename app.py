import youtubeVideoDownloader
from formatter_custom import mp4_2_wav
from nlp_azure import azure_speech_to_text

def main():
    '''
    youtube_link = "https://www.youtube.com/watch?v=Rwgux6vo9qs"
    youtubeVideoDownloader.getAudioFrom(youtube_link, output_path='source_of_knowledge', file_name='youtubeAudio.mp4')

    # convert mp4 to mav
    mp4_2_wav("source_of_knowledge/youtubeAudio.mp4")
    '''

    print("-------------------------------------------")
    azure_speech_to_text('source_of_knowledge/output.wav') #success: but doesn't give the entire text.
    print("-------------------------------------------")


if __name__ == "__main__":
    main()