def describe_pet(animal_type: str = "dog", pet_name: str = "white"):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}`s name is {pet_name.title()}!")


describe_pet()
