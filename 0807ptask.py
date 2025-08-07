#08/08
# what is armstrong number.
def Armstrong(n):
 n1=n
 n2=n
 count=0
 while n1!=0: #153!=0 
    n1=n1//10 
    count+=1
 total=0
 while n2!=0:
    last_digit=n2%10    # 153%10 15.3  3
    total=total+(last_digit**count)
    n2=n2//10
 if total==n:
    print(n,"is Armstrong number")
 else:
    print(n,"is not Armstrong number")

Armstrong(153)

#what is fibanooci???
#0 1 1 2 3 5 8 13 21 34
def fibanooci(n):
 a=0
 b=1
 for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
fibanooci(20)



# Number methods
#abs()
print(abs(-17)) #17
print(abs(10))  #10

#round()
print(round(3.91,0)) #4.0
print(round(3.45,1)) #3.4
print(round(3.45849,1)) #3.45

#pow()
print(pow(5,3)) #125
print(pow(3,4)) #81

#divmod()-Divisor&modulus
print(divmod(10,5))  #(quotient=2,remainder=0)
print(divmod(14,3))   #4,2

#int()
print(int("5")) #5
print(int(5.433)) #5

#float()
print(float(5)) #5.0
print(round(float(5.987),2)) #5.99

#complex()
print(complex(2,5)) #2+5j
print(complex(3))   #3+0j

#bin()
print(bin(35)) #100011
print(bin(3))  #0011

#oct() hex()
print(oct(8))  #0o10
print(hex(15)) #0xf

#isinstance()
print(isinstance(5,int))      #true
print(isinstance(2.33,float)) #true
print(isinstance(6.7,int))    #false