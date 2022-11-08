
import requests

def KSPLogin(strUrl, dicHeader, dicData):
    try:
        response = requests.post(strUrl, headers=dicHeader, data=dicData)
        #print(response.text)
        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    return response.text


def KSPGetConfigMap(url, header):
    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()
        jsonResponse = response.json()

        user_k8s_config = jsonResponse['data']['config']

        lb = "http://192.168.0.2:80"
        user_k8s_config = "" + user_k8s_config
        user_k8s_config = user_k8s_config.replace("https://10.96.0.1:443", lb)
    except Exception as err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    return user_k8s_config