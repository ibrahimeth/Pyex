import json
import time
x = []
with open("bigdatabanka.json","r",encoding="UTF-8") as file:
    info = json.load(file)
    for i in info :
        information = json.loads(i)
        x.append(information["password"])
        print(x)

