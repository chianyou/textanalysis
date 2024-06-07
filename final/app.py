from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import logging

# Azure Text Analytics service key and endpoint
TA_KEY = '712a88ae654741718d55010daa6bf688'
TA_ENDPOINT = 'https://chianyouanaly.cognitiveservices.azure.com/'

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_text(text):
    try:
        ta_client = TextAnalyticsClient(endpoint=TA_ENDPOINT, credential=AzureKeyCredential(TA_KEY))
        response = ta_client.analyze_sentiment(documents=[text])
        result = response[0]
        sentiment = result.sentiment
        return sentiment
    except Exception as e:
        logger.error(f"Error analyzing text: {e}")
        return None

text = "You make me very disappointed"
sentiment = analyze_text(text)
if sentiment:
    print(f"Sentiment: {sentiment}")
else:
    print("Failed to analyze sentiment.")
