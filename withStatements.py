import json

dictionary = {"a": "1", "b": "2"}
with open('example.json', 'w') as file:
    file.write(json.dumps(dictionary))

with open('example.json', 'r') as file:
    read_file = file.read()
    output_file = json.loads(read_file)

print(output_file)
