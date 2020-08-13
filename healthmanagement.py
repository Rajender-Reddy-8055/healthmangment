def getdate():
    import datetime
    return datetime.datetime.now()


t = getdate()
L = ["Harry", "Rohan", "Hammad"]
print("whose log do u want to access Harry \n Rohan \n Hammad ")
Name = input()
if Name == L[0]:
    D = ["Diet", "Exercise"]
    print("Diet OR Exercise")
    x = input()
    if x == D[0]:
        Z = ["Enter", "Retrive"]
        print("Enter or Retrive:")
        y = input()
        if y == Z[0]:
            with open("harrydiet.txt", "a") as H:
                print("Please enter what did you consume:")
                print(t)
                s = input()
                print(H.writelines(s+"\n"))
        else:
            with open("harrydiet.txt") as H:
                print(t)
                print(H.read())
    else:
        Z = ["Enter", "Retrive"]
        print("Enter or Retrive:")
        y = input()
        if y == Z[0]:
            with open("harryexe.txt", "a") as H:
                print("Please enter exercises done:")
                print(t)
                s = input()
                print(H.writelines(s+"\n"))
        else:
            with open("harryexe.txt") as H:
                print(t)
                print(H.read())
elif Name == L[1]:
    D = ["Diet", "Exercise"]
    print("Diet OR Exercise")
    x = input()
    if x == D[0]:
        Z = ["Enter", "Retrive"]
        print("Enter or Retrive:")
        y = input()
        if y == Z[0]:
            with open("rohandiet.txt", "a") as H:
                print("Please enter what did you consume:")
                print(t)
                s = input()
                print(H.writelines(s+"\n"))
        else:
            with open("rohandiet.txt") as H:
                print(t)
                print(H.read())
    else:
        Z = ["Enter", "Retrive"]
        print("Enter or Retrive:")
        y = input()
        if y == Z[0]:
            with open("rohanexe.txt", "a") as H:
                print("Please enter exercises done:")
                print(t)
                s = input()
                print(H.writelines(s+"\n"))
        else:
            with open("rohanexe.txt") as H:
                print(t)
                print(H.read())
else:
    D = ["Diet", "Exercise"]
    print("Diet OR Exercise")
    x = input()
    if x == D[0]:
        Z = ["Enter", "Retrive"]
        print("Enter or Retrive:")
        y = input()
        if y == Z[0]:
            with open("hammaddiet.txt", "a") as H:
                print("Please enter what did you consume:")
                print(t)
                s = input()
                print(H.writelines(s+"\n"))
        else:
            with open("hammaddiet.txt") as H:
                print(t)
                print(H.read())
    else:
        Z = ["Enter", "Retrive"]
        print("Enter or Retrive:")
        y = input()
        if y == Z[0]:
            with open("hammadexe.txt", "a") as H:
                print("Please enter exercises done:")
                print(t)
                s = input()
                print(H.writelines(s+"\n"))
        else:
            with open("hammadexe.txt") as H:
                print(t)
                print(H.read())
