import requests
import os

PIXE_API_ENDPOINT = "https://pixe.la/v1/users"
PIXE_API_PARAMS = {
    "token": os.environ["PIXE_API_TOKEN"],
    "username": os.environ["PIXE_API_USERNAME"],
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXE_API_ENDPOINT, json=PIXE_API_PARAMS)
# print(response.text)
