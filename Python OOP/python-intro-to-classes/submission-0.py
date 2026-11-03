class Pet:
    def __init__ (my_pet,name,species):
        my_pet.species = species
        my_pet.name = name


# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
