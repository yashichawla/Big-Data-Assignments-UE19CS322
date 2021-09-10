import requests
coordinates={"latitude": 35.09008,"longitude": -80.74556}
x=requests.post('http://20.185.44.219:5000/',json=coordinates)
print(x.json())