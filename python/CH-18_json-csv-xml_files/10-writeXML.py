import xml.etree.ElementTree as ET

person = ET.Element('person')  # Create the root XML element.
name = ET.SubElement(person, 'name')  # Create <name> and put it under <person>.
name.text = 'Alice Doe'  # Set the text between <name> and </name>.
age = ET.SubElement(person, 'age')
age.text = '30'  # XML content is always a string.
programmer = ET.SubElement(person, 'programmer')
programmer.text = 'true'
car = ET.SubElement(person, 'car')
car.set('xsi:nil', 'true')
car.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
address = ET.SubElement(person, 'address')
street = ET.SubElement(address, 'street')
street.text = '100 Larkin St.'

print(ET.tostring(person, encoding='utf-8').decode('utf-8'))
'''
<person><name>Alice Doe</name><age>30</age><programmer>true</programmer><car xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" /><address><street>100 Larkin St.</street></address></person>
'''