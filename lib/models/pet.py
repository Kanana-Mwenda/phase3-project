from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

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