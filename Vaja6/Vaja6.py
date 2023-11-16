import requests
import json

def getBlock(blockNum = "latest"):
    # definiraj VARIABLE nase skripte
    API = "https://mainnet.infura.io/v3/8891db36a05f485486fd7979445d5611"

        # JSON-RPC request payload  (pogledamo dokumentacijo!)
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [blockNum,True],
        "id": 0
        }

        # Nastavimo headerje za JSON-RPC request
    header = {
            "Content-Type": "application/json",
            
        }

    # Pošljemo request (uporabimo requests.post mdetodo)
    response = requests.post(API, data = json.dumps(payload), headers=header)

    # Error handling. POgledamo če smo dobili pravilen odgovor.
        # ce ni error-ja (status code 200) sprintamo sporocilo in shranimo dobljeno sporocilo v json

        # else, sprintaj sporocilo da nam ni uspelo dobiti zadnji block in dodaj kateri error oz. code-status code smo dobili

    if response.status_code == 200:
        if blockNum == "latest":
            print("Dobili smo zadnji block!")
            with open(f'Vaja6/DATA/zadnjiBlock.json', 'w') as f:
                json.dump(response.json(), f, indent=4)
        else:
            print(f"Dobili smo  block{response.json()["result"]["number"]}!")
            with open(f'Vaja6/DATA/Block{response.json()["result"]["number"]}.json', 'w') as f:
                json.dump(response.json(), f, indent=4)
        return response.json()
        

    else:
        print("Nismo dobili zadnjega blocka!")
        print("Error code: " + str(response.status_code))
        print("Error message: " + response.text)
        exit(1)
    return None

def prestejTranzakcije(blockNum = "latest"):

    # naredimo kopijo podatkov - .copy() metoda
    data = getBlock(blockNum).copy()

    # definiramo counter
    counter = 0

    # Iteriramo čez transakcije in povečujemo counter
    for transaction in data["result"]["transactions"]:
        counter += 1

    # Izpišemo/sprintamo counter (število transakcij)
    return counter




def izlusciNaslove(blockNum = "latest"):
    # naredimo kopijo podatkov - .copy() metoda
    data = getBlock(blockNum).copy()

    # definiramo dictionary za shranjevanje naslovov
    podatki = dict(od = [], to = [])

    # iteriramo čez transakcije in izluščimo naslove (.get("from")   .get("to")) in jih shranimo v dictionary
    for transaction in data["result"]["transactions"]:
        podatki["od"].append(transaction.get("from"))
        podatki["to"].append(transaction.get("to"))

    return podatki

def main():
    print(f"Zadnji block: {getBlock()}")
    print(f"Število transakcij v zadnjem blocku: {prestejTranzakcije()}")
    print("\n\n\n\n")
    #print(f"Naslovi v zadnjem blocku: {izlusciNaslove()}")

main()