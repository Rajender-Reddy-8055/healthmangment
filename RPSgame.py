import random
L = ["scissor","paper","rock"]
i = U = D = AI = 0
while True:
    x = random.choice(L)
    y = input("\n Choose any: \n rock\t paper\t scissor\t exit \n")
    print(f"You choose {y}")

    if(y == "exit"):
        print("Here are the final results")
        break
    elif y == L[0]:
        if x == L[0]:
            print(f"Computer choose {x}")
            print("draw")
            D = D+1
        elif x == L[1]:
            U = U+1
            print(f"Computer choose {x}")
            print("you won")
        else:
            print(f"Computer choose {x}")
            print("you lost")
            AI = AI+1
    elif y == L[1]:
        if x == L[0]:
            print(f"Computer choose {x}")
            print("you lost")
            AI = AI+1
        elif x == L[1]:
            print(f"Computer choose {x}")
            print("draw")
            D = D+1
        else:
            print(f"Computer choose {x}")
            print("you won")
            U = U+1
    elif y == L[2]:
        if x == L[0]:
            print(f"Computer choose {x}")
            print("you won")
            U = U+1
        elif x == L[1]:
            print(f"Computer choose {x}")
            print("you lost")
            AI = AI + 1
        else:
            print(f"Computer choose {x}")
            print("draw")
            D = D+1
    else :
        print("Choose wrong option...try again")
        continue           
print(f"your score = {U} , computer score = {AI} and draw matches ={D}")
if U > AI:
    print("you won....!")
elif U < AI:
    print("you lost :(..better luck time")
else:
    print("draw match!!")
