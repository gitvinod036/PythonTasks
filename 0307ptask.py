# # 1. Create a string with your name and print it.
name="vinod"
print(name)

# # # 2. Get the first character from the string.
name="Vinod"
print(name[0])

# # 3. Get the last character from the string.
name="Vinod"
print(name[len(name)-1])

# # # 4. Concatenate two strings.
f_name="Vinod"
l_name="kumar"
print(f_name+l_name)

# # 5. Repeat a string 3 times.
string="Hello"
for i in range(3):
    print(string)

# # 6. Slice the first 5 characters.
string="Vinod Kumar"
for i in range(len(string)):
   if i<=4:
    print(string[i])

# # # 7. Reverse a string using slicing.
string="vinod"
for i in range(len(string)-1,-1,-1):
  print(string[i])

# # 8. Check if a substring exists in a string.
string="vinod kumar"
print(string.find("k"))

# # # 9. Find the length of a string.
String="vinod kumar"
print(len(String))

# # 10. Convert string to uppercase.
String="Vinod"
print(String.upper())

# # 11. Convert string to lowercase.
String="Python"
print(String.lower())

# # 12. Capitalize the first letter.
String="PYTHON"
print(String.capitalize())

# # 13. Convert a string to title case.
String="Vinod kumar"
String=String.title()
print(String)
# # 14. Remove leading spaces using lstrip().
String="  Python   "
print(String.lstrip())

# # 15. Remove trailing spaces using rstrip().
String="  Python   "
print(String.rstrip())
