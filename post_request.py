import requests

def request_webhook_token():
    api_endpoint = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    
    user_details = {
        "name": "Anhad Rana",
        "regNo": "0827CS221037",
        "email": "anhadrana221095@acropolis.in"
    }

    try:
        response = requests.post(api_endpoint, json=user_details)
        response.raise_for_status()
        response_data = response.json()

  
        print("Response data:", response_data)

        webhook_url = response_data.get("webhook")
        access_token = response_data.get("accessToken")


        print("\nWebhook details received successfully:")
        print(f"Webhook URL   : {webhook_url}")
        print(f"Access Token  : {access_token}\n")

    except requests.RequestException as error:
        print("\nFailed to generate webhook.")
        print(f"Error: {error}\n")

if __name__ == "__main__":
    request_webhook_token()
