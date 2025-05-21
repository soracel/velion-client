import requests

class SiotClient:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.headers = {
            "Content-Type": "application/json",
            "X-SIOT-API-Key": api_key
        }

    def send(self, payload):
        try:
            response = requests.post(self.api_url, json=payload, headers=self.headers)
            if response.status_code == 200:
                print(f"[OK] Gesendet: {payload}")
            else:
                print(f"[{response.status_code}] Fehler: {response.text}")
        except Exception as e:
            print(f"[Netzwerkfehler] {e}")