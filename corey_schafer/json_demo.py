import json

people_json_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "345-243-542",
            "emails": ["johnsmith@gmail.com", "john.smith@wp.pl"],
            "has_license": false
        },
        {
            "name": "Adam Doe",
            "phone": "645-246-867",
            "emails": null,
            "has_license": true
        }
    ]
}    
'''

print("Zamiana jsona na słownik")
print("people_dict = json.loads(people_json_string")
people_dict = json.loads(people_json_string)

print("typem obiektu json people_json_string { } jest pythonowy słownik dict")
print("type(people_dict)", type(people_dict))
print()

print("typ tablicy json people [ ] jest pythonowa lista list")
print("type(people_dict['people'])", type(people_dict['people']))
print()

print("Cały słownik")
print(people_dict)
print()

print("Osoby:")
for person in people_dict["people"]:
    print(person)

print()

print("Imiona osób:")
for person in people_dict["people"]:
    print(person['name'])

print()

print("Zamiana słownika pythona na json string")

print("Usuwam nr telefonu ze słownika")
for person in people_dict["people"]:
    del person['phone']

print("Cały słownik bez numerów telefonów")
print(people_dict)
print()

print("Zamiana słownika bez telefonów na string. Formatowanie 2 spacje i sortowanie kluczy alfabetycznie")
print("new_json_string = json.dumps(people_dict, indent=2, sort_keys=True)")
new_json_string = json.dumps(people_dict, indent=2, sort_keys=True)
print()

print("Tak wygląda new_json_string bez numerów telefonów")
print(new_json_string)
print()

print("Otwieram plik states.json i zapisuję go do słownika data")
with open("states.json") as f:
    data = json.load(f)

print()
print("type(data)", type(data))

print()
print("Stany:")
for state in data['states']:
    print(state)

print()
print("Nazwy stanów i ich skróty:")
for state in data['states']:
    print(state['name'], state['abbreviation'])

print()
print("Usuwam area_codes ze słownika data")
for state in data['states']:
    del state['area_codes']

print()
print("Zapisuję zmieniony słownik data do nowego pliku new_states.json i daję 2 spacje w pliku")
with open("new_states.json", "w") as f:
    json.dump(data, f, indent=2)
