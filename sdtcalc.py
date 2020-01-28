#Speed distance time calc!
def sdtcalc():
    print("Welcome to Speed, Distance, Time Calculator!")
    while True:
#Take user input for what they are solving for, or if they input someting invalid
        solve = input("Are you solving for speed, distance or time? ")
#if user inputs time, it solves for time using data inputted
        if solve.lower() == ("time"):
                distance = float(input("How far are you launching the object? "))
                while True:
                    dunit = str(input("In Miles or Kilometers? "))
                    if dunit.lower() == "miles":
                        print(dunit, "it is then!")
                        break
                    elif dunit.lower() == "kilometers": 
                        print(dunit, "it is then!")
                        break
                    else:
                        print("Apologies! That unit is not recognized...")
                        continue
                if dunit.lower() == "miles":
                    speed = float(input("How fast is the object traveling (mph)? "))
                    time = (distance // speed)
                    ecirc = (distance // 24091)
                    print("The object will take", time, "hours to cover", distance, "miles at", speed, "mph!")
                    if ecirc >= 1:
                        print("The object will circumnavigate the globe", ecirc, "time(s)!")
                    else:
                        print("The object will not circumnavigate the globe...")
                    while True:
                        cont = input("Run Again? (Y/N)")
                        if cont == "Y":
                            sdtcalc()
                        elif cont == "y":
                            sdtcalc()
                        elif cont == "N":
                            quit()
                        elif cont == "n":
                            quit()
                        else:
                            print("Invalid Input")
                            continue
                if dunit.lower() == "kilometers":
                    speed = float(input("How fast is the object traveling (kph)? "))
                    time = (distance // speed)
                    ecirc = ((distance // 24091))
                    print("The object will take", time, "hours to cover", distance, "kilometers at", speed, "kph!")
                    if ecirc >= 1:
                        print("The object will circumnavigate the globe", ecirc, "time(s)!")
                    else:
                        print("The object will not circumnavigate the globe...")
                    while True:
                        cont = input("Run Again? (Y/N)")
                        if cont == "Y":
                            sdtcalc()
                        elif cont == "y":
                            sdtcalc()
                        elif cont == "N":
                            quit()
                        elif cont == "n":
                            quit()
                        else:
                            print("Invalid Input")
                            continue
#if user inputs speed, it solves for speed using data inputted

        elif solve.lower() == ("speed"):
            while True:
                distance = float(input("How far are you launching the object? "))
                while True:
                    dunit = str(input("In Miles or Kilometers? "))
                    if dunit.lower() == "miles":
                        print(dunit, "it is then!")
                        break
                    elif dunit.lower() == "kilometers":
                        print(dunit, "it is then!")
                        break
                    else:
                        print("Apologies! That unit is not recognized...")
                        continue
                if dunit.lower() == "miles":
                    time = float(input("How long will the object be traveling for (hours)? "))
                    speed = (distance // time)
                    print("The object will take", time, "hours to cover", distance, "miles at", speed, "mph!")
                    while True:
                        cont = input("Run Again? (Y/N)")
                        if cont.lower() == "y":
                            sdtcalc()
                        elif cont.lower() == "n":
                            quit()
                        else:
                            print("Invalid Input")
                            continue
                if dunit.lower() == "kilometers":
                    time = float(input("How long will the object be traveling for (hours)? "))
                    speed = (distance // time)
                    print("The object will take", time, "hours to cover", distance, "kilometers at", speed, "kph!")
                    while True:
                        cont = input("Run Again? (Y/N)")
                        if cont.lower() == "y":
                            sdtcalc()
                        elif cont.lower() == "n":
                            quit()
                        else:
                            print("Invalid Input")
                            continue
                            
 #if user inputs distance, it solves for distance using data inputted

        elif solve.lower() == ("distance"):
            while True:
                speed = float(input("How fast is the object traveling? "))
                while True:
                    sunit = str(input("In Miles or Kilometers? "))
                    if sunit.lower() == "miles":
                        print(sunit, "it is then!")
                        break
                    elif sunit.lower() == "kilometers":
                        print(sunit, "it is then!")
                        break
                    else:
                        print("Apologies! That unit is not recognized...")
                        continue
                if sunit.lower() == "miles":
                    time = float(input("How long will the object be traveling for (hours)? "))
                    distance = (speed * time)
                    print("The object will take", time, "hours to cover", distance, "miles at", speed, "mph!")
                    while True:
                        cont = input("Run Again? (Y/N)")
                        if cont.lower() == "y":
                            sdtcalc()
                        elif cont.lower() == "n":
                            quit()
                        else:
                            print("Invalid Input")
                            continue
                if sunit.lower() == "kilometers":
                    time = float(input("How long will the object be traveling for (hours)? "))
                    distance = (speed * time)
                    print("The object will take", time, "hours to cover", distance, "kilometers at", speed, "kph!")
                    while True:
                        cont = input("Run Again? (Y/N)")
                        if cont.lower() == "y":
                            sdtcalc()
                        elif cont.lower() == "n":
                            quit()
                        else:
                            print("Invalid Input")
                            continue
        else:
            print("Invalid Input")
            continue
