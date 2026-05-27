import json, pprint

"""
json_string = '{"name": "Alice Doe", "age": 30, "car": null, "programmer":
 true, "address": {"street": "100 Larkin St.", "city": "San Francisco", "zip":
 "94102"}, "phone": [{"type": "mobile", "number": "415-555-7890"}, {"type": 
"work", "number": "415-555-1234"}]}'
"""

json_string = '''{
    "name": "Alice Doe", 
    "age": 30, 
    "car": null, 
    "programmer": true, 
    "address": {
        "street": "100 Larkin St.", 
        "city": "San Francisco", 
        "zip":"94102"
    },
    "phone": [
    {"type": "mobile", "number": "415-555-7890"}, 
    {"type": "work", "number": "415-555-1234"}
    ]
}'''

python_data = json.loads(json_string)

print(python_data)