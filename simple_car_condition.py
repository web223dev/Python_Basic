# There are help, start, stop, quit command. And If you input "start" twice, print another message. 
temp = ''
started = False
while True:
    keyword = input(">").lower()
    if (keyword == 'help'):
        print("""
start - to start the car
stop - to stop the car
quit - to exit
            """)
    elif (keyword == 'start'):
        if started:
            print("Car alreday started...")
        else:
            started = True
            print("Car started... Ready to go!")

    elif (keyword == 'stop'):
        if not started:
            print("Car alreday stopped...")
        else:
            started = False
            print("Car stopped")
    elif (keyword == 'quit'):
        break
    else:
        print("I can't understand...")

    temp = keyword