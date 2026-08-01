number = int(input("number: "))
if number < 2:
    print("not prime")
    exit()
is_prime = True
for i in range (2, number):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print("prime")
else:
    print("not prime")

