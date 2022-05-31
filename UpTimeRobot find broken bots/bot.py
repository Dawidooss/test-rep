import json
import time
import requests

apikeys = json.load(open("../apikeys.json","r"))

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
} 

for apikey in apikeys.keys():
    print(apikey)
    url = "https://api.uptimerobot.com/v2/getMonitors"
    payload = "api_key="+apikey+"&format=json&logs=1"
    response = requests.request("POST", url, data=payload, headers=headers)
   
    data = json.loads(response.text)
    
    # print(data)

    total_working = 0

    broken = False

    for monitor in data['monitors']:
        monitor_id = monitor['id']
        if monitor['status'] == 2:
            total_working += 1
            # working
            continue
        elif monitor['status'] == 0:
            print("BROKEN APIKEY")
            broken = True
            
            new_apikeys = json.load(open("../apikeys.json", "r"))
            del new_apikeys[apikey]
            json.dump(new_apikeys, open("../apikeys.json", "w"), indent=4)
            
            new_apikeys = json.load(open("../broken_apikeys.json", "r"))
            new_apikeys.append(apikey)
            json.dump(new_apikeys, open("../broken_apikeys.json", "w"), indent=4)
            
            break
        else:
            # not working
            monitor_url = monitor['url']
            url = "https://api.uptimerobot.com/v2/deleteMonitor"
            payload = "api_key="+str(apikey)+"&id="+str(monitor_id)
            response = requests.request("POST", url, data=payload, headers=headers)
            data = json.loads(response.text)

            if (data and data['stat'] == 'ok'):
                url = "https://api.uptimerobot.com/v2/newMonitor"
                payload = "api_key="+apikey+"&format=json&type=1&url="+url+"&friendly_name="+url
                response = requests.request("POST", url, data=payload, headers=headers)
                data = json.loads(response.text)
                stat = data['stat']
                print("Status: " + stat)
                if (stat == 'ok'):
                    total_working += 1
    if broken:
        continue
    new_apikeys = json.load(open("../apikeys.json", "r"))
    new_apikeys[apikey] = total_working
    json.dump(new_apikeys, open("../apikeys.json", "w"), indent=4)

time.sleep(60)