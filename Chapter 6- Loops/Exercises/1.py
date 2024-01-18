# Initialize an empty list to store toppings
pizza_toppings = []

# Prompt the user for pizza toppings
while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")

    if topping.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'

    # Add the topping to the list
    pizza_toppings.append(topping)
    print(f"Added {topping} to your pizza.")

# Display the final list of pizza toppings
print("\nYour pizza will have the following toppings:")
for topping in pizza_toppings:
    print(topping)

