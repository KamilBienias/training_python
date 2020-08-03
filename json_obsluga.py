import json

my_dictionary = {"name": "John", "salary": 1280, "bonus": True}
print(my_dictionary)

file_name = "my_database.txt"

print("Writing json to a file")
with open(file_name, 'w') as f:
    json.dump(my_dictionary, f)  # zapis my_dictionary do pliku f

print("Reading json from a file")
with open(file_name) as f:
    loaded_dictionary = json.load(f)  # załadowanie zawartości pliku f do loaded_dictionary

print("Printing loaded_dictionary")
for key in loaded_dictionary:
    print(key, loaded_dictionary[key])

print("Second way")
print(loaded_dictionary)

print("Writing dictionary to json_string")
json_string = json.dumps(my_dictionary, indent=4)  # wcięcie ma 4 spacje

print("Dictionary saved as json_string")
print(json_string)

print("Writing json_string to dictionary")
dictionary_from_json = json.loads(json_string)

print("json_string saved as dictionary")
print(dictionary_from_json)
