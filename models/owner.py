from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from models import Base

# Base = declarative_base()
engine = create_engine("sqlite:///pet_adoption.db")

Session = sessionmaker(bind=engine)
session = Session()

class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone_number = Column(String())  

    pets = relationship("Pet", back_populates="owner")

#     def __init__(self, name, email, phone_number, id=None):
#         self.id = id
#         self.name = name
#         self.email = email
#         self.phone_number = phone_number

#     def __repr__(self):
#         return f"<Owner {self.id}: {self.name}, {self.email}, {self.phone_number}>"


