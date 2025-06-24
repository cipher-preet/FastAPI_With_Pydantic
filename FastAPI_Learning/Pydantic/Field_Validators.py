from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    # name: str = Field(max_length=50)
    name:str
    age: int
    email:EmailStr
    weigth:float
    married: bool
    allergies : List[str]
    contact_details: Dict[str,str]

    # add validator accourding to buisness logic
    @field_validator('email', mode='before')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com','icici.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid Domaim')
        return value 




def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weigth)
    print(patient.allergies)
    print(patient.married)
    print(patient.contact_details)
    print(patient.email)
    print("Inserted")


patient_info = {'name': 'nitish', 'email':'example@icici.com','age': 30,'weigth':75.0, 'allergies' : ['pollen','dust'] , 'married': True, 'contact_details':{'email':'example@gmail.com','phone':'741252588963'}}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)

