import json
import time
import requests

apikeys = json.load(open("../apikeys.json","r"))

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
} 

total_working = 0
total_down = 0
total_bots = 0

for apikey in apikeys.keys():
    print(apikey)
    url = "https://api.uptimerobot.com/v2/getMonitors"
    payload = "api_key="+apikey+"&format=json&statuses=2-9"
    response = requests.request("POST", url, data=payload, headers=headers)
   
    data = json.loads(response.text)
    
    for monitor in data['monitors']:
        monitor_id = monitor['id']
        if monitor['status'] == 2:
            total_working += 1
        else:
            total_down += 1
        total_bots += 1
print('\n')
print("Total Working: "+str(total_working))
print("Total Down: "+str(total_down))
print("Total Bots: "+str(total_bots))

time.sleep(60)