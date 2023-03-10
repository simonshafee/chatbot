import json
import os

with open('in.json') as file:
    data = json.load(file)
    print(data)