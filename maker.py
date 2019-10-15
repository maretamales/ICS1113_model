import json
from random import randint


def generate_data():
    sets = {
            "I": 3,
            "L": 10,
            "J": 2,
            "K": 1,
            "T": 31
        }

    aux = {
        "i": "I",
        "j": "J",
        "l": "L",
        "k": "K",
        "t": "T"
    }

    aux3 = {
        "s": [5000, 10000],
        "d": [100, 200],
        "q": [150000, 200000],
        "p": [5000, 150000],
        "e": [500, 5000],
        "n": [1000, 10000],
        "m": [1000, 10000],
        "l": [50, 100],
        "u": [2000, 3000],
        "beta": [500, 1000],
        "c":[10000,12500]
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
        "beta": ["k", "l"],
        "c":["l","k"]
    }

    params = dict()

    for p in aux2:
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
    
    print("="*10, "  DATA CREATED  ", "="*10)


def load_data():

    aux = {
        "s": 1,
        "d": 3,
        "q": 1,
        "p": 2,
        "e": 2,
        "n": 3,
        "m": 3,
        "l": 1,
        "u": 1,
        "beta": 2,
        "c": 2
    }

    with open("parameters.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    sets = data["sets"]
    params = data["params"]
    new_params = dict()
    for p in params:
        values = dict()
        for i in params[p]:
            if aux[p] > 1:
                param1 = params[p][i]
                for j in param1:
                    if aux[p] > 2:
                        param2 = params[p][i][j]
                        for k in param2:
                            tup = (int(i), int(j), int(k))
                            values[tup] = param2[k]
                    else:
                        tup = (int(i), int(j))
                        values[tup] = param1[j]
            else:
                tup = (int(i))
                values[tup] = params[p][i]
        new_params[p] = values
    
    return sets, new_params


if "__main__" == __name__:
    generate_data()
