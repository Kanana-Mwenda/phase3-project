from helpers import (
    exit_program,
    view_owners,
    find_owner_by_id,
    find_owner_by_name,
    create_owner,
    update_owner,
    delete_owner,
    view_pets,
    find_pet_by_id,
    find_pet_by_pet_type,
    create_pet,
    update_pet,
    delete_pet,
    view_owner_pets
)

def main():
    while True:
        menu()
        choice = input(">")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_owners()
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
            view_pets()
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
            view_owner_pets()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1: View all owners")
    print("2: Find owner by id")
    print("3: Find owner by name")
    print("4: Create owner")
    print("5: Update owner")
    print("6: Delete owner")
    print("7: View all pets")
    print("8: Find pet by id")
    print("9: Find pet by pet type")
    print("10: Create pet")
    print("11: Update pet")
    print("12: Delete pet")
    print("13: View all owner pets")
    
if __name__ == "__main__":
    main()