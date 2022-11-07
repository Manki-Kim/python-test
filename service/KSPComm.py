
import requests

def KSPLogin(strUrl, dicHeader, dicData):
    response = requests.post(strUrl, headers=dicHeader, data=dicData)
    #print(response.text)
    response.raise_for_status()
    return response.text