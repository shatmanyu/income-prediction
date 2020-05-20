## prime numbers 100 to 300
## brute force
##prime=[]
##for i in range(100,301):
##    c=0
##    for j in range(1,i+1):
##
##        if(i%j==0):
##            c+=1
##
##    if(c==2):
##        prime.append(i)
##
##print(*prime)

##################################################################
##################################################################
## to check the num is armstrong or not
def armstrong(a,a1):
    s=str(a)
    l=list(s)
    ans=[]
    for i in l:
        ans.append(str(pow(int(i),3)))

    num=0
    for i in ans:
        num+=int(i)

    if(num==a1):
        return True
    else:
        return False


a=int(input("enter the number"))
a1=int(a)
if(armstrong(a,a1)):
    print("yes")
else:
    print("no")

        
        
            
