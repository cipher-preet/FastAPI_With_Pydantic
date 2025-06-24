from pydantic import (
    BaseModel,
    EmailStr,
    AnyUrl,
    Field,
    field_validator,
    model_validator,
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

    # add validator accourding to buisness logic
    @field_validator("email", mode="before")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]

        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid Domaim")
        return value

    # model validator apply custom buisness Logic
    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return model


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weigth)
    print(patient.allergies)
    print(patient.married)
    print(patient.contact_details)
    print(patient.email)
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
}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)
