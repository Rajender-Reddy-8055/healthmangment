import random
L = ["SNAKE", "WATER", "GUN"]
i = 0
U = 0
AI = 0
L[0] = 1
L[1] = 2
L[2] = 3
while i < 10:
    x = random.choice(L)
    print("Choose any: \n 1 for SNAKE...2 for WATER...3 for GUN")
    y = input()
    if y == L[0]:
        print(f"turns left {9-i}")
        for c in L:
            if x == L[0]:
                print("draw")
                break
            elif x == L[1]:
                U = U+1
                break
                print("you won")
            else:
                print("you lost")
                AI = AI+1
                break
    elif y == L[1]:
        print(f"turns left {9 - i}")
        for c in L:
            if x == L[0]:
                print("you lost")
                AI = AI+1
                break
            elif x == L[1]:
                print("draw")
                break
            else:
                print("you won")
                U = U+1
                break
    else:
        print(f"turns left {9 - i}")
        for c in L:
            if x == L[0]:
                print("you won")
                U = U+1
                break
            elif x == L[1]:
                print("you lost")
                AI = AI + 1
                break
            else:
                print("draw")
                break
    i = i+1
    continue
print(f"your score = {U}  and ai score = {AI}")
if U > AI:
    print("you won....!")
elif U < AI:
    print("you lost :(..better luck time")
else:
    print("draw match!!")
