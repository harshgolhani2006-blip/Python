# def factors(n):
# for i in range(1,n+1):
# if n%i==0:
# print(i,end=" ")
# factors(12) 


# wap factori even or odd
# n = int(input("Enter number: "))
# fact = 1

# for i in range(1, n + 1):
# fact = fact * i

# print("Factorial =", fact)



# def factors(n):
# for i in range(1,n+1):
# if n%i==0:
# print(i,end=" ")
# x =factors(12) 
# print(x)


# def even_fact(n):
# ans=1
# for i in range(2,n+1,2):
# ans*=i
# return ans
# def odd_fact(n):
# pass
# n=int(input("Enter the number"))
# if n%2==0:
# print(even_fact(n))
# else:
# print(odd_fact(n)) 
 

# def even_fact(n):
# ans=1
# for i in range(2,n+1,2):
# ans*=i
# return ans
# def odd_fact(n):
# ans=1
# for i in range(1,n+1,2):
# ans*=i
# return ans

# n=int(input("Enter the number"))
# if n%2==0:
# print(even_fact(n))
# else:
# print(odd_fact(n)) 

 

# def factorial(x):
# fact = 1
# for i in range(1, x + 1):
# fact *= i
# return fact 

# def ncr(n, r):
# return factorial(n) // (factorial(r) * factorial(n - r))

# n = int(input("Enter n: "))
# r = int(input("Enter r: "))

# print("nCr =", ncr(n, r))



# list 
# lst=[1,2,3,"hello",5.6]
# print(lst [0])
# for i in range(len(lst)):
# print(lst[i],end=" ")

# create empty list
# lst=[]
# lst1=list()
# print(lst)
# print(lst1)


# lst=[1,2,3,"hello",5.6] 
# lst[-2]="hi"
# # print(lst [0])
# for i in range(len(lst)):
# print(lst[i],end=" ")


# lst=[1,2,3,"hello",5.6] 
# for i in lst:
#  print(i) 

lst=[3,4,5,6,7,8,-6,7,5,6666,]
for i in lst:
    if i%2==0:
        print(i,end=" ")
