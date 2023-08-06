import http.client
import json
import os

def lambda_handler(event, context):
    body = json.loads(event["body"])
    conversation_history = body["conversation_history"]
    completion = get_completion(conversation_history)
    responseObject = {}
    responseObject["statusCode"] = 200
    responseObject["headers"] = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "https://www.joshuahkirby.com",
        "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type",
    }
    responseObject["body"] = json.dumps({"bot_message": completion})
    return responseObject

def get_completion(conversation):
    connection = http.client.HTTPSConnection("api.openai.com")
    api_key = os.getenv("OPENAI_API_KEY")
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    data = {"model": "gpt-3.5-turbo", "temperature": 0, "messages": conversation}
    payload = json.dumps(data)
    connection.request("POST", "/v1/chat/completions", payload, headers)
    response = connection.getresponse()
    completion = json.loads(response.read().decode("utf-8"))["choices"][0]["message"]["content"]
    return completion
