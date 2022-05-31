max_threads = 20

# import http.client
from email import header
from turtle import update
import requests
import json
import time
import threading

monitors = []
threads = 0

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
} 

apikeys = json.load(open("../apikeys.json", "r"))

def update_file():
    print("updating file")
    with open("../apikeys.json", "w") as f:
        json.dump(apikeys, f, indent=2)

def thread_fun(api_monitors):
    global threads
    apikey = api_monitors['apikey']
    length = len(api_monitors['down'])
    for i, monitor_id in enumerate(api_monitors['down']):
        try:
            time.sleep(7)
            print(f"{i+1} / {length} - {apikey}")
            payload = f"api_key={apikey}&format=json&id={monitor_id}"
            url = "https://api.uptimerobot.com/v2/deleteMonitor"
            requests.request("POST", url, data=payload, headers=headers)
            apikeys[apikey] -= 1
            update_file()
            # stat = json.loads(response.text)['stat']
        except Exception as e:
            print(e)
    threads -= 1
    update_file()
    print(f"CLEARED {apikey}")

for apikey in apikeys.keys(): 
    api_monitors = {
        "apikey": apikey,
        "up": [],
        "down": []
    }
    monitors.append(api_monitors)

    url = "https://api.uptimerobot.com/v2/getMonitors"
    payload = "api_key="+apikey+"&format=json&statuses=2-9"
    response = requests.request("POST", url, data=payload, headers=headers)
   
    data = json.loads(response.text)
    
    for monitor in data['monitors']:
        monitor_id = monitor['id']
        if monitor['status'] == 2:
            api_monitors['up'].append(monitor_id)
        else:
            api_monitors['down'].append(monitor_id)
    total_up = len(api_monitors['up'])
    total_down = len(api_monitors['down'])
    total = total_down + total_up
    apikeys[apikey] = total
    print(f"{apikey}\n\tUP -    {total_up}\n\tDOWN -  {total_down}\n\tTOTAL - {total}")
    
update_file()
print(f"\nREMOVING DOWN ROBOTS ON {max_threads} THREADS!")

while len(monitors) > 0:
    api_monitors = monitors.pop(0)
    while threads >= max_threads:
        time.sleep(1)
    thread = threading.Thread(target=thread_fun, args=[api_monitors])
    threads += 1
    print(f"START CLEARING {apikey}")
    thread.start()
    # time.sleep(1)
