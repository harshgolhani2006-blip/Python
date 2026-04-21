#tuple.
#way to create tuple.
#1. using parentheses.
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)

#2.using tuple() constructor.
# my_tuple = tuple([1, 2, 3, 4, 5])
# print(my_tuple)

#3. without parentheses.
# my_tuple = 1, 2, 3, 4, 5
# print(my_tuple)
 
 #4. single element tuple.
# single_element_tuple = (5,)
# print(single_element_tuple)

#5. empty tuple.
# empty_tuple = ()
# print(empty_tuple)

#6.type of tuple.
# my_tuple = (1, 2, 3, 4, 5)
# print(type(my_tuple))

#wap to create a tuple with 5 elements and print the tuple.
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)

# tpl=(1,2,3,4,5,6)
# print(id(tpl))
# tpl+=("hello", "world", "python", "programming", 19, 2, 3, 4, 5, 6)
# print(tpl)
# print(id(tpl))

#deleting a tuple.  
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)
# del my_tuple
# print(my_tuple)

#counting the number of occurrences of an element in a tuple.
# my_tuple = (1, 2, 3, 4, 5, 2, 3, 2)
# count_of_2 = my_tuple.count(2)
# print("Count of 2 in the tuple:", count_of_2)

#reverse a tuple is not possible because tuples are immutable. However, you can create a new tuple that is the reverse of the original tuple.
# my_tuple = (1, 2, 3, 4, 5)
# reversed_tuple = my_tuple[::-1]
# print("Original tuple:", my_tuple)
# print("Reversed tuple:", reversed_tuple)

#sorting a tuple is not possible because tuples are immutable. However, you can create a new sorted tuple from the original tuple.
# my_tuple = (5, 2, 3, 1, 4)
# sorted_tuple = tuple(sorted(my_tuple))
# print("Original tuple:", my_tuple)
# print("Sorted tuple:", sorted_tuple)

tpl=(1, 2, 3, 4, 5,6,7,8,9,10)
tpl=list(tpl)
tpl[4]=40
tpl=tuple(tpl)
print(tpl)
