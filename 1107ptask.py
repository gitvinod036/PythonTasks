# #To find the smallest palindrome in the given word.
word="malayalam"
i=0
smallest=word
while i<len(word):
    temp=""
    for j in range(i,len(word)):
        temp+=word[j]
        if temp==temp[::-1] and len(temp)>2 and len(temp)<len(smallest):
            smallest=temp
    i+=1
if smallest!=word:
    print(smallest,"is the smallest palindrome")  #ala is the smallest palindrome
else:
    print("no palindromes")

# #To count the palindrome and adding the unique palindrome into the List.
# word="malayalam"
# count=0
# list=[]
# for i in range(len(word)):
#     temp=""
#     for j in range(i,len(word)):
#         temp+=word[j]
#         if temp==temp[::-1] and len(temp)>2:
#             if temp not in list:
#                 list.append(temp)
#                 count+=1
# print(count)        #O/p:5
# print(list)         #O/p:['malayalam','ala','alayala','layal','aya'] 



# rows=5
# for i in range(1,rows+1):
#     res=""
#     for space in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#        res+="*"+" "
#     print(res)
# rows=5
# for i in range(rows,0,-1):
#     res=""
#     for spaces in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)

#
# rows=5
# for i in range(1,rows+1):
#     res=""
#     for spaces in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)
# for i in range(rows-1,0,-1):
#     res=""
#     for space in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)

# rows=5
# for i in range(rows,0,-1):
#     res=""
#     for space in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)
# for i in range(1,rows+1):
#     res=""
#     for spaces in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)


# rows=5
# for i in range(1,rows+1):
#     res=""
#     for spaces in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#       if i==rows or i==j or j==1:
#         res+="*"+" "
#       else:
#          res+=" "+" "
#     print(res)
# for i in range(rows-1,0,-1):
#    res="" 
#    for spaces in range(1,rows-i+1):
#       res+=" "
#    for j in range(1,i+1):
#       if i==rows or j==1 or i+j==rows+1:
#          res+="*"+" "
#       else:
#          res+=" "+" "
#    print(res)
      