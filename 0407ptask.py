#write a function to return no of palindromes in string.
def no_of_palindromes(sentence):
 sentence=sentence.split(" ")
 is_palindrome=False
 count=0
 for i in range(len(sentence)):
    if sentence[i]==sentence[i][::-1]:
        is_palindrome=True
        count+=1
 if is_palindrome==True:
    print(count,"palindromes in this sentence")
 else:
    print("There are no palindromes in this string")

no_of_palindromes("The malayalam man have a racecar")

#check whether the given substring is present in a string.
def check_substring(string):
 sub_string=input("Enter the sub string value:")
 sub_length=len(sub_string)
 for i in range(len(string)):
   if string[i:i+sub_length]==sub_string:
      print(sub_string,"is a part of string")
      break

check_substring("i love python programming")


