#Make a guest list for a dinner
guests=["Brent Faiyaz", "SZA", "Drake", "J.Cole"]
#Make a loop that prints an invitation to every person in the guests list
for person in guests:
    print(f"{person}, I would like to invite you to a dinner at my place.")
#Brent Faiyaz cant come to dinner
print(f"\nIt seems like {guests[0]} can't make it to dinner.")
#Replace Brent Faiyaz with Hev Abi
guests[0]="Hev Abi"
#Backlash n for extra space
print("\n")
#Make another loop that prints out the newly updated list with Hev Abi
for person in guests:
    print(f"{person}, I would like to invite you to a dinner at my place.")

    