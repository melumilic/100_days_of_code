from datetime import datetime
from email import header
import requests

PIXELA_AUTH_KEY = "nl2ok*&jlk3#7hvHjslk#jk2@kjl!"
PIXELA_USERNAME = "melumi"
PIXELA_GRAPHID = "graph1"
PIXELA_GRAPHNAME = "code_graph"
PIXELA_ENDPOINT = "https://pixe.la"
PIXELA_USER_ENDPOINT = f"{PIXELA_ENDPOINT}/v1/users"
PIXELA_USER_GRAPH = f"{PIXELA_ENDPOINT}/v1/users/{PIXELA_USERNAME}/graphs"
PIXELA_USER_PIXEL = f"{PIXELA_USER_GRAPH}/{PIXELA_GRAPHID}"

headers = {
    "X-USER-TOKEN":PIXELA_AUTH_KEY
}

user_profile = {
    "Token":PIXELA_AUTH_KEY,
    "username":PIXELA_USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

#pix_request = requests.post(PIXELA_USER_ENDPOINT,json=user_profile)
#print(pix_request.text)

graph_data = {
    "id":PIXELA_GRAPHID,
    "name":PIXELA_GRAPHNAME,
    "unit":"commit",
    "type":"int",
    "color":"shibafu",
    "timezone":"America/Los_Angeles",
}

#pix_graph_request = requests.post(PIXELA_USER_GRAPH,json=graph_data,headers=headers)
#print(pix_graph_request.text)

date = datetime.now();
pixel_data = {
    "date":date.strftime("%Y%M%d"),
    "quantity":"3"
}

pix_request = requests.post(PIXELA_USER_PIXEL,json=pixel_data,headers=headers)
print(pix_request.text)