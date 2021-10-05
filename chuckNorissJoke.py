import requests
import json


def chuck():
    f = r"http://api.icndb.com/jokes/random"
    data = requests.get(f)
    tt = json.loads(data.text)
    print(tt["value"]["joke"])


chuck()


def chuck5():
    f = r"http://api.icndb.com/jokes/random/5"
    data = requests.get(f)
    tt = json.loads(data.text)
    values = tt["value"]
    for value in values:
        print(value["joke"])

chuck5()