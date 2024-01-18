#list with added three pastrami
sandwich_orders=["Egg sandwich", "Chicken sandwich", "Pastrami", "Beef sandwich", "Pastrami", "Ham sandiwch", "Pastrami", "Nutella sandwich"]
#empty list
finished_sandwiches=[]
print("The deli has ran out of Pastrami.")
#for every pastrami in sandwich order
while "Pastrami" in sandwich_orders:
    #delete pastrami using .remove()
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print(f"I am making your {sandwich}.")
    finished_sandwiches.append(sandwich)

print("\n")

for sandiwch in finished_sandwiches:
    print(f"I made your {sandiwch}")

    