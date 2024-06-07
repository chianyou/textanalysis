
from flask import Flask, request, render_template
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
import logging

# Azure Text Analytics 服务的密钥和端点
TA_KEY = '712a88ae654741718d55010daa6bf688'
TA_ENDPOINT = 'https://chianyouanaly.cognitiveservices.azure.com/'

# Azure 翻译服务的密钥、区域和端点
T_KEY = '524892d740eb404ebc6ab65043fe86ac'
T_REGION = 'eastus'
T_ENDPOINT = 'https://api.cognitive.microsofttranslator.com/'

app = Flask(__name__)

# 设置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_text(text):
    try:
        ta_client = TextAnalyticsClient(endpoint=TA_ENDPOINT, credential=AzureKeyCredential(TA_KEY))
        response = ta_client.analyze_sentiment(documents=[text])
        result = response[0]
        sentiment = result.sentiment
        logger.info(f"情感分析结果: {sentiment}")
        return sentiment
    except Exception as e:
        logger.error(f"分析文本时出错: {e}", exc_info=True)
        return None

def translate_text(text):
    try:
        translator = TextTranslationClient(endpoint=T_ENDPOINT, credential=TranslatorCredential(T_KEY, T_REGION))
        targets = [InputTextItem(text=text)]
        responses = translator.translate(content=targets, to=["zh-Hant"])
        return responses[0].translations[0].text
    except Exception as e:
        logger.error(f"翻译文本时出错: {e}", exc_info=True)
        return None

@app.route("/", methods=['GET', 'POST'])
def analyze_and_translate():
    if request.method == 'POST':
        text = request.form.get('text', '')
        if not text:
            return render_template('index.html', error="未提供文本")
        
        sentiment = analyze_text(text)
        if sentiment is None:
            return render_template('index.html', error="分析文本时出错")

        translated_sentiment = translate_text(sentiment)
        if translated_sentiment is None:
            return render_template('index.html', error="翻译情感时出错")
        
        return render_template('index.html', original_text=text, sentiment=sentiment, translated_sentiment=translated_sentiment)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



