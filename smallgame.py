import random
L = ["scissor","paper","rock"]
i = U = D = AI = 0
while i < 10:
    x = random.choice(L)
    y = input("Choose any: \n rock\t paper\t scissor\n")
    print(f"You choose {y}")

    if y == L[0]:
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
        print(f"turns left {9-i}")
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
        print(f"turns left {9 - i}")
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
            print(f"Computer choose{x}")
            print("draw")
            D = D+1
        print(f"turns left {9 - i}")
    else :
        print("Choose wrong option...try again")
        continue           
    i = i+1
    continue
print(f"your score = {U} , computer score = {AI} and draw matches ={D}")
if U > AI:
    print("you won....!")
elif U < AI:
    print("you lost :(..better luck time")
else:
    print("draw match!!")
