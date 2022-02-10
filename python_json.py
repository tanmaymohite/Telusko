import json

x = '{"name":"Tanmay","age":16,"city":"pcmc","div":"L1","college":"GPP","place":"shivajinagar","district":"pune"}'

y = json.loads(x)

print(y["name"])