# Exercise 02 - Strings

# Variables for firstname and last name
first_name = "cool"
last_name = "ravi"

# Add variable for full name
full_name = f"{first_name} {last_name}"
print("I am ", full_name)

# Print name in upper case, lower case and title
print(full_name.upper())
print(full_name.lower())
print(full_name.title())

# Display the string length of name
print(len(full_name))

# check whether particular word exist in fullname
specific_word = "cool"
if specific_word in full_name:
    print(specific_word, " exist in full_name")
else:
    print(specific_word, " doesnt exist in full_name")


# Use f-string to display name
print(f"Hello {full_name}! Welcome to the Python world.")

# Bonus items on strings exercise:
# print first character of full name
print("first character of full name: ", full_name[0])

# Display last character of full name
print("last character of full name: ", full_name[-1])

# Display full name in reverse order
print("reverse of full name: ", full_name[::-1])

# check whether full name is palindrome
if full_name == full_name[::-1]:
    print(full_name, "is a palindrome")
else:
    print(full_name, "isn't palindrome")
