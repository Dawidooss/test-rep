import json
import time
import requests
from pypresence import Presence 
import time

start = int(time.time())
client_id = "936023427842736210" 
RPC = Presence(client_id)
RPC.connect()
while True:
    try:
        apikeys = json.load(open("../apikeys.json","r"))

        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        } 

        total_working = 0
        total_down = 0
        total_bots = 0

        for apikey, amount in apikeys.items():
            print(apikey)
            if amount == 0:
                continue
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
        RPC.update(
                large_image = "status_dawidooss3", #name of your asset
                large_text = "HTTPS Bots:",
                details = "Up: "+str(total_working) , #Https Bots Online:
                state = "Down: "+str(total_down), #2000
                start = start,
            )
    except Exception as e:
        print(e)
    time.sleep(120)