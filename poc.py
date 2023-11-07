import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient
from azure.ai.language.conversations.authoring import ConversationAuthoringClient

# endpoint = "https://clu-sample-instance.cognitiveservices.azure.com/"
# credential = AzureKeyCredential("config")
# analysis_client = ConversationAnalysisClient(endpoint, credential)


# authoring_client = ConversationAuthoringClient(endpoint, credential)

# get secrets
clu_endpoint = "https://clu-sample-instance.cognitiveservices.azure.com/"
clu_key = "config"

clu_endpoint = "https://clu1-westus2.cognitiveservices.azure.com/"
clu_key = "config"

# project_name = os.environ["AZURE_CONVERSATIONS_PROJECT_NAME"]
# deployment_name = os.environ["AZURE_CONVERSATIONS_DEPLOYMENT_NAME"]

# analyze quey
client = ConversationAnalysisClient(clu_endpoint, AzureKeyCredential(clu_key))
with client:
    query = "Send an email to Carol about the tomorrow's demo"
    documents = ["I hated the movie. It was so slow!", "The movie made it into my top ten favorites. What a great movie!"]
    
    result = client.analyze_conversation(
        task={
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "participantId": "1",
                    "id": "1",
                    "modality": "text",
                    "language": "en",
                    "text": query
                },
                "isLoggingEnabled": False
            },
            "parameters": {
                "projectName": "CLU1-WestUS2",
                "deploymentName": "SampleDeployment",
                "verbose": True
            }
        }
    )

# view result
print("query: {}".format(result["result"]["query"]))
print("project kind: {}\n".format(result["result"]["prediction"]["projectKind"]))

print("top intent: {}".format(result["result"]["prediction"]["topIntent"]))
print("category: {}".format(result["result"]["prediction"]["intents"][0]["category"]))
print("confidence score: {}\n".format(result["result"]["prediction"]["intents"][0]["confidenceScore"]))

print("entities:")
for entity in result["result"]["prediction"]["entities"]:
    print("\ncategory: {}".format(entity["category"]))
    print("text: {}".format(entity["text"]))
    print("confidence score: {}".format(entity["confidenceScore"]))
    if "resolutions" in entity:
        print("resolutions")
        for resolution in entity["resolutions"]:
            print("kind: {}".format(resolution["resolutionKind"]))
            print("value: {}".format(resolution["value"]))
    if "extraInformation" in entity:
        print("extra info")
        for data in entity["extraInformation"]:
            print("kind: {}".format(data["extraInformationKind"]))
            if data["extraInformationKind"] == "ListKey":
                print("key: {}".format(data["key"]))
            if data["extraInformationKind"] == "EntitySubtype":
                print("value: {}".format(data["value"]))