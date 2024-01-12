# 1-masala
# list = [1, 2, 3.5, 4, 5, 6, 7, 8, 9]
# sum = 0
# for x in list:
#   sum += x
# print(sum)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 2-masala
# list1 = [4, 3, 2, 1]      # ➞ [1, 2, 3, 4]
#
# a = len(list1)
# for x in range(0, a):
#     for y in range(0, a - x - 1):
#         if list1[y] > list1[y + 1]:
#             list1[y], list1[y + 1] = list1[y + 1], list1[y]
#
# print(list1)
#
# list2 = [7, 8, 11, 66]    # ➞ [66, 11, 8, 7]
#
# n = len(list2)
# for x in range(0, n):
#     for y in range(0, n - x - 1):
#         if list2[y] < list2[y + 1]:
#             list2[y], list2[y + 1] = list2[y + 1], list2[y]
#
# print(list2)
#
# list3 = [1, 2, 3, 4]      # ➞ [1, 2, 3, 4]
# print(list3)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 3-masala
# n = 11              # ➞ [2, 2]
#
# print([n//2, n - n//2])

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 4-masala
# jazz = ["G", "F", "C"]      # ➞ ["G7", "F7", "C7"]
# a = []
# for i in jazz:
# 	if i[-1] != "7":
# 		a.append(i + "7")
# 	else:
# 		a.append(i)
#
# print(a)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 5-masala
# list = [1, 2, "aasf", "1", "123", 123]     # ➞ [1, 2, 123]
# filter_list = []
# for x in list:
# 	if type(x) == int:
# 		filter_list.append(x)
#
# print(filter_list)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 6-masala
# numbers = [1, 2, 3, 4, 5, 6]
#
# first = numbers[0]
# middle = numbers[1:-1]
# last = numbers[-1]
#
# print(f"first{[first]}")
# print(f"middle{middle}")
# print(f"last{[last]}")

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 8-masala
# def process_list(input_list):
#     input_number = int(input("Istalgan sonni kiriting: "))
#     if input_number in input_list:
#         input_list.remove(input_number)
#         input_list.append(input_number)
#         input_list.append(input_number)
#         print(my_list)
#     else:
#         print("fatalnaya oshibka !!!!")
#
# Test qilish
# my_list = [3, 6, 9, 12]
# process_list(my_list)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 7-masala
# list = ([
#   "###",
#   "###",
#   "###"
# ])
# n = len(''.join(list))
# print(n)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 9-masala
# list1 = [8]
# list2 = []
#
# for x in list1:
#     for y in range(2, x + 2, 2):
#         list2.append(y)
# print(list2)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 10-masala
# list1 = ["A", 0, "Edabit", 1729, "Python", "1729"]
# list2 = []
#
# for x in list1:
#     if type(x) == int:
#         list2.append(x)
#
# print(list2)
