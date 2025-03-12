from faker import faker
from models import Owner,engine
from sqlalchemy.orm import sessionmaker

session_inst = sessionmaker(bind=engine)
my_session = session_inst()

fake = Faker()

print("Start seeding owners")
owners_list=[]
for i in range(10):
    new_owner = Owner(name=fake.name(),email=fake.email)
my_session.add(my_session)
my_session.commit()