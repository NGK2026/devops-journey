import xml.etree.ElementTree as ET

xml_string = """<person><name>Alice Doe</name><age>30</age>
<programmer>true</programmer><car xsi:nil="true" xmlns:xsi=
"http://www.w3.org/2001/XMLSchema-instance"/><address><street>100 Larkin St.</street>
<city>San Francisco</city><zip>94102</zip>
</address><phone><phoneEntry><type>mobile</type><number>415-555-7890</number>
</phoneEntry><phoneEntry><type>work</type><number>415-555-1234</number>
</phoneEntry></phone></person>"""

root = ET.fromstring(xml_string)
print(root.tag)

print(list(root[0]))

print(root[0].tag)
print(root[0].text)

print(root[4][0].text)
print("*")

# iterate immidiate child elements
for elem in root:
    print(elem.tag, '--', elem.text)
"""
name -- Alice Doe
age -- 30
programmer -- true
car -- None
address -- None
phone -- None
"""
print("*")

# iterate over all children underneath element
for elem in root.iter():
    print(elem.tag, '--', elem.text)
"""
person -- None
name -- Alice Doe
age -- 30
programmer -- true
car -- None
address -- None
street -- 100 Larkin St.
city -- San Francisco
zip -- 94102
phone -- None
phoneEntry -- None
type -- mobile
number -- 415-555-7890
phoneEntry -- None
type -- work
number -- 415-555-1234
"""
print("*")

# iterate over only 'number' child elements of root
for elem in root.iter('number'):
    print(elem.tag, '--', elem.text)
"""
number -- 415-555-7890
number -- 415-555-1234
"""
print("*")


# convert XML to python
import xmltodict

xml_string = """<person><name>Alice Doe</name><age>30</age>
<programmer>true</programmer><car xsi:nil="true" xmlns:xsi=
"http://www.w3.org/2001/XMLSchema-instance"/><address><street>100 Larkin St.</street>
<city>San Francisco</city><zip>94102</zip>
</address><phone><phoneEntry><type>mobile</type><number>415-555-7890</number>
</phoneEntry><phoneEntry><type>work</type><number>415-555-1234</number>
</phoneEntry></phone></person>"""

python_data = xmltodict.parse(xml_string)
print(python_data)
'''
{'person': {'name': 'Alice Doe', 'age': '30', 'programmer': 'true', 'car': {'@xsi:nil': 'true', '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'}, 'address': {'street': '100 Larkin St.', 'city': 'San Francisco', 'zip': '94102'}, 'phone': {'phoneEntry': [{'type': 'mobile', 'number': '415-555-7890'}, {'type': 'work', 'number': '415-555-1234'}]}}}
'''