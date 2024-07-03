import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'height':20, 'width':4.3, 'mass':5.5, 'color_score':0.75})
print(r.json())