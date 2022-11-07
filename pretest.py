import requests

from service import KSPComm


# def KSPLogin(strUrl, dicHeader, dicData):
#     response = requests.post(strUrl, headers=dicHeader, data=dicData)
#     #print(response.text)
#     response.raise_for_status()
#     return response.text

url = 'http://35.223.167.128:32116/oauth/token'
header = {'Content-Type':'application/x-www-form-urlencoded'}
scriptData = { 'grant_type': 'password',
               'username':'admin',
               'password':'P@88w0rd',
               'client_id':'kubesphere',
               'client_secret':'kubesphere'}

retValue = KSPComm.KSPLogin(url, header, scriptData)
print('KSPLogin Token #1 : \n', retValue)




