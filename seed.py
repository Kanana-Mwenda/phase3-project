from faker import Faker
from models import Owner,Pet
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import random

my_engine = create_engine("sqlite:///pet_adoption.db")
session_inst = sessionmaker(bind=my_engine)
my_session = session_inst()

fake = Faker()

# Dictionary of pet types and their corresponding breeds
breeds = {
    "Dog": ["Labrador", "Golden Retriever", "Bulldog"],
    "Cat": ["Persian", "Siamese", "Bengal"],
    "Fish": ["Goldfish"],
    "Bird": ["Parrot", "Finch", "Macaw"]
}

#owners
print("Start seeding owners")
owners_list=[]
for i in range(10):
    new_owner = Owner(name=fake.name(),email=fake.email(),phone_number=fake.phone_number())
    owners_list.append(new_owner)

my_session.add_all(owners_list)
my_session.commit()
print("Successfully seeded owners")

#pets  
print("Start seeding pets")
pets_list=[]
for i in range(20):
    pet_type=random.choice(["Dog","Cat","Fish","Bird"])
    adopted=bool(random.choice([True,False]))
    owner_id=random.choice([owner.id for owner in owners_list]) if adopted else None

    new_pet = Pet(
    name=fake.first_name(),
    pet_type=pet_type,
    breed=random.choice(breeds[pet_type]),
    age=random.randint(0,20),
    gender=random.choice(["Male", "Female"]),
    adopted = adopted,
    owner_id= owner_id
    )
    pets_list.append(new_pet)

my_session.add_all(pets_list)
my_session.commit()
print("Successfully seeded pets")

# # Clear existing data before seeding new data
# my_session.query(Pet).delete()
# my_session.query(Owner).delete()
# my_session.commit()
# print("Cleared existing data successfully.")
