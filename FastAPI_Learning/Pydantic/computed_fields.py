from pydantic import (
    BaseModel,
    EmailStr,
    AnyUrl,
    Field,
    field_validator,
    model_validator,
    computed_field
)
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    # name: str = Field(max_length=50)
    name: str
    age: int
    email: EmailStr
    weigth: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def caluclated_bmi(self) -> float:
        bmi = round(self.weigth / (self.age**2),2)
        return bmi


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weigth)
    print(patient.allergies)
    print(patient.married)
    print(patient.contact_details)
    print(patient.email)
    print('BMI',patient.caluclated_bmi)
    print("Inserted")


patient_info = {
    "name": "nitish",
    "email": "example@icici.com",
    "age": 61,
    "weigth": 75.0,
    "allergies": ["pollen", "dust"],
    "married": True,
    "contact_details": {
        "email": "example@gmail.com",
        "phone": "741252588963",
        "emergency": "1235469",
    },
    'height':1.78
}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)
