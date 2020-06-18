import requests
 
res = requests.post('http://127.0.0.1:15000/postAPI/', data={'a':3, 'b':4})
print(res.text)