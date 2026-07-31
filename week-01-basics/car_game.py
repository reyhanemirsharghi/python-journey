command = ""
started = False
while True :
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Hey the car is already started")
        else :
            started = True
            print("Car started... Ready to go")
    elif command == "stop" :
            if not started :
                print("Hey the car is already stopped.")
            else:
                started = False
                print("car stopped.")
    elif command == "help":
        print(""" 
start - to start the car
stop - to stop the car 
quit - to exit """)
    elif command == "quit":
        break
    else:
        print("sorry... I don't understand that")
