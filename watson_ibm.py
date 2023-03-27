import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



def getWatsonSpeech2txt(audio_file):
    
    # Set up authentication
    authenticator = IAMAuthenticator('HW9Buf20uOtY2u9T37ADCygeBNLQsWZ7DHstRC7kYm_G')
    speech_to_text = SpeechToTextV1(authenticator=authenticator)

    # Set up service URL
    speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com')

    # Transcribe audio file
    with open(audio_file, 'rb') as af:
        result = speech_to_text.recognize(
            audio=af,
            content_type='audio/mp4',
            model='en-US_NarrowbandModel',
            timestamps=True,
            word_confidence=True
        ).get_result()

    # Print transcription
    transcription = result['results'][0]['alternatives'][0]['transcript']
    #print(transcription)
    return transcription