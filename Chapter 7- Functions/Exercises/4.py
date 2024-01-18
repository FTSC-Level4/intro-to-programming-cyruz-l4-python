#create a similar function as exercise 3 but with a fixed argument
def make_shirt(size="large", message="I love Python"):
    print(f"Made a {size}-sized shirt with the message: '{message}'.")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(size="small", message="In GOD we TRUST!")
