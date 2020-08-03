# youtube https://www.youtube.com/watch?v=7BtLtBqO9s0
import xml.etree.cElementTree as ETXML  # cElementTree jest szybsze niż ElementTree, bo korzysta z języka C

root = ETXML.Element("root")  # create root element
root.set("attribute_name", "attribute_value")  # sam dodałem ten atrybut
sub = ETXML.SubElement(root, "sub")  # create sub under root

ETXML.SubElement(sub, "sub1", name="sub1_name", category="CAT_A").text = "Sub_1"  # create sub1 and sub2 under sub
ETXML.SubElement(sub, "sub2", name="sub2_name", category="CAT_B").text = "Sub_2"

header = ETXML.SubElement(sub, "header")  # create header under sub
ETXML.SubElement(header, "head1", name="header1").text = "Header_1 content"  # create head1 and head2 under header
ETXML.SubElement(header, "head2", name="header2").text = "Header_2 content"

body = ETXML.SubElement(sub, "body")  # create body under sub

values = ETXML.SubElement(body, "values")  # create values under body
for x in range(0,4):
    ETXML.SubElement(values, "value", name="val"+str(x), type="string").text = "value_" + str(x) + " content"  # create value under values

items = ETXML.SubElement(body, "items")  # create items under body
for y in range(0,3):
    ETXML.SubElement(items, "item", name="it"+str(y), type="int").text = str(y)  # create item under items

rootWrite = ETXML.ElementTree(root)
rootWrite.write("create.xml")