# Think of at least five places in the world you’d like to visit
places=["Paris", "Tokyo", "New York", "Japan", "Amsterdam"]

# Print your list in its original order
print("Original order:", places)

# Use sorted() to print your list in alphabetical order without modifying the actual list
print("Alphabetical order:", sorted(places))

# Show that your list is still in its original order by printing it
print("Original order:", places)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
print("Reverse alphabetical order:", sorted(places, reverse=True))

# Show that your list is still in its original order by printing it again
print("Original order:", places)

# Use reverse() to change the order of your list
places.reverse()
print("Reversed order:", places)

# Use reverse() to change the order of your list again
places.reverse()
print("Back to original order:", places)

# Use sort() to change your list so it’s stored in alphabetical order
places.sort()
print("Sorted order:", places)

# Use sort() to change your list so it’s stored in reverse alphabetical order
places.sort(reverse=True)
print("Reverse sorted order:", places)

