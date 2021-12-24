# Band Name Generator

print("----Welcome to the Band Name Generator----")

#  initializing the variables as empty strings
city = ""
pet_name = ""

#  simple check to make sure the user has entered something
while True:
    print("What's the name of the city you grew up in?")
    city = input("> ")
    # if there is no input, asking again
    if city == "":
        print("Sorry.....You haven't entered anything. Please try again.")
    # if there is some input, breaking out of the loop
    else:
        break

#  check for the pet name
while True:
    print("What's your pet's name?")
    pet_name = input("> ")
    if pet_name == "":
        print("You haven't entered anything. Please try again.")
    else:
        break

#  output using f-strings
print(f"Your band name could be {city} {pet_name}.")
