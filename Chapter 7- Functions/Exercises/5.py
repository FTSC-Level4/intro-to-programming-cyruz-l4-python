#create new function that takes two argument, a (city) and a default value (USA)
def describe_city(city, country="USA"):
    print(f"{city} is in {country}.")
#print "new york" as the value of city
describe_city("New York")

#replace the values of the argument, city and country
describe_city("Paris", "France")
describe_city("Tokyo", "Japan")

