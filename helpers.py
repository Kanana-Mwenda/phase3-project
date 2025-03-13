from models.owner import Owner
from models.pet import Pet

def exit_program():
    print("Goodbye!")
    exit()

def view_owners():
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
    name = input("Enter the owner's new name:")
    email = input("Enter the owner's new email:")
    phone_number = input("Enter the owner's new phone number:")

    updated_owner= Owner.update(id,name,email,phone_number)
    if updated_owner:       
        print(f"Successfully updated {updated_owner}")
    else:
        print(f"Owner {id} not found")

def delete_owner():
    id = input("Enter the owner's id:")
    deleted_owner = Owner.delete(id)
    if deleted_owner:
        print(f"Successfully deleted {deleted_owner}")
    else:
        print(f"Owner {id} not found")

def view_owner_pets():
    id = input("Enter the owner's id:")
    owner = Owner.find_by_id(id)
    if owner:
        print(owner.pets())
    else:
        print(f"Owner {id} not found")

def view_pets():
    pets = Pet.get_all()
    for pet in pets:
        print(pet)

def find_pet_by_id():
    id = input("Enter the pet's id:")
    pet = Pet.find_by_id(id)
    if pet:
        print(pet)
    else:
        print(f"Pet {id} not found")

def find_pet_by_pet_type():
    pet_type = input("Enter the pet type:")
    pets = Pet.find_by_pet_type(pet_type)
    if pets:
        for pet in pets:
            print(f"ID: {pet.id}, Name: {pet.name}, Breed: {pet.breed}, Age: {pet.age}, Adopted: {pet.adopted}")
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
    
def update_pet():
    id = input("Enter the pet's id:")
    name = input("Enter the pet's name:")
    pet_type = input("Enter the pet's type:")
    breed = input("Enter the pet's breed:")
    age = input("Enter the pet's age:")
    adopted = input("Enter the pet's adopted status:")
    owner_id = input("Enter the pet's owner id:")

    pet = Pet.find_by_id(id)
    updated_pet = Pet.update(id,)
    if updated_pet:
        print(f"Successfully updated {updated_pet}")
    else:
        print("Pet {id} not found")

def delete_pet():
    id = input("Enter the pet's id")
    deleted_pet= Pet.delete(id)
    if deleted_pet:
        print(f"Successfully deleted {deleted_pet}")
    else:
        print("Pet {id} not found")


def view_owner_pets():
    id = input("Enter the owner's id:")
    owner = Owner.find_by_id(id)
    if owner:
        if owner.pets:
            print(f"Pets owned by {owner.name}:")
        for pet in owner.pets:
            print(pet)
    else:
        print(f"Owner {id} not found")
                    
