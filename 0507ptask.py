#Lcm of two numbers ----Least common multiple
 #The LCM (Least Common Multiple) of two or more integers is the smallest positive number that is exactly divisible by each of the numbers.
# n1 = 4 and n2 = 5 
# Multiples of 4: 4, 8, 12, 16, 20 , 24...
# Multiples of 5: 5, 10, 15, 20, 25, ...

n1=100        #900
n2=45           
big=0      
small=0
if n1<n2:       #to find big number and small number
    big=n2
    small=n1
else:
    small=n2
    big=n1
print(big,small)

if big%small==0:       #check if big number exactly multilplies small number 
    print(big,"is lcm")         #if divides it is the lcm
else:
    is_found=False            # taking a true condition to run loop until condition satisfy
    temp_lcm=big+big         #already we have checked with the big number so from next we have to check
    while is_found==False:     #condition false until finding the lcm
       if temp_lcm%n1==0 and temp_lcm%n2==0:       #conditions until multiples divides with both the numbers
           print(temp_lcm,"is a lcm")            
           break                                 #to stop loop when find
       else:
           temp_lcm+=big         #if not found add big number to temp_lcm to get next multiple


#To get gcd of two numbers
n1=int(input("Enter the First number:"))
n2=int(input("Enter the Second number:"))
small=0
if n1<n2:
    small=n1
else:
    small=n2
print(small)
gcd=0
for i in range(1,small+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print(gcd)


#To check whether the given number is perfect number or not
n=123
perfect=0
for i in range(1,n):
    if n%i==0:
     perfect+=i
print(perfect)
if n==perfect:
   print("Is perfect")
else:
   print("not")
