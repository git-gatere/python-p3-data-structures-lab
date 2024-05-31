import string

def sorted_names(names):
    alphabet = string.ascii_lowercase
    letter_values = {}
    
    # Assigning numerical values to letters
    for index, letter in enumerate(alphabet):
        value = index + 1
        letter_values[letter] = value
    
    # Printing values for each letter in each name
    for name in names:
        for letter in name.lower():  # Converting to lowercase for consistency
            if letter in letter_values:
                print(letter_values[letter])
            else:
                # If the character is not a letter, you may handle it as per your requirement
                print("Not a letter:", letter)
                
# Example usage
names = ["Alice", "Bob", "Charlie"]
sorted_names(names)
