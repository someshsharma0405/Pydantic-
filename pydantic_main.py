from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):

    name : str = Field(max_length=10) # Field function allows us to apply custom data validation. Field function with Annotated we can provide metadata to it .Also can add default value with both of this things
    email: EmailStr 
    url: AnyUrl
    age : Annotated[int, Field(gt=16, lt=80, strict=True)]
    weight: float = Field(gt=0, lt=100)
    married: Annotated[Optional[bool], Field(default=None, description='Is the patient married or not')]
    allergies: List[str]
    contact_details: Dict[str,str]

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


patient_info = {'name': 'somesh', 'email':'abcd@gmail.com', 'url':'https://www.github.com', 'age': 21, 'weight':70.0, 'married':False, 'allergies':['dust','pollen','sweet'], 'contact_details':{'phone':'6232052308'}}

patient1 = patient(**patient_info)

insert_patient_data(patient1)
