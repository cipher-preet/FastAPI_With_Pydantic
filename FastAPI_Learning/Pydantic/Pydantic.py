from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    # name: str = Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title='name of the patient', description='Give the name of th patient in less than 50 chars', example=["pankaj", "preet"])] 
    age: int
    email:EmailStr
    weigth:float = Field(gt=0,lt=100, strict=True)
    married: Annotated[bool, Field(default=None, description="Is the patient married or not")]
    allergies : Optional[List[str]] = None
    contact_details: Dict[str,str]


def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weigth)
    print(patient.allergies)
    print(patient.married)
    print(patient.contact_details)
    print(patient.email)
    print("Inserted")


patient_info = {'name': 'nitish', 'email':'example@gmail.com','age': 30,'weigth':75.0, 'allergies' : ['pollen','dust'] , 'married': True, 'contact_details':{'email':'example@gmail.com','phone':'741252588963'}}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)

