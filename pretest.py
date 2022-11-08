
import json
import requests
from service import KSPComm
from requests.exceptions import HTTPError

def jsonLogin (url):
    try:
        print(url)
        response = requests.get(url)
        #response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        print("Entire JSON response")
        print(jsonResponse)

        print("JSON response[step_status]")
        print(jsonResponse['step_status'])

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def jsonConfigMap(url):
    try:
        print(url)
        header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Njc5MjM4NjIsImlhdCI6MTY2NzkxNjY2MiwiaXNzIjoia3ViZXNwaGVyZSIsInN1YiI6ImFkbWluIiwidG9rZW5fdHlwZSI6ImFjY2Vzc190b2tlbiIsInVzZXJuYW1lIjoiYWRtaW4ifQ.MK9O6GpY53gHzWbm429VMTbyOZ7tW4wYUqRyQzq2sD4"}
        response = requests.get(url, headers=header)
        jsonResponse = response.json()
        print(jsonResponse)

        print("JSON response3['data']['config']")
        user_k8s_config = jsonResponse['data']['config']
        print(user_k8s_config)

        lb = "http://192.168.0.2:80"
        user_k8s_config = ""+ user_k8s_config
        user_k8s_config = user_k8s_config.replace("https://10.96.0.1:443", lb)
        print(f"chagned : %s", user_k8s_config)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')



def menu():
    print("MAIN MENU")
    print("-----------------")
    print("1. Kubesphere Login")
    print("2. Kubesphere Get ConfigMap")
    print("3. kubesphere cm ")

    choice = input("Choose menu option (1-3): ")
    while choice not in ['1', '2', '3']:
        choice = input("Invalid choice.  Choose menu option (1-3): ")
    return int(choice)


menu_chosen = True
choice = menu()
print("You chose menu option", choice)

if choice == 1:
    url = "http://localhost:8000/login"
    jsonLogin(url=url)
elif choice == 2:
    url = "http://35.223.167.128:32116/api/clusters/member1/v1/namespaces/kubesphere-controls-system/configmaps/kubeconfig-user2/"
    jsonConfigMap(url=url)
elif choice == 3:
    print("choice 3")
    # url = "http://35.223.167.128:32116/api/clusters/member1/v1/namespaces/kubesphere-controls-system/configmaps/kubeconfig-user2/"
    # json_ksp_cm(url=url)
