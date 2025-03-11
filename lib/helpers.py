from models.owner import Owner
from models.pet import Pet

def exit_program():
    print("Goodbye!")
    exit()

def list_owners():
    owners = Owner.get_all()
    for owner in owners:
        print(owner)

 def find_owner_by_id():
    id = input("Enter the owner's id:")  
    owner = Owner.find_by_id(id)
    if owner:
        print(owner)
    else:
        print(f"Owner {id} not found")

def find_owner_by_name():
    name = input("Enter the owner's name:")
    owner = Owner.find_by_name(name)
    if owner:
        print (owner)
    else:
        print(f"Owner {name} not found")

def create_owner():
    name = input("Enter the owner's name: ")
    email = input("Enter the owner's email:")
    phone_number= input("Enter the owner's phone number:")
    try:
        owner = Owner.create(name,email,phone_number)
        print(f"Successfully created {owner}")
    except Exception as exc:
        print("Error creating owner:",exc)

def update_owner():
    id = input("Enter the owner's id:")
    owner = Owner.find_by_id(id)
    if owner:
        try:
            name = input("Enter the owner's new name:")
            email = input("Enter the owner's new email:")
            phone_number = input("Enter the owner's new phone number:")
  
            owner.update()
            print(f"Successfully updated {owner}")

        except Exception as exc:
            print("Error updating owner:", exc)
    else:
        print(f"Owner {id} not found")

def delete_owner():
    id = input("Enter the owner's id:")
    owner = Owner.find_by_id(id)
    if owner:
        owner.delete()
        print(f"Owner {id} deleted")
    else:
        print("Owner {id} not found")

def list_owner_pets():
    id = input("Enter the owner's id:")
    owner = Owner.find_by_id(id)
    if owner:
        print(owner.pets())
    else:
        print(f"Owner {id} not found")

def list_pets():
    pets = Pet.get_all()
    for pet in pets:
        print(pet)

def find_pet_by_id():
    id = input("Enter the pet's id:")
    pets = Pet.find_by_id(id)
    if pet:
        print(pet)
    else:
        print(f"Pet {id} not found")

def find_pet_by_pet_type():
    pet_type = input("Enter the pet type:")
    pets = Pet.find_by_pet_type(pet_type)
    if pet:
        print(pet)
    else:
        print(f"Pet with {pet_type} not found")

def create_pet():
    name = input("Enter the pet's name:")
    pet_type = input("Enter the pet's type:")
    breed = input("Enter the pet's breed:")
    age = input("Enter the pet's age:")
    adopted = input("Enter the pet's adopted status:")
    owner_id = input("Enter the pet's owner id:")
    try:
        pet = Pet.create(name,pet_type,breed,age,adopted,owner_id)
        print(f"Successfully created {pet}")
    except Exception as exc:
        print("Error creating pet:",exc)

