import random
x=int(input("Enter the number of dices you want: " ))

for _ in range(x):
        w=int(random.randint(1,6))
        if (w==1):
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
            print("\n")
        if w == 2:
            print("[-----]")
            print("[ 0   ]")
            print("[     ]")
            print("[   0 ]")
            print("[-----]")
            print("\n")                        

        if w == 3:
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
            print("\n")
        if w == 4:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
            print("\n")
        if w == 5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
            print("\n")
        if w == 6:
            print("[-----]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[-----]")
            print("\n")