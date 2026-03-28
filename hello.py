# print("hello world")
# print("hello world")
# print("I am Manish Golhani")

# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# h=float(input("Enter your height: "))
# print("My name is ",name,", my age is ",age," and my height is ",h)

# #write a program in which length and breadth of rectangle is given by user and find area and perimeter of rectangle

# length=float(input("Enter length of rectangle: "))
# breadth=float(input("Enter breadth of rectangle: "))
# area=length*breadth
# perimeter=2*(length+breadth)
# print("Area of rectangle is: ",area)
# print("Perimeter of rectangle is: ",perimeter)
# #write a which will take principal, rate of interest and time from user and calculate simple interest
# p=float(input("Enter principal amount: "))
# r=float(input("Enter rate of interest: "))
# t=float(input("Enter time in years: "))
# si=(p*r*t)/100
# print("Simple Interest is: ",si)
# #write a program which wil take age as input from user and if age is above 18 then it will print you are eligible for voting otherwise not
# age=int(input("Enter your age: "))
# if age>=18:
#     print("You are eligible for voting")
# else:
#     print("ypu are not eligible for voting")
# #Write a program which will take a YEAR as input from user and check whether the year is leap year or not.
# year=int(input("Enter a year: "))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(year," is a leap year")
# else:
#     print(year," is not a leap year")
# #Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
# # For first 50 units Rs. 0.50/unit
# # For next 100 units Rs. 0.75/unit
# # For next 100 units Rs. 1.20/unit
# # For unit above 250 Rs. 1.50/unit
# # An additional surcharge of 20% is added to the bill
# # Program to calculate electricity bill

# units = float(input("Enter total electricity units consumed: "))

# if units <= 50:
#     amount = units * 0.50
# elif units <= 150:
#     amount = 50 * 0.50 + (units - 50) * 0.75
# elif units <= 250:
#     amount = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
# else:
#     amount = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50

# # Adding 20% surcharge
# surcharge = amount * 0.20
# total_amount = amount + surcharge

# print(f"Electricity Bill = Rs. {total_amount:2f}")
# # for loop
# # start -> include
# # and->exclude
# # Default->
# # start->0
# # end ->1
# # range error jab throw karta hai tab step =0 or end 
# for i in range(2,21,2):
#     print(i)
#     # write a program to cal sum of all even numbers from 1 to n
# sum=0
# n=int(input("Enter a number: "))
# for i in range(2,n+1,2):
#     sum=sum+i
# print("Sum of all even numbers from 1 to ",n," is: ",sum)
# #write a program to which will print fizz for multiples of 3, buzz for multiples of 5 and fizzbuzz for multiples of both 3 and 5
# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)
# #WAP to print your name n time .
# n=int(input("Enter a number of n :"))
# for i in range(0,n,1):
#     print("Harsh Golhani")
# #WAP to print Even number n time .