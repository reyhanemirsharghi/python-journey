number = [1,1,2,3,4,5,5,5,6]
new_list = []
for num in number:
    if num not in new_list:
        new_list.append(num)
print(new_list)

