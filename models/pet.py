from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,create_engine
from sqlalchemy.orm import relationship,sessionmaker
from models.owner import Base



class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    pet_type = Column(String())
    breed = Column(String())
    age = Column(Integer())
    adopted = Column(Boolean)
    owner_id = Column(Integer(),ForeignKey('owners.id'))

    owner = relationship("Owner", back_populates="pets")

    #class methods
    all = {}

    def __init__(self,name,pet_type,breed,age,adopted,owner_id,id=None):
        self.id = id
        self.name = name
        self.pet_type = pet_type
        self.breed = breed
        self.age = age
        self.adopted = adopted
        self.owner_id = owner_id

    def __repr__(self):
        return (f"<Pet {self.id}: {self.name}, {self.pet_type},{self.breed},{self.age},{self.adopted}, {self.owner_id}>")

    @property #name
    def name(self):
        self._name

    @name.setter
    def name(self,name):
        if isinstance(name,str):
            self._name = name
        else:
            raise ValueError("Name must be a string")

    @property #pettype
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self,pet_type):
        if isinstance(pet_type,str):
            self._pet_type = pet_type
        else:
            raise ValueError("Pet type must be a string")

    @property #breed
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self,breed):
        if isinstance (breed,str):
            self._breed = breed
        else:
            raise ValueError("Breed must be a string")

    @property #age
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if isinstance(age,int):
            self._age =age
        else:
            raise ValueError("Age must be an integer")

    @property #adopted
    def adopted(self):
        return self._adopted

    @adopted.setter
    def adopted(self,value):
        if isinstance(value,bool):
            self._adopted = value
        else:
            raise ValueError("Adopted status must be True or False")

    @property #owner_id
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self,owner_id):
        if isinstance(owner_id,int):
            self._owner_id = owner_id
        else:
            raise ValueError("owner_id must refer to an owner in the database")
@classmethod
def get_all(cls):
    pass
    
@classmethod
def find_by_id(cls,id):
    pass

@classmethod
def find_by_pet_type(cls,pet_type):
    pass

@classmethod
def create():
    pass

@classmethod
def update():
    pass

@classmethod
def delete():
    pass