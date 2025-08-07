
#Check whether the char is lower,upper,number using function 
def check_type(char):
    Lower_count=0
    upper_count=0
    number_count=0
    for i in range(len(char)):
        order=ord(char[i])  #order=ord converts char that present in index[i] into ascci code
        if order>=65 and order<=90:
            upper_count+=1
        elif order>=97 and order<=122:
            Lower_count+=1
        elif order>=48 and order<=57:
            number_count+=1
    print(upper_count)
    print(Lower_count)
    print(number_count)
check_type("aA1")

#write function to convert vowel char into next char
def function(char):
 secret=""
 for i in range(len(char)):
    word=ord(char[i])        # ord converts char present in index[i] into ascii code and store in word
    if char[i]=='a' or char[i]=='i' or char[i]=='o' or char[i]=='u' or char[i]=='e':
        secret+=chr(word+1)  #ascii code +1 if char is vowel and convert into char by using chr function and add to secret
    else:
        secret+=char[i] #else add the char into secret
 return secret          
print(function("vinod"))