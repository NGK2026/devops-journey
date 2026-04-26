import json

python_data = {
    "name": "Alice Doe", 
    "age": 30, 
    "car": None, # py not js null
    "programmer": True, # py not js true
    "address": {
        "street": "100 Larkin St.", 
        "city": "San Francisco", 
        "zip":"94102"
    },
    "phone": [
        {"type": "mobile", "number": "415-555-7890"}, 
        {"type": "work", "number": "415-555-1234"}
    ]
}

json_string = json.dumps(python_data)

print(json_string)
"""
{"name": "Alice Doe", "age": 30, "car": null, "programmer": true, "address": {"street": "100 Larkin St.", "city": "San Francisco", "zip": "94102"}, "phone": [{"type": "mobile", "number": "415-555-7890"}, {"type": "work", "number": "415-555-1234"}]}
"""
print()

json_string = json.dumps(python_data, indent=2)
print(json_string)
'''
{
  "name": "Alice Doe",
  "age": 30,
  "car": null,
  "programmer": true,
  "address": {
    "street": "100 Larkin St.",
    "city": "San Francisco",
    "zip": "94102"
  },
  "phone": [
    {
      "type": "mobile",
      "number": "415-555-7890"
    },
    {
      "type": "work",
      "number": "415-555-1234"
    }
  ]
}
'''