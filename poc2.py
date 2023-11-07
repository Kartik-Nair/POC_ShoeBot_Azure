import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient
from azure.ai.textanalytics import TextAnalyticsClient


# clu_endpoint = "https://clu-sample-instance.cognitiveservices.azure.com/"
# clu_key = "6258c8f56b7a448ea9331fda1cced398"

clu_endpoint = "https://clu1-westus2.cognitiveservices.azure.com/"
clu_key = "11bc08a610754c618d20ff4173700b97"

# client = ConversationAnalysisClient(clu_endpoint, AzureKeyCredential(clu_key))
client = TextAnalyticsClient(clu_endpoint, AzureKeyCredential(clu_key))
with client:
    query = ["Find me Adidas shoes under 100 euros and size 8"]

    # documents = ["I hated the movie. It was so slow!", "The movie made it into my top ten favorites. What a great movie!"]
    
    result = client.recognize_entities(query)
    client.begin_recognize_custom_entities
    # result2 = client.
    print(result)