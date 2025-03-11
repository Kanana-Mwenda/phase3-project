from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone_number = Column(Integer())

    pets = relationship("Pet", back_populates="owner")

#class methods
    all = {}

    def __init__(self,name,email,phone_number,id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return f"<Owner {self.id}: {self.name}, {self.email}, {self.phone_number}>"

    @property #name
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance(name,str):
            self._name = name
        else:
            raise ValueError("Name must be a string")
    
    @property #email
    def email(self):
        return self._email

    @email.setter
    def email(self,email):
        if isinstance (email,string):
            self._email = email
        else:
            raise ValueError("Name must be a string")

    @property #phone_no
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self,phone_number):
        if isinstance(phone_number,int):
            self._phone_number = phone_number
        else:
            raise ValueError("Phone number must be an integer")

    