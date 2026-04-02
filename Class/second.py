#wap to degree calcius #to degree fahrenheitc
# degree_celcius = float(input("Enter the degree in celcius: "))
# degree_fahrenheit = (degree_celcius * 9/5) + 32
# print(f"{degree_celcius} degree celcius is equal to {degree_fahrenheit} degree fahrenheit")

# #wap to degree fahrenheit #to degree celcius
# degree_fahrenheit = float(input("Enter the degree in fahrenheit: "))
# degree_celcius = (degree_fahrenheit - 32) * 5/9
#print(f"{degree_fahrenheit} degree fahrenheit is equal to {degree_celcius} degree celcius")

#wap which takes the radius of a circle as input and calculates the area and circumference of the circle.
# radius = float(input("Enter the radius of the circle:"))
# area = 3.14 * radius * radius
# circumference = 2 * 3.14 * radius
# print("The area of the circle is:", area)
# print("The circumference of the circle is:", circumference)
 
 #condition statement.
 #Wap to check egilibility for voting.
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

#wap to determine grade based on marks obtained.
# marks = float(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade: A")   
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

#wap to determine the person is a child, teenager, adult, or senior citizen based on their age.
# age = int(input("Enter your age: "))
# if age < 13:
#     print("You are a child.")
# elif age < 20:
#     print("You are a teenager.")
# elif age < 60:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")
    
    #wap to check the dividibility of a number by 2, 3, and 5.
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is divisible by 2.")
# if number % 3 == 0:
#     print(f"{number} is divisible by 3.")
# if number % 5 == 0:
#     print(f"{number} is divisible by 5.")
# else:
#     print(f"{number} is not divisible by 2, 3, or 5.")
    
    #wap to find the largest of three numbers.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3
# print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")
 
 #wap to detemine of a triangle is equilateral, isosceles, or scalene based on the lengths of its sides.
# side1 = float(input("Enter the length of the first side of the triangle: "))
# side2 = float(input("Enter the length of the second side of the triangle: "))
# side3 = float(input("Enter the length of the third side of the triangle: "))
# if side1 == side2 == side3:
#     print("The triangle is equilateral.")
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     print("The triangle is isosceles.")
# else:
#     print("The triangle is scalene.")
  
  #wap tp determine if a year is a century year or not.
# year = int(input("Enter a year: "))
# if year % 100 == 0:
#     print(f"{year} is a century year.")
# else:
#     print(f"{year} is not a century year.")

#wap to determine if a year is a leap year or not.
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

#wap to  input electricity unit consumed and calculate the total electricity bill and cal surcharge if the bill exceeds 20% The billing rates are as follows:
# units= float(input("Enter the electricity units consumed: "))
# if units <= 50:
#     bill = units * 0.50
# elif units <= 150:
#     bill = (50 * 0.50) + ((units - 50) * 0.75)
# elif units <= 250:
#     bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
# else:
#     bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)
# print(f"The total electricity bill for {units} units is: {bill:.2f}")
# surcharge = bill * 0.20
# bill += surcharge
# print(f"A surcharge of 20% has been added to the bill for consuming more than 250 units.",bill)
# print(f"The total electricity bill after adding the surcharge is: {bill:.2f}")
    
#wap a which accept the kilometer covered and calculate the bill according to the following:
#first 10 km: Rs. 11 per km Next 90 km: Rs. 10 per km After that: Rs. 9 per km
# kilometers = float(input("Enter the kilometers covered: "))
# if kilometers <= 10:
#     bill = kilometers * 11
# elif kilometers <= 100:
#     bill = (10 * 11) + ((kilometers - 10) * 10)
# else:
#     bill = (10 * 11) + (90 * 10) + ((kilometers - 100) * 9)
# print(f"The total bill for covering {kilometers} kilometers is: Rs. {bill:.2f}")

#loop function
# in range error step=0, and no parameter give.
range(2, 10, 2)
print(list(range(2, 10, 2)))