import requests
import json

def emotion_detect(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = obj, headers=header, verify=False) # Send a POST request to the API with the text and headers 
    jsonobj = json.loads(response.text)
    emotions = jsonobj["emotionPredictions"][0]["emotion"]
    dominent_emo = max(emotions, key=emotions.get)
    emotions["dominent_emotion"] =dominent_emo
    return emotions

