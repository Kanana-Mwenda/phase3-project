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
            owner.name = name
            email = input("Enter the owner's new email:")
            owner.email = email
            phone_number = input("Enter the owner's new phone number:")
            owner.phone_number = phone_number

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

def update_pet():
    id = input("Enter the pet's id")
    pet = Pet.find_by_id(id)
    if pet:
        try:
            name = input("Enter the pet's new name:")
            pet.name = name
            pet_type = input("Enter the pet's new type:")
            pet.pet_type = pet_type
            breed = input("Enter the pet's new breed:")
            pet.breed = breed
            age = input("Enter the pet's new age:")
            pet.age = age
            gender = input("Enter the pet's new gender:")
            pet.gender = gender
            adopted = input("Enter the pet's new adopted status:")
            pet.adopted = adopted
            owner_id = input("Enter the pet's new owner_id:")
            pet.owner_id = owner_id
            
            pet.update()
            print(f"Successfully updated {pet}")
        except Exception as exc:
            print("Error updating {pet}:",exc)

def delete_pet():
    id = input("Enter the pet's id")
    pet = Pet.find_by_id(id)
    if pet:
        pet.delete()
        print(f"Successfully deleted {pet}")
    else:
        print("Pet not found")

def list_owner_pets():
    id = input("Enter the owner's id:")
    owner = Owner.find_by_id(id)
    if owner:
        print(owner.pets())
    else:
        print(f"Owner {id} not found")

