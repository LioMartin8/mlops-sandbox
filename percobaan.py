import json

with open("dodol.json", "w") as file:
    asa = []
    history = json.dump(asa, file)

print(type(history))
