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

    def __repr__(self):
        return f"<Owner {self.id}: {self.name}, {self.email}, {self.phone_number}>"

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, owner_id):
        return session.query(cls).filter_by(id=owner_id).first()

    @classmethod
    def find_by_name(cls,name):
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def create(cls,name,email,phone_number):
        owner = cls(name=name,email=email,phone_number=phone_number)
        session.add(owner)
        session.commit()
        return owner

    @classmethod
    def update(cls,id,name=None,email=None,phone_number=None):
        owner = cls.find_by_id(id)
        if owner:
            if name:
                owner.name = name
            if email:
                owner.email = email
            if phone_number:
                owner.phone_number = phone_number
            session.commit()
            return owner

    @classmethod
    def delete(cls,id):
        owner = cls.find_by_id(id)
        if owner:
            session.delete(owner)
            session.commit()
            return owner
            