import requests


ip = requests.get('http://165704599489980799.dev.checkerproxy.org/?num=1&area_type=1&level=2').text
proxies = { "http": "http://"+ip}