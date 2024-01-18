#Prints a sentence summarizing the size and message of a shirt.
def make_shirt(size, message):
    print(f"Made a {size}-sized shirt with the message: '{message}'.")

# Call the function using positional arguments
make_shirt("medium", "I love SZA")

# Call the function using keyword arguments
make_shirt(size="large", message="For all the dogs")
