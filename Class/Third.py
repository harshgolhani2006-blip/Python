# for i in range(0,30,2):
#      print(i)   //vertical.
# for i in range(0,30,2):
#     print(i,end=" ")  #Horizontal.
    
    # wap print virtual divible by fizz =3 , buzz=5(1-50)
# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("It is both fizz and buzz")
#     elif i % 3 == 0:
#       print("It is fizz")
#     elif i % 5==0:
#       print("It is buzz")
# else:
#     print("It is not divisible by 3 and 5")
        

#wap  which will take a num input for user factor in 12.
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     if  n % i==0:
#         print(i)

#wap to print factors and find enven and odd how many present in factors.
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     if n % i ==0:
#         print(i)
#         if i % 2 ==0:
#             print("Even")
#         else:
#             print("Odd")
            
# wap to print factor and count the number even count  and odd count present in factors.
# n=int(input("Enter a number :"))
# even_count=0
# odd_count=0
# for i in range(1,n+1):
#     if n % i ==0:
#         print(i)
#         if i % 2 ==0:
#             even_count+=1
#         else:
#             odd_count+=1
# print("Even count:",even_count)
# print("Odd count:",odd_count)

#wap to print the prime number.
# n=int(input("Enter a number :"))
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print(n, "is not a prime number")
#             break
#     else:
#         print(n, "is a prime number")
        
# wap to print the prime number between 1 to 100.
# for num in range(1, 101):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# WHILE LOOP
# i=2
# while i<=30:
#     if i%2==0:   
#       print(i)
#     i+=1

#wap to take a number input from user and calculate the digit count in that number.
# n=int(input("Enter a number :"))
# digit_count=0
# while n>0:
#     digit_count+=1
#     n//=10
# print("Digit count:", digit_count)

#wap to take a number input from user and calculate the digit count and also calculate the sum of digits in that number.
# n=int(input("Enter a number :"))
# digit_count=0
# digit_sum=0
# while n>0:
#     digit_count+=1
#     digit_sum+=n%10
#     n//=10
# print("Digit count:", digit_count)
# print("Sum of digits:", digit_sum)

#wap to take a number input from user and reverse the number.
n=int(input("Enter a number :"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
print("Reversed number:", reverse)
