import time
import requests

while True:
    try:
        resp = requests.get('http://127.0.0.1:5000/aaa/bbb')
    except:
        print('connection error')
    else:
        print(resp.status_code)
    time.sleep(1)
    
