prvo = int(input("Vpisite 1. stevilo"))
drugo = int(input("Vpisite 2. stevilo"))
tretje = int(input("Vpisite 3. stevilo"))

print(prvo, type(prvo), "\n", drugo, type(drugo), "\n", tretje, type(tretje))

if prvo == drugo and tretje <= prvo:
    print("Prvi dve števili sta enaki in tretje je manjše ali enako številu")

else:
    print("Pogoj ni izpolnjen")