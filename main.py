import requests
import os
import datetime


# ____ CREATE ACCOUNT ON PIXELA API ____
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


# ______ CREATE A GRAPH ______
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


# ____ ADD PIXEL ON  A GRAPH _____
today = (datetime.date.today()).strftime("%Y%m%d")
minutes = "11"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_NAME}"
PIXEL_PARAMS = {
    "date": today,
    "quantity": minutes,
}

# response = requests.post(url=PIXEL_ENDPOINT, json=PIXEL_PARAMS, headers=PIXELA_HEADERS)
# print(response.text)
# check the graph on : https://pixe.la/v1/users/marionroro/graphs/graph1.html



#  ____ update pixel on a graph  _____
date = today
new_minutes = "15"
UPDATE_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_NAME}/{date}"
UPDATE_PIXEL_PARAMS = {
    "quantity": new_minutes,
}

# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=UPDATE_PIXEL_PARAMS, headers=PIXELA_HEADERS)
# print(response.text)


# ____ ADD PIXEL ON  A GRAPH _____
date = today
DELETE_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_NAME}/{date}"

response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=PIXELA_HEADERS)
print(response.text)