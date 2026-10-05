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

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pincode)
print(patient1.age)