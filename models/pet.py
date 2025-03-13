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
    owner_id = Column(Integer(),ForeignKey('owners.id'),nullable=True)

    owner = relationship("Owner", back_populates="pets")

    def __repr__(self):
        return (f"<Pet {self.id}: {self.name}, {self.pet_type},{self.breed},{self.age},{self.adopted}, {self.owner_id}>")
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls,id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_pet_type(cls,pet_type):
        return session.query(cls).filter_by(pet_type=pet_type).all()

    @classmethod
    def create(cls,name,pet_type,breed,age,adopted,owner_id):
        adopted = bool(adopted)
        pet = cls(name=name,pet_type=pet_type,breed=breed,age=age,adopted=bool(adopted),owner_id=owner_id)
        session.add(pet)
        session.commit()
        return pet 

    @classmethod
    def update(cls,id,name,pet_type,breed,age,adopted,owner_id):
        pet = cls.find_by_id(id)
        if pet:
            if name:
                pet.name = name
            if pet_type:
                pet.pet_type = pet_type
            if breed:
                pet.breed = breed
            if age:
                pet.age = age
            if adopted:
                pet.adopted = adopted
            if owner_id:
                pet.owner_id = owner_id
            session.commit()
            return pet
    @classmethod
    def delete(cls,id):
        pet = cls.find_by_id(id)
        if pet:
            session.delete(pet)
            session.commit()
            return pet 



