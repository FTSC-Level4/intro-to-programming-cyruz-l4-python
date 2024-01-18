#Add more words to the dictionary made on exercise 2
Programming_words = {"List" : "are used to store multiple items in a single variable",
                     "Dictionary" : "are used to store data values in key:value pairs",
                     "While_loop" : "executes a set of statements as long as a condition is true",
                     "For_Loop" : "are used for iterating over a sequence",
                     "Strings" : "are used to represent text rather than numbers",
                     "Integer" : "are whole numbers, positive or negative, without decimals",
                     "Float" : "an integer containing one or more decimals",
                     "Tuple" : "used to store multiple items in a single variable",
                     "Comments" : "used to explain Python code",
                     "Booleans" : "represents True or False"}

#Make a for loop that prints out the items in the dictionary 
for word, definition in Programming_words.items():
    print(word, ":", definition)

    