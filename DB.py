from constant import *
import json
fruit = ['Pomme', 'Poire', 'Prune']
quality = ['Arbre', 'Sol', 'Kiosque']

def keyFruitIndex(x):
    return {
        'Pomme':0,
        'Poire':1,
        'Prune':2
    }[x]

def keyQualityIndex(x):
    return {
        'Arbre':0,
        'Sol':1,
        'Kiosque':2
    }[x]

def keyFruitName(x):
    return {
        0:'Pomme',
        1:'Poire',
        2:'Prune'
    }[x]

def keyQualityName(x):
    return {
        0:'Arbre',
        1:'Sol',
        2:'Kiosque'
    }[x]

def writeJSON(data):
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

def getData():
    data =[]
    try :
        with open('data.txt', 'r') as json_file:
            data = json.load(json_file)
            if DEBUG_DB:
                i=0
                for c in fruit:
                    print(data[i])
                    i=i+1
    except:
        for c in fruit:
            d = {}
            d['name'] = c
            for r in quality:
                d[r] = 0.0
            data.append(d)
        writeJSON(data)
    return data
