from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,create_engine
from sqlalchemy.orm import relationship,sessionmaker, declarative_base
from models import Base

# Base = declarative_base()
engine = create_engine("sqlite:///pet_adoption.db")

Session = sessionmaker(bind=engine)
session = Session()

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    pet_type = Column(String())
    breed = Column(String())
    age = Column(Integer())
    gender = Column(String())
    adopted = Column(Boolean)
    owner_id = Column(Integer(),ForeignKey('owners.id'))

    owner = relationship("Owner", back_populates="pets")

    #class methods
    #all = {}

    # def __init__(self,name,pet_type,breed,age,gender,adopted,owner_id,id=None):
    #     self.id = id
    #     self.name = name
    #     self.pet_type = pet_type
    #     self.breed = breed
    #     self.age = age
    #     self.gender = gender
    #     self.adopted = adopted
    #     self.owner_id = owner_id

    def __repr__(self):
        return (f"<Pet {self.id}: {self.name}, {self.pet_type},{self.breed},{self.age},{self.adopted}, {self.owner_id}>")


