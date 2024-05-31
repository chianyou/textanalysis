from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Azure Text Analytics 服務的金鑰和端點
TA_KEY = '5f45af0393fe4f53aced90f416202e30'
TA_ENDPOINT = 'https://analysis10317.cognitiveservices.azure.com/'

def analyze_text(text):
    ta_client = TextAnalyticsClient(endpoint=TA_ENDPOINT, credential=AzureKeyCredential(TA_KEY))
    result = ta_client.analyze_sentiment(documents=[text])[0]
    sentiment = result.sentiment
    return sentiment

text = "You make me very disappointed"
sentiment = analyze_text(text)
print(sentiment)
