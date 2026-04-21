#write a program to print the list of first and last element of each list of lists.
# list_of_lists = [[23, 45, 76], [45, 3, 12], [3, 5, 20]]
# first_and_last = []
# for lst in list_of_lists:
#     first_and_last.append((lst[0], lst[-1]))
# print(first_and_last)

#write a program to calculate and print the sum of max elements of each list of lists.
# list_of_lists = [[1, 2, 4, 5], [3, 5, 4, 3], [4, 5, 3, 2]]

# Sum_of_max = 0

# for lst in list_of_lists:
#     maximum = max(lst)
#     print("Maximum of", lst, "=", maximum)
#     Sum_of_max += maximum

# print("Sum of maximum elements =", Sum_of_max)

#wap to calculate and print the sum of min elements of each list of lists.
# list_of_lists = [[1, 2, 4, 5], [3, 5, 4, 3], [4, 5, 3, 2]]

# Sum_of_min = 0

# for lst in list_of_lists:
#     minimum = min(lst)
#     print("Minimum of", lst, "=", minimum)
#     Sum_of_min += minimum

# print("Sum of minimum elements =", Sum_of_min)

#wap to insert the product of the first and last element at the third position in the list.print the list before and after the insertion.
# list_of_lists = [[1, 2, 4,5], [3, 5, 4,3], [4, 5,3,2]]
# for lst in list_of_lists:
#     product = lst[0] * lst[-1]
#     lst.insert(2, product)
# print(list_of_lists)

#wap to divdide the list into two equal halves and print the sum of each half.
# list_of_Lists=[2,4,6,8,3,5,8,9]
# half_length = len(list_of_Lists) // 2
# first_half = list_of_Lists[:half_length]
# second_half = list_of_Lists[half_length:]
# print("First half:", first_half)
# print("Second half:", second_half)
# print("Sum of first half:", sum(first_half))
# print("Sum of second half:", sum(second_half))

#wap create a list with divible by 3 between 4 to 25 and print the list.
# divisible_by_3 = [num for num in range(4, 26) if num % 3 == 0]
# print(divisible_by_3)

#wap to create a list with divible by 3 between 4 and 50 and print a even and odd number  and square of each number in the list.
# divisible_by_3 = [num for num in range(4, 51) if num % 3 == 0]
# even_numbers = [num for num in divisible_by_3 if num % 2 == 0]
# odd_numbers = [num for num in divisible_by_3 if num % 2 != 0]
# squares = [num ** 2 for num in divisible_by_3]
# squares_of_even_numbers = [num ** 2 for num in even_numbers]
# squares_of_odd_numbers = [num ** 2 for num in odd_numbers]
# print("Divisible by 3:", divisible_by_3)
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)
# print("Squares:", squares)
# print("Squares of even numbers:", squares_of_even_numbers)
# print("Squares of odd numbers:", squares_of_odd_numbers)

#wap to create a list and print even and odd replace with "even" and "odd" respectively.
# list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = ["even" if num % 2 == 0 else "odd" for num in list_of_numbers]
# print("Result:", result)

# wap to print list of first and last element of each list of lists.
list_of_lists = [[23, 45, 76], [45, 3, 12], [3, 5, 20]]
first_and_last = []
for lst in list_of_lists:
    first_and_last.append((lst[0], lst[-1]))    
print(first_and_last)