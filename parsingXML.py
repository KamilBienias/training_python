import xml.etree.cElementTree as ET

try:
    tree = ET.parse("people.xml")
except FileNotFoundError:
    print("Plik nie istnieje")
    new_base = open("people.xml", "w")
    new_base.close()
    tree = ET.parse("people.xml")
    # exit()
root = tree.getroot()  # tak dostaję najbardziej zewnętrzny tag (w tym wypadku people)
print("Nazwa tagu people:")
print(root.tag)
print("Słownik atrybutów tagu people:")
print(root.attrib)

print("Nazwy tagów bezpośrednich dzieci i ich atrybuty")
for child in root:
    print(child.tag, child.attrib)

print("Nazwisko pierwszej osoby:")
print(root[0][1].text)

print("Nazwiska wszystkich osób:")
for nazwisko in root.iter('lastName'):
    print(nazwisko.text)

print("Imiona i nazwiska wszystkich osób:")
for person in root:
    for elements in person:
        print(elements.text)

print("Inny sposób na nazwiska wszystkich osób:")
for person in root:
    for nazwisko in person.iter('lastName'):
        print(nazwisko.text)

print("Zmieniam lastName dla person id=1")
root[0][1].text = "Bond"

print("Nazwisko pierwszej osoby:")
print(root[0][1].text)

#zapis do pliku
tree.write("people.xml")  # ścieżka względna

# tak robię stringa z pliku xml
# xml_as_string = ""
#
# with open("people.xml") as file:
#     for line in file:
#         # print(line.strip().split()) # nie trzeba
#         # line = line.strip() # nie trzeba
#         # print(line, end="\n") # nie trzeba
#         # print(line) # nie trzeba
#         xml_as_string += line
#
# print(xml_as_string)
# print(type(xml_as_string))
#
# tree = ET.fromstring(xml_as_string)

# data = '''
# <people>
#     <person id="1">
#         <firstName>name1</firstName>
#         <lastName>surname1</lastName>
#     </person>
# </people>
# '''
#
# tree = ET.fromstring(data)
# print(type(tree.find('person/lastName').text))
# print("Name:" + tree.find('person/lastName').text)