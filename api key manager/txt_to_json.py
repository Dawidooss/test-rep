import json
import time

apikeys = {}

with open("../apikeys.json", "r") as f:
    old_apikeys = json.load(f)
    for apikey, total in old_apikeys.items():
        apikeys[apikey] = total
    

with open("apikeys.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if not (line in apikeys):
            apikeys[line] = 0

with open("../apikeys.json", "w") as f:
    json.dump(apikeys, f, indent=2)

print("DONE")    
time.sleep(2)