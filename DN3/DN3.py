import json

with open('DN3/DATA/zacetniData.json', 'r') as f:
    startData = json.load(f)

with open('DN3/DATA/updateData.json', 'r') as f:
    updateData = json.load(f)

name_to_person = {person["name"]: person for person in startData["persons"]}

for updated_person in updateData["persons"]:
    name = updated_person["name"]
    if name in name_to_person:
        person = name_to_person[name]
        for key, value in updated_person.items():
            if key in person:
                person[key] = value

print(startData)

with open('DN3/DATA/posodobljenData.json', 'w') as f:
    json.dump(startData, f, indent=2)