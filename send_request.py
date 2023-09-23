import requests

headers = {
    'Content-Type': 'multipart/form-data',
    #'x-api-key': 'xxxxxx-xxxxx-xxxx-xxxx-xxxxxxxx',
}

files = {
    'file': open('./e.jpg', 'rb'),
}
r = requests.post('http://46.242.121.246:25601', headers=headers, files={'file': open('./iz2.png', 'rb')})
print(r.json())

#requests.post('http://localhost:25601', files={'file': open('./iz2.png', 'rb'),})
#response = requests.post('http://localhost:5000/', headers=headers, files=files)
#print(response)