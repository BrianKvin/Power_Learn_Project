""" 
Create a program that stores a list of words. 
Then, use list comprehension to create a new list 
that contains only the words that have an odd number of characters
"""


# Store a list of words
word_list = ["apple", "banana", "orange", "pear", "grape", "kiwi", "pineapple"]

# Use list comprehension to create a new list containing only words with odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

# Print the new list
print("Words with odd number of characters:", odd_length_words)
