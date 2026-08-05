score_list = []
score_summation = 0
while True:
    student_name = input("Name: ")
    count = int(input("How many scores you want to enter? "))
    for i in range (count):
        while True:
            try:
                score = int(input("Score: "))
                if 0 <= score <= 20:
                    score_list.append(score)
                    break
            except ValueError:
                print("Please enter a number.")
            
    
    for i in score_list:
        score_summation += i
    

    maximum_score = score_list[0]
    minimum_score = score_list[0]
    for i in score_list:
        if i > maximum_score:
            maximum_score = i
        elif i < minimum_score:
            minimum_score = i


    score_average = score_summation / count
    print(student_name)
    print(f"scores: {score_list}")
    print(f"total: {score_summation}")
    print(f"average: {score_average}")
    print(f"Heighest score is: {maximum_score}")
    print(f"Lowest score is: {minimum_score}")

    break



    
    