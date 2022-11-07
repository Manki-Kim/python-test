import requests

url = 'http://35.223.167.128:32116/oauth/token'
header = { 'Content-Type':'application/x-www-form-urlencoded'}

scriptData = { 'grant_type': 'password',
               'username':'admin',
               'password':'P@88w0rd',
               'client_id':'kubesphere',
               'client_secret':'kubesphere'}

response = requests.post(url, headers=header, data=scriptData)
print(response.text)
response.raise_for_status()


