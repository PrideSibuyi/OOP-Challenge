from pet import Pet

def main():
    print(" Digital Pet Simulator")
    pet_name = input("Enter your pet's name: ")
    my_pet = Pet(pet_name)

    print(f'\nCreated pet: {my_pet.name}')

    while True:
        print("\nMain Menu:")
        print("1. Feed Pet")
        print("2. Put Pet to Sleep")
        print("3. Play with Pet")
        print("4. Train Pet")
        print("5. Show Pet's Tricks")
        print("6. Show Pet's Status")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            my_pet.eat()
        elif choice == '2':
            my_pet.sleep()
        elif choice == '3':
            my_pet.play()
        elif choice == '4':
            trick = input("Enter a trick to teach your pet: ")
            my_pet.train(trick)
        elif choice == '5':
            my_pet.show_tricks()
        elif choice == '6':
            my_pet.get_status()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

