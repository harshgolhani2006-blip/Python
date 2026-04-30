#wap to create two set and find the common element in both set
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# common_elements = set1.intersection(set2)
# print("Common elements in both sets:", common_elements)

# wap to create two set and find the union of both set
# set1={10,20,30,40,50}
# set2={40,50,60,70,80}
# union_set=set1.union(set2)
# print("Union of both sets:",union_set)

#wap to create two set and check if all elements of one set contained within another sets and print the result.
# set1={1,2,3}
# set2={1,2,3,4,5,6,7,8}
# is_subset=set1.issubset(set2)
# print("Is set1 a subset of set2?",is_subset)

# wap which create a new set from given two sets have only that elements which  are not common.
# set1={2,4,6}
# set2={1,3,5}
# print(set1 ^ set2)

#wap to combine all elements from three sets and find the length of the combined set.
# set1={1,2,3}
# set2={4,5,6}
# set3={7,8,9}
# combined_set=set1.union(set2).union(set3)
# print("Combined set:",combined_set)
# print("Length of combined set:", len(combined_set))

#wap to find all elements in a set that are not in another set.
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# difference_set=set1-set2
# print("Elements in set1 that are not in set2:",difference_set)

# wap to remove a specific element(n) from a set ,but only if it exits in the set.
# set={1,2,3,4,5}
# n=int(input("Enter the element to remove: "))
# if n in set:
#     set.remove(n)
#     print("Element removed:", n)
# else:
#     print("Element not found in the set")

#Write a program to multiply all the float element in the set.set should be taken as input such that a set should contain integer float and string element.
# Input:- Enter a set:-{5, 'abc', 7, 8.0, 'def', '10.0', 11, 12.0, '123', 14.0}
#Output:- 1344.0

# input_set = input("Enter a set: ")
# input_set = eval(input_set)  # Convert the input string to a set
# product = 1.0  # Initialize product as a float
# for element in input_set:
#     if isinstance(element, float):  # Check if the element is a float
#         product=product * element  # Multiply the float element to the product
# print("Product of all float elements in the set:", product)

# Write a program to add all the integer element in a set and set should be taken as input such that a set should contain integer float and string element.
# input_set = input("Enter a set: ")
# input_set = eval(input_set)  # Convert the input string to a set
# total = 0  # Initialize total as an integer
# for element in input_set:
#     if isinstance(element, int):  # Check if the element is an integer
#         total += element  # Add the integer element to the total
# print("Sum of all integer elements in the set:", total)

#Write a Python program to convert all the even number of a set into a string and set should be user defined.
# input_set = input("Enter a set: ")
# input_set = eval(input_set)  # Convert the input string to a set
# converted_set = set()  # Create an empty set to store the converted elements
# for element in input_set:
#     if isinstance(element, int) and element % 2 == 0:  # Check if the element is an even integer
#         converted_set.add(str(element))  # Convert the even integer to a string and add it to the converted set
#     else:
#         converted_set.add(element)  # Add the non-even elements as they are to the converted set
# print("Set after converting even numbers to strings:", converted_set)

#Write a Python program to convert all the odd number of a set into a float and set should be user defined.
# input_set = input("Enter a set: ")
# input_set = eval(input_set)  # Convert the input string to a set
# converted_set = set()  # Create an empty set to store the converted elements
# for element in input_set:
#     if isinstance(element, int) and element % 2 != 0:  # Check if the element is an odd integer
#         converted_set.add(float(element))  # Convert the odd integer to a float and add it to the converted set
#     else:
#         converted_set.add(element)  # Add the non-odd elements as they are to the converted set
# print("Set after converting odd numbers to floats:", converted_set)

#Write a program to convert all the integer element of a set into float and the float element of a set into integer and set should be user defined
# input_set = input("Enter a set: ")
# input_set = eval(input_set)  # Convert the input string to a set
# converted_set = set()  # Create an empty set to store the converted elements
# for element in input_set:
#     if isinstance(element, int):  # Check if the element is an integer
#         converted_set.add(float(element))  # Convert the integer to a float and add it to the converted set
#     elif isinstance(element, float):  # Check if the element is a float
#         converted_set.add(int(element))  # Convert the float to an integer and add it to the converted set
#     else:
#         converted_set.add(element)  # Add the non-integer and non-float elements as they are to the converted set
# print("Set after converting integers to floats and floats to integers:", converted_set)

# Given two sets, A and B.Write a python program which find all elements that are in either A or B,but not in both. Create a third set with these elements.
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# C = A.symmetric_difference(B)
# print("Set C (elements in either A or B but not in both):", C)

# Given two sets, X and Y.Write a python program which check if all elements of X are presentwithin Y. If present, then remove those elements from Y; otherwise, add theelements of X to Y.
# Input sets
# X = set(map(int, input("Enter elements of X separated by space: ").split()))
# Y = set(map(int, input("Enter elements of Y separated by space: ").split()))

# # Check if all elements of X are present in Y
# if X.issubset(Y):
#     # Remove elements of X from Y
#     Y = Y - X
#     print("All elements of X are present in Y.")
#     print("After removing X from Y:", Y)
# else:
#     # Add elements of X to Y
#     Y = Y.union(X)
#     print("Not all elements of X are present in Y.")
#     print("After adding X to Y:", Y)

# You are given three lists, L1, L2, and L3.Write a python program which combine all unique elements from these
# lists into a set. After that, remove any elements that appear in all three lists.
# l1 = [1, 2, 3, 4, 5]
# l2 = [4, 5, 6, 7, 8]
# l3 = [5, 6, 7, 8, 9]
# # Combine all unique elements from the lists into a set
# combined_set = set(l1) | set(l2) | set(l3)
# # Find elements that appear in all three lists
# common_elements = set(l1) & set(l2) & set(l3)
# # Remove elements that appear in all three lists from the combined set
# final_set = combined_set - common_elements
# print("Final set after removing elements that appear in all three lists:", final_set)

#Write a python program if a set and list is given then, for each elementin L, if it's not already in S, add it; otherwise, remove it from S and then print S. 
# Input set S
# S = set(map(int, input("Enter elements of the set S separated by space: ").split()))

# # Input list L
# L = list(map(int, input("Enter elements of the list L separated by space: ").split()))

# # Process each element of L
# for element in L:
#     if element not in S:
#         S.add(element)      # Add element if not present
#     else:
#         S.remove(element)   # Remove element if already present

# # Output final set
# print("Final set S after processing list L:", S)

#. Write a python program which combine three sets, A, B, and C. Then, if any number in the set is greater than 10, remove all such numbers.
# A = {1, 2, 3, 11}
# B = {4, 5, 6, 12}
# C = {7, 8, 9, 13}
# # Combine the three sets
# combined_set = A | B | C
# # Remove numbers greater than 10
# final_set = {num for num in combined_set if num <= 10}
# print("Final set after removing numbers greater than 10:", final_set)

## Input sets X and Y
X = set(map(int, input("Enter elements of set X separated by space: ").split()))
Y = set(map(int, input("Enter elements of set Y separated by space: ").split()))

# Find common elements
common_set = X.intersection(Y)

# Find elements unique to either X or Y (but not both)
unique_set = X.symmetric_difference(Y)

# Display results
print("Common elements set:", common_set)
print("Unique elements set:", unique_set)
