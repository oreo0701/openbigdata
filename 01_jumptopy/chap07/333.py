from xml.etree.ElementTree import parse

tree = parse("note2.xml")
note = tree.getroot()

childs = note.getiterator()
childs = note.getchildren()

childs = note.getiterator()
childs = note.getchildren()

# for child in note.iter():
#     print(child.attrib)

from_tag = note.find("from")
for student in from_tag.iter():
    print(student.attrib)

print("end")