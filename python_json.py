import json

x = '{"name":"Tanmay","age":16,"city":"PCMC"}'

y = json.loads(x)
print(y['age'])