import requests
import os
import datetime


# create account on pixela
PIXELA_API_ENDPOINT = "https://pixe.la/v1/users"
token = os.environ["PIXELA_API_TOKEN"]
username = os.environ["PIXELA_API_USERNAME"]
PIXELA_API_PARAMS = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_API_ENDPOINT, json=PIXELA_API_PARAMS)
# print(response.text)


# # create a graph
GRAPH_ENDPOINT = f"{PIXELA_API_ENDPOINT}/{username}/graphs"
GRAPH_NAME = "graph1"
GRAPH_PARAMS = {
    "id": GRAPH_NAME,
    "name": "Meditation Time Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
}
PIXELA_HEADERS = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PARAMS, headers=PIXELA_HEADERS)
# print(response.text)

# add a pixel on a graph
today = (datetime.date.today()).strftime("%Y%m%d")
minutes = "11"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_NAME}"
PIXEL_PARAMS = {
    "date": today,
    "quantity": minutes,
}

response = requests.post(url=PIXEL_ENDPOINT, json=PIXEL_PARAMS, headers=PIXELA_HEADERS)
print(response.text)