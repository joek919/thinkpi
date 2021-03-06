import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    username='',
    password='',
    x_watson_learning_opt_out=False
)

#print(json.dumps(speech_to_text.models(), indent=2))
#print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open(join(dirname(__file__), 'speech.wav'),'rb') as audio_file:
    response = speech_to_text.recognize(audio_file, content_type='audio/wav', timestamps=True, word_confidence=True)
    #print(json.dumps(response,indent=2))
    transcript = response['results'][0]['alternatives'][0]['transcript']
    print(transcript)
