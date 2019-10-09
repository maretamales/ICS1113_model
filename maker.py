import json
from random import randint


with open("parameters.json", "r", encoding="utf-8") as file:
    params = json.load(file)

aux = {
    "i": "I",
    "j": "J",
    "l": "L",
    "k": "K",
    "t": "T"
}

aux3 = {
    "s": [400, 500],
    "d": [200, 400],
    "q": [1000, 1500],
    "p": [5000, 150000],
    "e": [500, 5000],
    "n": [1000, 10000],
    "m": [1000, 10000],
    "l": [50, 100],
    "u": [200, 300],
    "beta": [2000, 3000]
}

aux2 = {
    "s": ["i"],
    "d": ["l", "j", "t"],
    "q": ["k"],
    "p": ["l", "i"],
    "e": ["l", "k"],
    "n": ["l", "k", "j"],
    "m": ["l", "i", "k"],
    "l": ["k"],
    "u": ["k"],
    "beta": ["k", "l"]
}



sets = params["sets"]
params = params["params"]

for p in params:
    index = aux2[p]

    a_dict = dict()
    i = index[0]
    for n1 in range(sets[aux[i]]):
        if len(index) > 1:
            i2 = index[1]
            a_dict_2 = dict()
            for n2 in range(sets[aux[i2]]):
                if len(index) > 2:
                    i3 = index[2]
                    a_dict_3 = dict()
                    for n3 in range(sets[aux[i3]]):
                        a_dict_3[n3] = randint(aux3[p][0], aux3[p][1])
                    a_dict_2[n2] = a_dict_3
                else:
                    a_dict_2[n2] = randint(aux3[p][0], aux3[p][1])
            a_dict[n1] = a_dict_2
        else:
            a_dict[n1] = randint(aux3[p][0], aux3[p][1])
    params[p] = a_dict

with open("parameters.json", "w", encoding="utf-8") as file:
    json.dump({"sets": sets, "params": params}, file)

    