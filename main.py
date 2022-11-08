from typing import Union
from service import KSPComm
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/login")
async def read_root():
    url = 'http://35.223.167.128:32116/oauth/token'
    header = {'Content-Type':'application/x-www-form-urlencoded'}
    scriptData = { 'grant_type': 'password',
                   'username':'admin',
                   'password':'P@88w0rd',
                   'client_id':'kubesphere',
                   'client_secret':'kubesphere'}

    retData = KSPComm.KSPLogin(url, header, scriptData)

    return Response(content=retData, media_type="application/json")


@app.get("/configmap")
async def read_root():
    url = "http://35.223.167.128:32116/api/clusters/member1/v1/namespaces/kubesphere-controls-system/configmaps/kubeconfig-user2/"
    header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Njc5MjM4NjIsImlhdCI6MTY2NzkxNjY2MiwiaXNzIjoia3ViZXNwaGVyZSIsInN1YiI6ImFkbWluIiwidG9rZW5fdHlwZSI6ImFjY2Vzc190b2tlbiIsInVzZXJuYW1lIjoiYWRtaW4ifQ.MK9O6GpY53gHzWbm429VMTbyOZ7tW4wYUqRyQzq2sD4"}

    retData = KSPComm.KSPGetConfigMap(url, header)

    return Response(content=retData, media_type="application/json")