import json
import time
import requests
from threading import Thread

apikeys = json.load(open("../apikeys.json","r"))
broken_apikeys = json.load(open("../broken_apikeys.json","r"))

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
} 

def find_avaible_apikey():
    for apikey, amount in apikeys.items():
        if amount < 50:
            return apikey


def main():
    work = True
    while work:
        if (len(broken_apikeys) == 0):
            return
        broken_apikey = broken_apikeys[0]
        broken_apikeys.pop()

        print(broken_apikey)

        url = "https://api.uptimerobot.com/v2/getMonitors"
        payload = "api_key="+broken_apikey+"&format=json"
        response = requests.request("POST", url, data=payload, headers=headers)

        # print(response.text)

        data = json.loads(response.text)
        
        print(len(data['monitors']))

        total_working = 0

        broken = False

        for monitor in data['monitors']:
            monitor_id = monitor['id']
            if monitor['status'] == 0:
                
                monitor_url = monitor['url']
                
                apikey = find_avaible_apikey()
                if (not apikey):
                    return "All apikeys full!"

                # print(monitor_url)

                url = "https://api.uptimerobot.com/v2/newMonitor"
                payload = "api_key="+apikey+"&format=json&type=1&url="+monitor_url+"&friendly_name="+monitor_url
                # print(payload)
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                if ("Rate limit" in response.text):
                    print('extended time')
                    time.sleep(6)
                    continue
                data = json.loads(response.text)

                if (data['stat'] == 'fail'):
                    print('already exists')
                    time.sleep(6)
                    continue
                print('works :)')

                new_apikeys = json.load(open("../apikeys.json", "r"))
                new_apikeys[apikey] += 1
                json.dump(new_apikeys, open("../apikeys.json", "w"), indent=4)
            time.sleep(6)

for i in range(10):
    t = Thread(target=main)
    t.start()
    time.sleep(3)


input("Zamknij...")