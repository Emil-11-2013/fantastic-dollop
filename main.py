import requests
from config import hf_api_key

def classify_text(text):
    API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    headers = {"Authorization": f"Bearer {hf_api_key}"}
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json() 

if __name__ == "__main__":
    sample_text = "I love programming!"
    result = classify_text(sample_text)
    print(f"Input Text: {sample_text}")
    print(f"Classification Result: {result}")   

