num_list = []
summation = 0
count = int(input("How many numbers you want to enter? "))
if count == 0:
    print("it can't be 0")
    exit()
for i in range(count):
    number = int(input("Enter a number: "))
    num_list.append(number)
for i in num_list:
    summation += i
print(f"summation: {summation}")
average = summation / count
print(f"Average: {average}")