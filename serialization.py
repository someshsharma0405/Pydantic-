from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pincode : int

class patient(BaseModel):
    name : str
    gender : str
    age : int
    address : Address

address_dict = {'city': 'noida', 'state': 'uttarpradesh', 'pincode': 201310}

address1 = Address(**address_dict)

patient_dict = {'name': 'somesh', 'gender': 'male', 'age':21, 'address': address1}

patient1 = patient(**patient_dict)

dict_export = patient1.model_dump(include=['name','gender','age']) # we can pass arguments here also to control some operations like include , exclude , exclude unset etc
json_export = patient1.model_dump_json(exclude={'address':['city']}) # exclude_unsest = either True or False if used 


print(dict_export)
print(type(dict_export))

print(json_export)
print(type(json_export))