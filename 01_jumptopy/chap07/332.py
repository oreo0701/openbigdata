from xml.etree.ElementTree import parse

tree = parse("note2.xml")
note = tree.getroot()

print(note.get("date"))
print(note.get("foo", "default"))
print(note.keys())
print(note.items())

from_tag = note.find("from")
from_tags = note.findall("from")
from_text = note.findtext("from")
print("end")