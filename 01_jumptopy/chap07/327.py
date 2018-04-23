from xml.etree.ElementTree import Element,SubElement,dump, ElementTree

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "from").text = "Jani"

dummy = Element("dummy")
note.insert(1, dummy)
#<dummy />    : 혼자 열고 닫기 다 함
note.remove(dummy)

note.attrib["data"] = "20120104"




dump(note)
ElementTree(note).write("note.xml")