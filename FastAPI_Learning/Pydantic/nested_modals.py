from pydantic import BaseModel

class Address(BaseModel):

    city:str
    state:str
    pin:str


class Patient(BaseModel):

    name:str
    gender:str
    age:int
    address : Address


address_dict = {'city':'gurgaon', 'state':'haryana', 'pin':'122001'}
address1 = Address(**address_dict)

patient_dict = {'name':'preet', 'gender':'male', 'age':35, 'address': address1}

patient1 = Patient(**patient_dict)

# print(patient1.name)
# print(patient1.address.city)

# use( include and exclude parametrs)  -> when dump
temp = patient1.model_dump()               # return python Dictionary

temp1 = patient1.model_dump_json()            # return JSON Object

print(type(temp))
print(temp)

