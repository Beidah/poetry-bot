import json
import os

resource_folder = "res/"

chain = {}


def generate_trigram(words):
    if len(words) < 3:
        return
    for i, word in enumerate(words[:-2]):
        yield (word, words[i + 1], words[i + 2])


def create_chain():
    chain = {}
    words = []
    for filename in os.listdir(resource_folder):
        file = open(os.path.join(resource_folder, filename))
        # lines = file.readline()
        for line in file:
            words += line.split(" ")

    for word1, word2, word3 in generate_trigram(words):
        key = (word1, word2)
        if key in chain:
            chain[key].append(word3)
        else:
            chain[key] = [word3]

    return chain


def load_chain(fh):
    data = json.load(fh)
    dic = json.loads(data)
    k = dic.keys()
    v = dic.values()
    k1 = [eval(i) for i in k]
    return dict(zip(*[k1, v]))


def get_chain():
    chain = {}
    if os.path.isfile("chain.json"):
        with open("chain.json", 'r') as fh:
            chain = load_chain(fh)
    else:
        chain = create_chain()

        with open('chain.json', 'w') as outfile:
            k = chain.keys()
            v = chain.values()
            j_keys = [str(i) for i in k]
            json.dump(json.dumps(
                dict(zip(*[j_keys, v]))), outfile, indent=4, sort_keys=True)

    return chain
