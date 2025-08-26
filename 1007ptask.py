#finding the prime number present at the given position.
pos=3
num=2
count=0
while pos>count:
    factor=0
    for i in range(2,num):
        if num%i==0:
            factor+=1
            break
    if factor==0:
        count+=1
        prime=num
    num+=1
    print(f"{count} prime number is {prime}")
    

#to check th longest palindrome in given string.
string="malayali"
longest=""
i=0
while i<len(string) and len(longest)<len(string[i::]) : #For time complexity
    temp="" 
    for j in range(i,len(string)):
        temp+=string[j]
        if temp==temp[::-1] and len(temp)>len(longest):
            longest=temp
    i+=1
print(longest)   #O/p:layal

print(f"{count} palindromes in the given string")

# to check lowest
# word="ambikeasr"
# smallest=""
# for i in range(0,len(word)):
#     temp=""
#     for j in range(i,len(word)):
#         temp+=word[j]
#         if temp==temp[::-1] and len(temp)<len(smallest):
#             smallest=temp
#     i+=1
# print(temp)

#Truthsy values

# if "v":               #non empty string is true value
#     print("truthsy") #O/p:truthsy

# if (1):               #non empty tuple
#     print("truthsy")  #truthsy

# if[1,2]:                 #non empty list
#     print("truthsy") #truthsy


# #falsy values

# if 0:                     # Zero is false value 
#     print("truthsy")
# else:
#     print("falsy")  #falsy

# if not None:
#     print("falsy")  #falsy

# if not []:
#     print("falsy") #falsy



