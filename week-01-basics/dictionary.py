final = ""
phone_number = input("Phone: ")
number = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
}
for i in phone_number:
    final += number.get(i , "!") + " "
                        
print(final)

#if final == "":
        #final += number[i]
    #else:
        #final += " "
        #final += number[i]"""
