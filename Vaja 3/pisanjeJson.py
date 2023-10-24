import json

person = {
  "name" : "Alice",
  "age" : 30,
  "address":{
      "street" : "dunajska",
      "city" : "Ljubljana",
  },
  "married" : True
}

with open('/Users/brinsoko/Documents/TP/VAJE/Vaja 3/VAJE/VAJE-3/DATA/person.json', 'w') as f:
    json.dump(person, f, indent=4, sort_keys=False)