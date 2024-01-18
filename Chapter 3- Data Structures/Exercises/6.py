# Make a guest list for a dinner
guests = ["Brent Faiyaz", "SZA", "Drake", "J.Cole"]

# Make a loop that prints an invitation to every person in the guests list
for person in guests:
    print(f"{person}, I would like to invite you to a dinner at my place.")

# Brent Faiyaz can't come to dinner
print(f"\nIt seems like {guests[0]} can't make it to dinner.")

# Replace Brent Faiyaz with Hev Abi
guests[0] = "Hev Abi"

# Backslash n for extra space
print("\n")

# Make another loop that prints out the newly updated list with Hev Abi
for person in guests:
    print(f"{person}, I would like to invite you to a dinner at my place.")

# Print message about space limitation
print("\nOh no! We only have space for two people!")

# Use pop() to remove guests until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"I'm sorry, {removed_guest}, but we can't invite you to dinner.")

# Print invitation messages for the remaining two people
for person in guests:
    print(f"{person}, you are still invited to a dinner at my place.")

# Use del to remove the last two names and create an empty list
del guests[:]

# Print to verify the list is empty
print("\nUpdated guest list:", guests)
