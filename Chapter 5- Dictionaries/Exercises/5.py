#Empty List
pets = []

#Create a dictionary(1) that displays all information of a pet
pet = {"Animal" : "Lion",
           "Name" : "Gab",
           "Owner" : "Cy",}

#.append() is used to add an item to certain collection types. In this case, the pet(dictionary) is added to pets(list)
pets.append(pet)  

#Create a dictionary(2) that displays all information of a pet
pet = {"Animal" : "Snake",
        "Name" : "Okininam",
        "Owner" : "CJ",}

pets.append(pet)

#Create a dictionary(3) that displays all information of a pet
pet = {"Animal" : "Hamster",
        "Name" : "Riri",
        "Owner" : "Siway"}

pets.append(pet)

#create a for loop for that every pet in pets, print the name of the pet
for pet in pets:
    print("Information about",pet['Name'],":", "\n")
#another for loop that prints out the items in every dictionary 
    for key, value in pet.items():
        print(key, ":", value)
    print("\n")


