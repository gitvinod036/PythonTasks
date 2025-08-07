#3
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1  or j==rows or i==(rows//2)+1 or i==rows:
         res+="*"+" "
        else:
         res+=" "+" "
    print(res)


#2
n=5
mid=(n//2)+1
for i in range(1,n+1):
    res=""
    for j in range(1,n+1):
        if i<=mid:
            if i==1 or i==mid or j==n:
                res+="*"+" "
            else:
                res+=" "+ " "
        else:
            if i==n or j==1:
                res+="*"+" " 
            else:
                res+=" "+" " 
    print(res)    

#s
rows=5
mid=(rows//2)+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i<=mid:
         if i==1 or i==mid or j==1:
           res+="*"+" "
         else:
            res+=" "+" "
        else:
         if j==rows or i==rows:
              res+="* "
         else:
              res+=" "+" "
    print(res)







