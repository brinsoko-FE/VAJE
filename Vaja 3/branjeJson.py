import json

with open('/Users/brinsoko/Documents/TP/VAJE/Vaja 3/VAJE/VAJE-3/DATA/person.json', 'r') as f:
    deserialized_person = json.load(f)

deserialized_person['age'] = 40
deserialized_person['married'] = False



with open('/Users/brinsoko/Documents/TP/VAJE/Vaja 3/VAJE/VAJE-3/DATA/updatedPerson.json', 'w') as f:
    json.dump(deserialized_person, f, indent=4)