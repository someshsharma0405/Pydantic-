from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
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

    @model_validator(mode='after')
    def check_emergency_contact(model): 

        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient above age of 60 must have a emergency contact')
        return model

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


patient_info = {'name': 'somesh', 'email':'abcd@hdfc.com', 'url':'https://www.github.com', 'age': 71, 'weight':70.0, 'married':False, 'allergies':['dust','pollen','sweet'], 'contact_details':{'phone':'6232052308', 'emergency':'9305187808'}}

patient1 = patient(**patient_info)

insert_patient_data(patient1)
