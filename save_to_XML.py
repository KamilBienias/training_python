# youtube https://www.youtube.com/watch?v=OAfeQuNhcps

import xml.etree.cElementTree as ET

root = ET.Element('people')

# person = ET.Element('person')
# person.set('id', '007')  # ustawiam artybut dla tagu person
# root.append(person)
# first_name = ET.Element('firstName')
# person.append(first_name)
# first_name.text = 'James'
# last_name = ET.Element('lastName')
# person.append(last_name)
# last_name.text = 'Bond'
for i in range(1, 4):
    person = ET.Element('person')
    person.set('id', str(i))  # ustawiam artybut dla tagu person
    root.append(person)
    first_name = ET.Element('firstName')
    person.append(first_name)
    first_name.text = 'name' + str(i)
    last_name = ET.Element('lastName')
    person.append(last_name)
    last_name.text = 'surname' + str(i)

print(ET.tostring(root))

#zapis do pliku
tree = ET.ElementTree(root)
tree.write("people.xml")  # ścieżka względna
# rootWrite.write(r"C:\Users\dom\PycharmProjects\person.xml")  # ścieżka bezwzględna działa


