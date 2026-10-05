from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):

    name : str 
    email: EmailStr 
    url: AnyUrl
    age : int
    weight: float #kg
    height: float #meter
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def insert_patient_data(patient:patient):
    print(patient.name)
    print(patient.email)
    print(patient.url)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print('BMI',patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted")


patient_info = {'name': 'somesh', 'email':'abcd@hdfc.com', 'url':'https://www.github.com', 'age': 71, 'weight':70.0, 'height':1.778, 'married':False, 'allergies':['dust','pollen','sweet'], 'contact_details':{'phone':'6232052308', 'emergency':'9305187808'}}

patient1 = patient(**patient_info)

insert_patient_data(patient1)
