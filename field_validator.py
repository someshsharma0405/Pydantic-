from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):

    name : str 
    email: EmailStr 
    url: AnyUrl
    age : int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @field_validator('email', mode='after')
    @classmethod
    def email_validator(cls,value):
        
        valid_domains= ['hdfc.com', 'icici.com', 'axis.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):

        return value.upper()
    

def insert_patient_data(patient:patient):
    print(patient.name)
    print(patient.email)
    print(patient.url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted")


patient_info = {'name': 'somesh', 'email':'abcd@hdfc.com', 'url':'https://www.github.com', 'age': 21, 'weight':70.0, 'married':False, 'allergies':['dust','pollen','sweet'], 'contact_details':{'phone':'6232052308'}}

patient1 = patient(**patient_info)

insert_patient_data(patient1)
