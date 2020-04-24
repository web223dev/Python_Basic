lists = [1, 3, 4, 5, 21, 6, 3, 5, 2, 1]
unique = []

for list in lists:
      if list not in unique:
            unique.append(list)
unique.sort()
print(unique)

# My method
# lists = [1, 3, 4, 5, 21, 6, 3, 5, 2, 1]
# for list in lists:
#       if(lists.count(list) != 1):
#             lists.remove(list)
# lists.sort()
# print(lists)