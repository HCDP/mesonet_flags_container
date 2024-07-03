import os
import requests

hcdp_api_token = os.environ.get("HCDP_API_TOKEN")
print(hcdp_api_token)
header = {
    "Authorization": f"Bearer {hcdp_api_token}"
}
body = {
    "recepients": ["mcleanj@hawaii.edu"],
    "source": "Mesonet flags test",
    "type": "INFO",
    "message": os.environ.get("MSG")
}


# res = requests.post("https://api.hcdp.ikewai.org/notify", headers = header, json = body)
# print(res)