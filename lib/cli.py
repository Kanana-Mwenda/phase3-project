from helpers import (
    exit_program,
    list_owners,
    find_owner_by_id,
    find_owner_by_name,
    create_owner,
    update_owner,
    delete_owner,
    list_pets,
    find_pet_by_id,
    find_pet_by_pet_type,
    create_pet,
    update_pet,
    delete_pet,
    list_owner_pets
)

def main():
    while True:
        menu()
        choice = input(">")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_owners()
        elif choice == "2":
            find_owner_by_id()
        elif choice == "3":
            find_owner_by_name()
        elif choice == "4":
            create_owner()
        elif choice == "5":
            update_owner()
        elif choice == "6":
            delete_owner()
        elif choice == "7":
            list_pets()
        elif choice == "8":
            find_pet_by_id()
        elif choice == "9":
            find_pet_by_pet_type()
        elif choice == "10":
            create_pet()
        elif choice == "11":
            update_pet()
        elif choice == "12":
            delete_pet()
        elif choice == "13":
            list_owner_pets()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")

if __name__ == "main":
    main()