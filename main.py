import requests
import os


PIXELA_API_ENDPOINT = "https://pixe.la/v1/users"
token = os.environ["PIXELA_API_TOKEN"]
username = os.environ["PIXELA_API_USERNAME"]
PIXELA_API_PARAMS = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# create account on pixela
# response = requests.post(url=PIXELA_API_ENDPOINT, json=PIXELA_API_PARAMS)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_API_ENDPOINT}/{username}/graphs"
GRAPH_PARAMS = {
    "id": "graph1",
    "name": "Meditation Time Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
}
GRAPH_HEADERS = {
    "X-USER-TOKEN": token
}

# create a graph
response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PARAMS, headers=GRAPH_HEADERS)
print(response.text)
