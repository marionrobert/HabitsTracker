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
def add_pixel():
    today = (datetime.date.today()).strftime("%Y%m%d")
    PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_NAME}"
    PIXEL_PARAMS = {
        "date": today,
        "quantity": input("How many minutes did you meditate today? "),
    }
    add_response = requests.post(url=PIXEL_ENDPOINT, json=PIXEL_PARAMS, headers=PIXELA_HEADERS)
    print(add_response.text)
    # check the graph on : https://pixe.la/v1/users/marionroro/graphs/graph1.html


#  ____ update pixel on a graph  _____
def update_pixel():
    update_date = input("For which day do you want to update the pixel? Please, respect this format: yyyyMMdd. ")
    new_minutes = input("How many minutes did you meditate this day? ")
    UPDATE_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_NAME}/{update_date}"
    UPDATE_PIXEL_PARAMS = {
        "quantity": new_minutes,
    }
    response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=UPDATE_PIXEL_PARAMS, headers=PIXELA_HEADERS)
    print(response.text)


# ____ ADD PIXEL ON  A GRAPH _____
def delete_pixel():
    delete_date = input("For which day do you want to delete the pixel? Please, respect this format: yyyyMMdd. ")
    DELETE_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_NAME}/{delete_date}"
    delete_response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=PIXELA_HEADERS)
    print(delete_response.text)



app_on = True

while app_on:
    action = input("What action do you want to do ? \nAdd a new pixel for today: type 'add'. \nUpdate a pixel: type 'update'. \nDelete a pixel: type 'delete'. \nExit: type 'exit'. \n--> ").lower()
    if action == "add":
        add_pixel()
    elif action == "update":
        update_pixel()
    elif action == "delete":
        delete_pixel()
    elif action == "exit":
        app_on = False
        print("Bye bye!")