#APIS

import requests
#Get fake apis from {JSON} Placeholder
response = requests.get("https://jsonplaceholder.typicode.com/comments")

if response.status_code == 200:
    data = response.json()

    print("Success !")

else:
    print("Failed !")

