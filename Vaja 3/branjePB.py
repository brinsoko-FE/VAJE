import person_pb2

person = person_pb2.Person()

# Deserialize from file
with open("/Users/brinsoko/Documents/TP/VAJE/Vaja 3/VAJE/VAJE-3/DATA/person.pb", "rb") as f:
    person.ParseFromString(f.read())

# Manipulate the data (e.g., change age and married status)
person.age = 31
person.married = False

# Serialize back to file
with open("/Users/brinsoko/Documents/TP/VAJE/Vaja 3/VAJE/VAJE-3/DATA/updatedPerson.pb", "wb") as f:
    f.write(person.SerializeToString())

# Print person object
print(person)