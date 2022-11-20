import requests
import json

url = "https://ilharu-node.saltmine.kr/v1/partner/kpi/visit"
headers = {"Content-Type": "application/json", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZG1pbklkIjoiNjM1YTc5Zjc3ZGUzMWIwMDEyMzdhOGZkIiwiY29tcGFueU5hbWUiOiLsnbztlZjro6giLCJpYXQiOjE2Njg0ODc3MDcsImV4cCI6MTY2OTQ4NzcwN30.8xleP82Ja-9MwuJEwz2O2WsFh7Qbx-xLWZv-z4RcPSc"}
response = requests.post(url, headers=headers)

print(response.text)
print(response.json()["content"])