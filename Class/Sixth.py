#wap to compute the difference between two lists.
# color1=["red","orange","green","blue","white"]
# color2=["black","yellow","green","blue"]
# difference1=list(set(color1)-set(color2))
# difference2=list(set(color2)-set(color1))
# print("Difference between color1 and color2:", difference1)
# print("Difference between color2 and color1:", difference2)

#wap user input to compute the difference between two lists.
# color1=input("Enter the first list of colors (comma separated): ").split(",")
# color2=input("Enter the second list of colors (comma separated): ").split(",")
# difference1=list(set(color1)-set(color2))
# difference2=list(set(color2)-set(color1))
# print("Difference between color1 and color2:", difference1)
# print("Difference between color2 and color1:", difference2)

# wap to pack consecutive duplicates of a list into sublists.
# WAP to pack consecutive duplicates of a list into sublists.

# n = int(input("Enter number of elements: "))

# lst = []

# print("Enter elements:")
# for i in range(n):
#     lst.append(int(input()))

# result = []
# temp = [lst[0]]

# for i in range(1, len(lst)):
#     if lst[i] == lst[i - 1]:
#         temp.append(lst[i])
#     else:
#         result.append(temp)
#         temp = [lst[i]]

# result.append(temp)

# print("Original List:", lst)
# print("Packed List:", result)

#wap  to remove consecutive duplicates of a list.
# n = int(input("Enter number of elements: "))
# lst = []
# print("Enter elements:")
# for i in range(n):
#     lst.append(int(input()))
# result = []
# for i in range(len(lst)):
#     if i == 0 or lst[i] != lst[i - 1]:
#         result.append(lst[i])
# print("Original List:", lst)
# print("List after removing consecutive duplicates:", result)

# myString="python tu'torials "
# print(myString[-3:-8:-1])
# print(myString[-2:4:-1])

# x="Hello World"
# x=x.lower()
# y=x.replace("o","a")
# z=x.upper()
# print(z)
# print(x)
# print(y)

# str="Hello,I am learning python programming"
# lst=str.split(sep=",")
# print(lst)
# print(str.split())

# words_list = ["Hello", "World", "Python", "Programming.","I", "am", "learning", "python", "programming"]
# temp=' # '.join(words_list)
# print(temp)

# sentence="Python is a high-level, interpreted programming language."
# index=sentence.find("programming")
# print("Index of 'programming':", index)

# text="apple,orange,banana,grape,melon,lemon,kiwi,peach,pear,plum,mango,apple,orange,banana,grape,melon,lemon,kiwi,peach,pear,plum,mango"
# modified_text=text.replace("apple","fruit")
# print(modified_text)

# text="Global College is the Best College in the World"
# text1=sorted(text)
# print(text1)
# a=''.join(text1)
# print(text1)
# print(a)

x="hello,everyone.Let's learn python programming together."
x=x.replace(".","#")
x=x.replace(",",".")
x=x.replace("#",",")
print(x)