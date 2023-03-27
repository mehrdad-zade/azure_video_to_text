import requests
import json
import azure.cognitiveservices.speech as speechsdk
from secrets_custom import azure_speech2text_subscription_token, azure_speech2text_access_token_endpoint, azure_speech2text_api_endpoint, azure_speech2text_region


def getText(audio_file_path):

    # Set the headers
    headers = {
        'Ocp-Apim-Subscription-Key': azure_speech2text_subscription_token,
        'Authorization': 'Bearer ' + getAccessToken(),
        'Content-Type': 'audio/wav'
    }

    params = {
        'language': 'en-US'
    }

    # Read the audio file as binary data
    # with open(audio_file_path, 'rb') as f:
    #     audio_data = f.read()
    audio_data = open(audio_file_path, 'rb')

    response = requests.post(azure_speech2text_api_endpoint, headers=headers, params=params, data=audio_data)
    print(response.status_code)  
    # print(response.json()['DisplayText'])
   
   
def getTextSdk(audio_file_path):
    # Set up the speech configuration
    speech_config = speechsdk.SpeechConfig(subscription=azure_speech2text_subscription_token, region=azure_speech2text_region)

    # Set up the audio configuration
    audio_config = speechsdk.AudioConfig(filename=audio_file_path)

    # Create a speech recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Recognize speech from the audio file
    result = speech_recognizer.recognize_once()

    # Print the transcribed text
    print(result.text)


def getAccessToken():
    headers = {
        'Ocp-Apim-Subscription-Key': azure_speech2text_subscription_token
    }
    response = requests.post(azure_speech2text_access_token_endpoint, headers=headers)
    access_token = str(response.text)
    return access_token
    #print('Access token:', access_token)

#print(json.dumps(response.json(), indent=4))    