#Computational Thinking Project 1: Smart Microwave
#Group 9
#13526016 - Sheila Zahramutia
#13526040 - Natasha Gabriel      
#18226016 - Cessnya Octavia Aphrodita
#18026016 - Zahvira Ghaida Saputra



wifi=input("Is Wi-Fi connected? (yes/no): ") #wifi connection

if wifi=="yes": #while the wifi is connected
    print("Choose command:")
    print("1. Phone")
    print("2. Smart Home")
    print("3. Voice")
    command=int(input("Enter your choice (1-3): "))
    
    while command !=1 and command !=2 and command !=3:
        print("Invalid command. Please try again.")
        command=int(input("Enter your choice (1-3): "))
    print("Command accepted")
    print("Choose action:")
    print("1. Cook")
    print("2. Reheat")
    print("3. Defrost")
    action=int(input("Enter action (1-3): "))
    while action !=1 and action !=2 and action !=3:
        print("Invalid action. Please try again.")
        action=int(input("Enter action (1-3): "))
    print("Action accepted")
    time=int(input("Enter time (minutes): "))
    #power settings
    print("Choose power mode:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    power_mode=int(input("Enter your choice (1-3): "))

    while power_mode !=1 and power_mode !=2 and power_mode !=3:
        print("Invalid power mode. Please try again.")
        power_mode=int(input("Enter your choice (1-3): "))
    if power_mode == 1:
        power="Low"
    elif power_mode == 2:
        power="Medium"
    elif power_mode == 3:
            power="High"
    else:
        print("Invalid power mode")

    if power_mode==1 or power_mode==2 or power_mode==3:
        microwave = input("Is microwave available? (yes/no): ")

        if microwave=="no":
            print("Microwave unavailable")

        else:
            door=input("Is the door closed? (yes/no): ")

            if door=="no":
                print("Check door")
            else:
                print("Action started!")
                print("Power mode:", power)
                print("Time:", time, "minutes")

                action_process=True

                while action_process==True:
                    action_finished = input("Is action finished? (yes/no): ")

                    if action_finished=="yes":
                        print("Action stopped")
                        action_process=False
                    else:
                        remaining=int(input("Enter remaining time (minutes): "))
                        print("Time remaining:", remaining, "minutes")

else:
    print("Please Connect to Wi-Fi First.")


