import requests
from datetime import datetime

# https://pixe.la/v1/users/rob1234567/graphs/graph1.html   completed url to view project

TOKEN = "24689RTHG"
USERNAME = "rob1234567"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# created user with line below
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Study Graph",
    "unit": "hrs",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# created graph with line below
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# posting a pixel on the graph
pix_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime.now()
quantity = input("Enter amount of time spent studying: ")

pix_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity,
}

# pix_post = requests.post(url=pix_endpoint, json=pix_data, headers=headers)
# print(pix_post.text)

# update/PUT pixel requests
pix_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
update_data = {
    "quantity": quantity,
}

pix_update = requests.put(url=pix_update_endpoint, json=update_data, headers=headers)
print(pix_update.text)

# delete a pixel
pix_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
pix_delete = requests.delete(url=pix_delete_endpoint, headers=headers)
print(pix_delete.text)
