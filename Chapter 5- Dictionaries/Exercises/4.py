#Create a dictionary of three major rivers
Rivers = {"Yangtze River" : "China",
          "Mississipi River" : "United States",
          "Yenisey River" : "Russia"}

#Create a for loop in which for every "river" and "country" in the dictionary, print the ouput
#.items() returns all items(rivers, countries) in a dictionary
for river, country in Rivers.items():
    print(river, "runs through", country)

#Backslash n for extra space
print("\n")

#Create for loop that prints out the river for every keys the loop encounters
#.keys() returns all keys(rivers) in a dictionary
for river in Rivers.keys():
    print(river)
print("\n")

#Create a for loop that prints out the country for every value the loop encounters
#.values() returns all values(country) in a dictionary
for country in Rivers.values():
    print(country)

    