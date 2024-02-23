import requests
import json

def send_https_request(prompt, temperature):
    
    url = "https://localhost:8385/composeEmail"  # Your endpoint URL
    payload = {
        "prompt": prompt,
        "temperature": temperature
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)  
        response.raise_for_status()  # Raise an error if the request fails
        print(response.text)  
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}") 

# Example usage
my_prompt = "Write a funny poem about a cat."
my_temperature = 0.7  

send_https_request(my_prompt, my_temperature)
