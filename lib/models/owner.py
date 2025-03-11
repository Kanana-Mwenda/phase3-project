from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone_number = Column(Integer())

    pets = relationship("Pet", back_populates="owner")