from flask import Flask, request
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

# Azure Text Analytics 服務的金鑰和端點
TA_KEY = '5f45af0393fe4f53aced90f416202e30'
TA_ENDPOINT = 'https://analysis10317.cognitiveservices.azure.com/'

# Azure 翻譯服務的金鑰、位置和端點
T_KEY = '48e9fd120ac34d0e8fa8ca91172055ee'
T_REGION = 'eastus2'
T_ENDPOINT = 'https://api.cognitive.microsofttranslator.com/'

app = Flask(__name__)

def analyze_text(text):
    ta_client = TextAnalyticsClient(endpoint=TA_ENDPOINT, credential=AzureKeyCredential(TA_KEY))
    result = ta_client.analyze_sentiment(documents=[text])[0]
    sentiment = result.sentiment
    return sentiment

def translate_text(text):
    translator = TextTranslationClient(endpoint=T_ENDPOINT, credential=TranslatorCredential(T_KEY, T_REGION))
    targets = [InputTextItem(text=text)]
    responses = translator.translate(content=targets, to=["zh-Hant"])
    return responses[0].translations[0].text

@app.route("/", methods=['GET', 'POST'])
def analyze_and_translate():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_text(text)
        translated_sentiment = translate_text(sentiment)
        return translated_sentiment
    else:
        return '''
            <form method="post">
                <textarea name="text" rows="4" cols="50"></textarea><br>
                <input type="submit" value="分析">
            </form>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
