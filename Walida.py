import json
import common

with open("user.json") as fin:
    user = fin.read()

test = json.loads(user)
common.jprint(test)

print(test[0]["user"])
print(test[0]["password"])