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


